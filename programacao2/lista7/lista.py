# EXERCÍCIO 1
from collections import defaultdict

def find_judge(n_people: int, trust: list):
    # Save, for each person, the people who trusts in them.
    people_who_trust = defaultdict(set)
    # Save, for each person, the people they trust.
    trusted_people = defaultdict(set)
    
    # Initialize the dictionaries with the entry list info
    for trusts, trusted in trust:
        people_who_trust[trusted].add(trusts)
        trusted_people[trusts].add(trusted)
        
    # Find the person that is trusted by everyone and that doens't trust anyone
    for trusted, people_who_trust in people_who_trust.items():
        if len(people_who_trust) != n_people - 1:
            continue
        if len(trusted_people[trusted]) == 0:
            return trusted
        
    return -1

t = [[1, 2], [1, 3], [2, 3]]
n = 3
print(find_judge(n, t))

t = [[1, 3], [2, 3], [3, 1]]
n = 3
print(find_judge(n, t))


# EXERCÍCIO 2 - Item (a)
from collections import deque, defaultdict

def calculate_distances(points) -> dict[tuple[int, int], float]:
    '''
    Calculate the distances between each point of the given list
    '''
    # Distance by edge
    distances: dict[tuple[int, int], float] = dict()
    
    for i, pi in enumerate(points):
        for j in range(i+1, len(points)):
            pj = points[j]
            edge = (pi, pj)
            
            # Calculate the distance between the points of the edge
            distance = ((pi[0] - pj[0])**2 + (pi[1] - pj[1])**2)**(1/2)
            distances[edge] = distance
    return distances

def nodes_are_connected(node1, node2, adj_list):
    '''
    Bfs to check if two nodes are connected
    '''
    queue = deque([node1])
    visited = set([node1])
    
    # Search through the whole connected component that contains
    # the node 1 
    while len(queue) != 0:
        node = queue.popleft()
        
        for neighbor in adj_list[node]:
            if neighbor == node2:
                return True
            if not neighbor in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False
        
        
def minimum_spanning_tree(points: list[tuple]):
    '''
    Calculate minimum spanning tree for the given list of points
    '''
    points = list(set(points))
    adj_list: dict[tuple, list[tuple]] = defaultdict(list)
    distances = calculate_distances(points)
    # List of tuples that contain the edge and its distance
    edges_ordered_by_distance = sorted(distances.items(), key=lambda item: item[1])
    
    for edge, distance in edges_ordered_by_distance:
        node1, node2 = edge
        # If the nodes are already connected, adding an edge between them would
        # create a cycle. Therefore, it only adds this egde to the MST if the
        # nodes aren't connected
        if not nodes_are_connected(node1, node2, adj_list):
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
        
    return adj_list


# EXERCÍCIO 2 - Item (b)
# Para demonstrar que o problema de calcular a Minimum-spanning Tree é Ω(nlog(n)), vamos reduzir o problema
# de ordenação a ele.
# Dado um conjunto de números, ordenaremos eles da seguinte forma:
# Associaremos cada número n ao ponto (n, 0) no R^2. Em seguida, calcularemos a MST para o conjunto resultante.
# O resultado será uma árvore cujas arestas conectam um ponto aos dois pontos mais próximos, exceto para os dois
# pontos extremos da lista, que terão apenas um vizinho cada. Entre esses dois pontos, escolhemos o de menor
# coordenada x. Depois, percorremos a árvore partindo desse ponto. A ordem em que a árvore é percorrida
# indica a ordem da lista dos pontos ordenados pela coordenada x, ou seja, por cada um dos n números iniciais.
# Com isso, obtemos o resultado da ordenação.
# Como ordenação é Θ(n log n) e pode ser reduzida à MST, o problema de calcular a Minimum-spanning Tree é Ω(nlog(n)).


# EXERCÍCIO 2 - Item (c)
# Considerando E o número de arestas e V o número de vértices:
# Como temos arestas entre todos os pontos, E = V escolhe 2 = (V^2 - V)/2
#
# O algoritmo de Kruskal, que utiliza a estrutura Union Find, é O(E log V) quando já recebe os pesos (ou distâncias) das arestas
# a serem consideradas de antemão. Para a nossa entrada, a complexidade é O(V^2 log V)=O(V^2).
#
# No nosso caso, precisamos calcular as distâncias entre todos os pontos e ordená-las. O cálculo das distâncias é feito 
# em O(V^2). Além disso, a ordenação das arestas resultantes é O(V^2 log V)=O(V^2). Logo, a complexidade desse passo é O(V^2).
#
# A partir desse ponto, estamos na situação inicial do algoritmo de Kruskal que tem complexiade O(V^2). No entanto,
# o algoritmo implementado aqui calcula uma bfs para cada aresta percorrida. A complexidade da bfs é O(V^2) (por causa do
# número de arestas). Como ela é calculada para cada uma das (V^2 + V)/2 arestas, a complexidade do loop é O(V^4).
#
# Como, mesmo desconsiderando a necessidade de calcular as distâncias entre todos os vértices, o algoritmo aqui implementado
# tem complexidade pior do que o algoritmo de Kruskal, ele não é ótimo.


# EXERCÍCIO 3
def interpolate(known_points: list[tuple], unknown_x: float):
    '''
    Interpolate the given points into a polynomial using Lagrange's method 
    to approximate the function value in the unknown point.
    '''
    L = [1 for _ in known_points]
    for i, pi in enumerate(known_points):
        xi, yi = pi
        for j, pj in enumerate(known_points):
            xj, yj = pj
            if i == j:
                continue
            L[i] *= (unknown_x - xj)/(xi - xj)
    
    res = 0
    for i, l in enumerate(L):
        yi = known_points[i][1]
        res += yi * l
        
    return res
                
# EXERCÍCIO 3 - Item (a)
temperature_by_height = [(15, 200), (9, 400), (5, 600), (3, 800), (-2, 1000), (-5, 1200), (-15, 1400)]
print(interpolate(temperature_by_height, 0))

# EXERCÍCIO 3 - Item (b)
height_by_temperature = [(200, 15), (400, 9), (600, 5), (800, 3), (1000, -2), (1200, -5), (1400, -15)]
print(interpolate(height_by_temperature, 700))


# EXERCÍCIO 4
from root_finder import RealFunction, Interval, grid_search, bissect

def newton_root(f: RealFunction, x0: float, erroTol: float = 1e-4, maxItr: int = 1e4, eps: float = 1e-6) -> float:
    '''
    Newton's method to find a root.
    '''
    x = x0
    for _ in range(int(maxItr)):
        # If the function has a value equal or smaller than the error tolerance,
        # then the root has been found
        if abs(f(x)) <= erroTol:
            return x
        
        # A derivative too close to 0 would crash the step that has the derivative
        # in the denominator
        if abs(f.prime_safe(x)) < eps:
            raise ValueError("Derivative too close to zero.")
        
        # Finds the next x to be evaluated
        x -= (f(x) / f.prime_safe(x))
    
    raise ValueError("Did not converge in the maximum number of iterations.")

# Use case:
class QuadraticFunction(RealFunction):
    """
    Represents x^2 - 4
    """
    f = lambda self, x: x**2 - 4
    prime = lambda self, x: 2 * x
    domain = Interval(-3, 3)

quad_func = QuadraticFunction()

# Find interval that contains a root
interval_guess = grid_search(quad_func, grid_freq=15)
if interval_guess:
    # Find the root with bissect
    refined_interval = bissect(quad_func, search_space=interval_guess)
    print('bissect:', refined_interval)

    # Find the root with Newton's method
    try:
        root = newton_root(quad_func, x0=refined_interval.haf)
        print('Newton:', root)
    except ValueError as e:
        print(e)


# EXERCÍCIO 5
from poly_interpolant import interpolater, VandermondeMatrix
from scipy.interpolate import lagrange
import time
import random

class LagrangeInterpolater(interpolater):
    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        # Calculate the approximation polynomial using Lagrange's method
        self.poly = lagrange(x, y)
        
    def evaluate(self, X):
        return self.poly(X)

# Time test:

# Generate the entries randomly:
list_size = 100
n_lists = 100
xs = [[random.uniform(0, 100) for _ in range(list_size)] for _ in range(n_lists)]
ys = [[random.uniform(0, 100) for _ in range(list_size)] for _ in range(n_lists)]

# Calculate the time for Vandermond
start_time = time.time()
for i in range(n_lists):
    VandermondeMatrix(xs[i], ys[i])
end_time = time.time()
vandermond_time = (end_time - start_time)/n_lists

# Calculate the time for Lagrange:
start_time = time.time()
for i in range(n_lists):
    LagrangeInterpolater(xs[i], ys[i])
end_time = time.time()
lagrange_time = (end_time - start_time)/n_lists

# Measure execution times
print('Vandermond:', vandermond_time)
print('Lagrange:', lagrange_time)