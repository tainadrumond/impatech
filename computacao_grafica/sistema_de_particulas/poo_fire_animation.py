import pygame
import random
import math

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema de Partículas - Fogo")

# Configurações das partículas
MAX_PARTICLES = 200000  # Aumenta o número de partículas
GRAVITY = -0.02  # Gravidade que afeta as partículas

class Particula:
    def __init__(self, x, y, vx, vy, size, life, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.life = life
        self.color = color
    
    def apply_attraction(self, ponto_atracao):
        """Aplica atração para o ponto de atração (ponto máximo de altura e ponto médio da largura)."""
        dx = ponto_atracao[0] - self.x
        dy = ponto_atracao[1] - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance > 0:
            attraction_strength = 0.1  # Força de atração
            self.vx += (dx / distance) * attraction_strength
            self.vy += (dy / distance) * attraction_strength
    
    def update(self):
        """Atualiza a posição e a vida da partícula com gravidade e atratividade."""
        self.x += self.vx
        self.y += self.vy + GRAVITY  # Aplica a gravidade

        self.life -= 1  # Decrementa o tempo de vida da partícula

        # Gradiente de cor: a partícula clareia conforme a vida diminui
        r, g, b = self.color
        self.color = (min(255, r + 5), min(255, g + 5), b)
    
    def is_alive(self):
        """Verifica se a partícula ainda está viva."""
        return self.life > 0
    
    def draw(self, screen, formato="circulo"):
        """Desenha a partícula na tela, dependendo do formato especificado."""
        if formato == "circulo":
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        elif formato == "quadrado":
            pygame.draw.rect(screen, self.color, (self.x - self.size / 2, self.y - self.size / 2, self.size, self.size))


class SistemaDeParticulas:
    def __init__(self, origem, formato="circulo", largura_fogo=200, altura_fogo=300):
        self.origem = origem
        self.formato = formato
        self.largura_fogo = largura_fogo  # Largura do início do fogo
        self.altura_fogo = altura_fogo  # Altura máxima que o fogo atinge
        self.particulas = []

    def emitir_particulas(self, num_particulas=50):
        """Emite partículas da origem com formatos e características variáveis, influenciado pela largura e altura do fogo."""
        for _ in range(num_particulas):
            # A largura de emissão varia entre a largura do fogo
            x = random.randint(self.origem[0] - self.largura_fogo // 2, self.origem[0] + self.largura_fogo // 2)
            # A altura inicial varia, mas está limitada à base do fogo
            y = self.origem[1]

            # O tamanho e o tempo de vida das partículas são influenciados pela altura do fogo
            size = random.randint(1, 3)  # Partículas menores
            life = random.randint(20, 50) + int(self.altura_fogo / 10)  # Vida das partículas maior se a altura do fogo for grande

            # A velocidade das partículas também é influenciada pela altura do fogo
            vy = random.uniform(-2, -4) + self.altura_fogo / 100  # A velocidade vertical aumenta com a altura
            vx = random.uniform(-1, 1)  # A velocidade horizontal ainda é aleatória

            # Cor inicial das partículas (de laranja a vermelho)
            color = (255, random.randint(100, 150), 0)

            particle = Particula(
                x=x,
                y=y,
                vx=vx,
                vy=vy,
                size=size,
                life=life,
                color=color
            )
            self.particulas.append(particle)

    def atualizar_particulas(self):
        """Atualiza as partículas do sistema."""
        ponto_atracao = (self.origem[0], self.origem[1] - self.altura_fogo)  # Ponto de atração na altura máxima
        for particle in self.particulas:
            particle.apply_attraction(ponto_atracao)  # Aplica a atração pela origem
            particle.update()

        # Remove partículas "mortas"
        self.particulas = [p for p in self.particulas if p.is_alive()]

    def desenhar_particulas(self, screen):
        """Desenha as partículas na tela com base no formato especificado."""
        for particle in self.particulas:
            # Se a partícula atingir a altura máxima do fogo, ela desaparece
            if particle.y < self.origem[1] - self.altura_fogo:
                particle.life = 0
            particle.draw(screen, formato=self.formato)

# Inicialização do sistema de partículas
sistema_fogo1 = SistemaDeParticulas(origem=(WIDTH // 2, HEIGHT - 100), formato="circulo", largura_fogo=300, altura_fogo=350)
sistema_fogo2 = SistemaDeParticulas(origem=(WIDTH // 3, HEIGHT - 100), formato="circulo", largura_fogo=300, altura_fogo=350)

# Loop principal da animação
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))  # Limpa a tela a cada frame

    # Emissão contínua de partículas ao longo da largura do fogo
    sistema_fogo1.emitir_particulas()

    # Atualização e desenho das partículas
    sistema_fogo1.atualizar_particulas()
    sistema_fogo1.desenhar_particulas(screen)

    # Limita o número de partículas
    if len(sistema_fogo1.particulas) > MAX_PARTICLES:
        sistema_fogo1.particulas = sistema_fogo1.particulas[-MAX_PARTICLES:]
        
    
    # Emissão contínua de partículas ao longo da largura do fogo
    sistema_fogo2.emitir_particulas()

    # Atualização e desenho das partículas
    sistema_fogo2.atualizar_particulas()
    sistema_fogo2.desenhar_particulas(screen)

    # Limita o número de partículas
    if len(sistema_fogo2.particulas) > MAX_PARTICLES:
        sistema_fogo2.particulas = sistema_fogo2.particulas[-MAX_PARTICLES:]
    

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(30)

    # Verifica se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
