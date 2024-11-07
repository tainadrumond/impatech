# EXERCÍCIO 1
# A função acha o ponto do array que tem a menor distância para o ponto
# dado como parâmetro.
# Vamos analisar a complexidade de cada passo, considerando que as dimensões
# dos pontos são fixas:
# Passo 1: subtrai o ponto dado de cada um dos pontos do array.
# A complexidade é O(n).
# Passo 2: calcula a norma de cada um dos vetores resultantes da
# operação anterior. A complexidade é O(n).
# Passo 3: acha a menor das normas calculadas anteriormente. Como,
# no pior caso, todas as normas são checadas, a complexidade é O(n).
# Passo 4: retorna a menor distância e o índice do ponto correspondente
# a ela. A complexidade é O(1)
# Complexidade final: O(n)


# EXERCÍCIO 2
import random

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))
        
def generate_maze(m, n, room = 0, wall = 1, cheese = '.'):
    # Initialize a (2m + 1) x (2n + 1) matrix with all walls (1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Directions: (row_offset, col_offset) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs_itrv():
        """Iterative DFS to generate the maze."""
        
        # Initializes the stack that saves the previous cell visited and the next direction to visit
        stack = [{'prev': (0, 0), 'dir': (0, 0)}]
        
        while len(stack) != 0:
            el = stack.pop() # Element from the stack
            px, py = el['prev'] # Previous cell coordinates
            dx, dy = el['dir'] # Next direction
            x, y = px + dx, py + dy  # New cell coordinates
            
            if not(0 <= x < m and 0 <= y < n and maze[2 * x + 1][2 * y + 1] == wall):
                continue
            
            # Opens the wall between the previous cell and the new cell
            maze[2 * px + 1 + dx][2 * py + 1 + dy] = room
            # Marks the current cell as visited by making it a path (room)
            maze[2 * x + 1][2 * y + 1] = room
            
            random.shuffle(directions)
            
            for dx, dy in directions:
                # Adds the next cell to be visited in the stack
                stack.append({'prev': (x, y), 'dir': (dx, dy)})

    # Starts the iterative DFS
    dfs_itrv()
    count = 0
    while True: # placing the chesse
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        count += 1
        if maze[i][j] == room:
            maze[i][j] = cheese 
            break

    return maze

room, wall, cheese = ' ', 'H', '@'
maze = generate_maze(6, 6, room, wall, cheese)
print_maze(maze)
print()

# EXERCÍCIO 3
# DISCUSSÃO:
# Utilizei a busca em profundidade para encontrar um caminho até o queijo no labirinto.
# A busca em profundidade foi escolhida por ser similar ao algoritmo que gera o labirinto.
# Além disso, é eficiente para encontrar um caminho válido sem explorar todas as 
# alternativas e permite construir o caminho final facilmente.

from copy import deepcopy

def find_cheese(maze, wall, cheese):
    '''
    Recursively finds the cheese in the given maze.
    '''
    m = len(maze) # Height of the maze
    n = len(maze[0]) # Width of the maze
    visited = [[False] * (2 * n + 1) for _ in range(2 * m + 1)] # Matrix to save the cells that have been visited
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path = [] # List that keeps the path traveled to the cheese
    
    def dfs(cell_coordinates):
        '''
        Recursive depth first search that returns true if the current cell is in
        the path to the cheese.
        '''
        x, y = cell_coordinates
        visited[x][y] = True # Sets the current cell as visited
        
        if maze[x][y] == cheese:
            return True
        
        # Iterates through every direction
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # New cell coordinates
            # Checks if the new cell is valid and has not been visited yet
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != wall and not visited[nx][ny]:
                if dfs((nx, ny)):
                    # If one of the following cells is in the path to the cheese, then the current cell is also in the path to the cheese.
                    path.append((x, y))
                    return True
        
        # Returns false in case none of its following cells is in the path to the cheese
        return False
    
    # Starts the search for the cheese from the (1, 1) cell
    dfs((1, 1))
    return path

def print_path(maze, path, path_cell = '.'):
    '''
    Prints the given path in the maze
    '''
    path_maze = deepcopy(maze)
    for x, y in path:
        path_maze[x][y] = path_cell
    print_maze(path_maze)
    
path = find_cheese(maze, wall, cheese)
print_path(maze, path)


# EXERCÍCIO 4
class Vertex:
    def __init__(self, value = None):
        self.value = value
        
    def set_value(self, value):
        self.value = value

class Graph:
    def __init__(self, adj: dict[set[Vertex]] = {}):
        self.adj = adj
    
    def adjacent(self, x, y):
        if x in self.adj:
            return y in self.adj[x]
        return False
    
    def neighbors(self, x):
        if x in self.adj:
            return list(self.adj[x])
        return None
    
    def add_vertex(self, x):
        if x in self.adj:
            return False
        self.adj[x] = set()
        return True
        
    def remove_vertex(self, x):
        if x not in self.adj:
            return False
        for vertex, neighbors in self.adj.items():
            if x in neighbors:
                self.adj[vertex].remove(x)
        self.adj.pop(x)
        return True
    
    def add_edge(self, x, y):
        if x not in self.adj or y in self.adj[x]:
            return False
        self.adj[x].add(y)
        return True
    
    def remove_edge(self, x, y):
        if x not in self.adj or y not in self.adj[x]:
            return False
        self.adj[x].remove(y)
        return True
    
    def get_vertex_value(self, x):
        if x not in self.adj:
            return None
        return x.value
    
    def set_vertex_value(self, x, v):
        x.set_value(v)
        
def test_graph():
    # Create vertices
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    # Initialize the graph
    g = Graph()

    # Add and check a single vertex
    assert g.add_vertex(v1) == True, "Error adding v1"
    assert g.neighbors(v1) == [], "v1 should have zero neighbors"

    # Add and check an edge
    g.add_vertex(v2)
    assert g.add_edge(v1, v2) == True, "Error adding edge v1-v2"
    assert g.adjacent(v1, v2) == True, "v1 and v2 should be adjacent"
    
    # Check neighbors after adding an edge
    assert v2 in g.neighbors(v1), "v1 should have v2 as a neighbor"

    # Remove edge and check
    assert g.remove_edge(v1, v2) == True, "Error removing edge v1-v2"
    assert g.adjacent(v1, v2) == False, "v1 and v2 should not be adjacent"

    # Update and check vertex value
    g.set_vertex_value(v1, "X")
    assert g.get_vertex_value(v1) == "X", "Error updating value of v1"

    # Remove vertex and verify removal
    assert g.remove_vertex(v1) == True, "Error removing v1"
    assert g.neighbors(v1) == None, "v1 was removed, so it should have no neighbors"

# Run the tests
test_graph()


            