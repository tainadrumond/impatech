import pygame
import random
import math

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle System - Multiple Fire Flows")

# Configurações das partículas
particles = []
MAX_PARTICLES = 2000000  # Aumenta o número de partículas
GRAVITY = -0.02  # Partículas se movem para cima
ATTRACTION_POINT = (WIDTH // 2, HEIGHT - 300)  # Ponto para o qual as partículas serão atraídas (mais alto)

# Função para adicionar novas partículas com diferentes tamanhos e velocidades
def emit_fire_particles():
    for _ in range(10000):  # Aumenta o número de partículas emitidas por ciclo
        x = random.randint(WIDTH // 2 - 150, WIDTH // 2 + 150)  # Largura de emissão variada
        y = HEIGHT - random.randint(80, 150)  # Altura inicial das partículas (variada para múltiplas chamas)

        size = random.randint(1, 3)  # Partículas ainda menores
        life = random.randint(20, 50)  # Vida das partículas mais curta

        particle = {
            "x": x,
            "y": y,
            "vx": random.uniform(-1, 1),
            "vy": random.uniform(-2, -4),  # Movimentação mais vertical para simular fogo subindo
            "size": size,
            "life": life,
            "color": (227, random.randint(100, 150), 0)  # Cor inicial laranja/vermelho
        }
        particles.append(particle)

# Função para aplicar a atração para o ponto central
def apply_attraction(particle):
    # Distância entre a partícula e o ponto de atração
    dx = ATTRACTION_POINT[0] - particle["x"]
    dy = ATTRACTION_POINT[1] - particle["y"]
    distance = math.sqrt(dx ** 2 + dy ** 2)
    
    # Se a partícula estiver perto do ponto de atração, aplica a força de atração
    if distance > 0:
        attraction_strength = 0.1  # Força de atração
        # Normaliza a direção da atração e aplica na velocidade
        particle["vx"] += (dx / distance) * attraction_strength
        particle["vy"] += (dy / distance) * attraction_strength

# Loop principal da animação
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))  # Limpa a tela a cada frame

    # Emissão contínua de partículas ao longo de uma linha horizontal
    emit_fire_particles()

    # Atualização e desenho das partículas
    for particle in particles:
        # Aplica a atração para o ponto central
        apply_attraction(particle)
        
        # Atualiza as posições das partículas com gravidade
        particle["x"] += particle["vx"]
        particle["y"] += particle["vy"] + GRAVITY
        particle["life"] -= 1

        # Gradiente de cor: a partícula clareia conforme a vida diminui
        r, g, b = particle["color"]
        particle["color"] = (min(255, r + 3), min(255, g + 3), b)

        # Desenha a partícula
        screen.set_at((int(particle["x"]), int(particle["y"])), particle["color"])
        # pygame.draw.circle(screen, particle["color"], (int(particle["x"]), int(particle["y"])), particle["size"])

    # Remove partículas "mortas"
    particles = [p for p in particles if p["life"] > 0]

    # Limita o número de partículas
    if len(particles) > MAX_PARTICLES:
        particles = particles[-MAX_PARTICLES:]

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)

    # Verifica se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
