import random
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return '('+str(self.x)+', '+str(self.y)+')'

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def circle_from_two_points(p1, p2):
    center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    radius = distance(p1, p2) / 2
    return center, radius

def circle_from_three_points(p1, p2, p3):
    ax, ay = p1.x, p1.y
    bx, by = p2.x, p2.y
    cx, cy = p3.x, p3.y
    
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    center = Point(ux, uy)
    radius = distance(center, p1)
    return center, radius

def is_point_in_circle(p, center, radius):
    return distance(p, center) <= radius

steps = []

def welzl(points, boundary_points=[]):
    steps.append((list(points), list(boundary_points)))
    
    if len(points) == 0 or len(boundary_points) == 3:
        if len(boundary_points) == 0:
            return Point(0, 0), 0
        elif len(boundary_points) == 1:
            return boundary_points[0], 0
        elif len(boundary_points) == 2:
            return circle_from_two_points(boundary_points[0], boundary_points[1])
        elif len(boundary_points) == 3:
            return circle_from_three_points(boundary_points[0], boundary_points[1], boundary_points[2])

    p = points.pop()
    center, radius = welzl(points, boundary_points)

    if is_point_in_circle(p, center, radius):
        points.append(p)
        return center, radius

    boundary_points.append(p)
    result = welzl(points, boundary_points)
    boundary_points.pop()
    points.append(p)
    
    return result

def find_minimum_enclosing_circle(points, boundary_points=[]):
    points_copy = points[:]
    # random.shuffle(points_copy)
    center, radius = welzl(points, boundary_points)
    return center, radius

def print_points(points):
    p_str = []
    for p in points:
        p_str.append(str(p))
    print(', '.join(p_str))

def manual_step_through(points):
    global steps
    steps.clear()
    
    boundary_points = []
    find_minimum_enclosing_circle(points, boundary_points)
    steps.append((list(points), list(boundary_points)))
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    
    # Inicializa a figura e o círculo vazio
    boundary_circle = Circle((0, 0), 0, fill=False, edgecolor='red')
    ax.add_patch(boundary_circle)
    
    # Atualiza os passos no gráfico
    frame = [0]

    def update_step(event):
        if event.key == "right" and frame[0] < len(steps) - 1:
            frame[0] += 1
        elif event.key == "left" and frame[0] > 0:
            frame[0] -= 1
        else:
            return
        
        # Limpa a área de desenho sem apagar os limites e título
        ax.cla()  # Usando ax.cla() em vez de ax.clear()
        ax.set_aspect('equal')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)

        points, boundary_points = steps[frame[0]]
        
        # Plota os pontos em azul e os pontos de borda em verde
        for p in points:
            ax.plot(p.x, p.y, 'bo')  # Pontos azuis (os pontos de entrada)
        for bp in boundary_points:
            ax.plot(bp.x, bp.y, 'go')  # Pontos verdes (os pontos de borda)

        # Calcula o círculo mínimo baseado nos pontos de borda
        if len(boundary_points) == 2:
            c, r = circle_from_two_points(boundary_points[0], boundary_points[1])
        elif len(boundary_points) == 3:
            c, r = circle_from_three_points(boundary_points[0], boundary_points[1], boundary_points[2])
        else:
            c, r = Point(0, 0), 0

        # Desenha o círculo com as coordenadas de centro e raio calculados
        circle = Circle((c.x, c.y), r, fill=False, edgecolor='red')
        ax.add_patch(circle)
        
        plt.draw()

    # Liga os eventos de teclado à função de atualização de passo
    fig.canvas.mpl_connect('key_press_event', update_step)
    plt.show()
    plt.draw()
    
    return frame[0]


# mylist = [
#     Point(1, 0),            # A
#     Point(0.309, 0.951),    # B
#     Point(-0.809, 0.588),   # C
#     Point(-0.809, -0.588),  # D
#     Point(0.309, -0.951)    # E
# ]

# t = manual_step_through(mylist)
# print(t)

test_points = [Point(random.uniform(-8, 8), random.uniform(-8, 8)) for _ in range(10)]
manual_step_through(test_points)

# print(len(steps))
