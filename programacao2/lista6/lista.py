# CLASSES AUXILIARES UTILIZADAS
class Vertex:
    def __init__(self, value: object = None):
        self.value = value
        
    def set_value(self, value):
        self.value = value

class Graph:
    def __init__(self, adj: dict[Vertex, set[Vertex]] = {}):
        self.adj = adj
    
    def adjacent(self, x, y):
        if x in self.adj:
            return y in self.adj[x]
        return False
    
    def neighbors(self, x) -> list[Vertex]:
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
    
    def get_vertices(self) -> set[Vertex]:
        vertices = set()
        for vertex in self.adj.keys():
            vertices.add(vertex)
            vertices.update(self.adj[vertex])
        return vertices
    
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


# EXERCÍCIO 1
# Para esse exercício, considerei as classes Vertex e Graph implementadas
# na lista 5.
from collections import deque
def bfs(graph: Graph, initial_vertex: Vertex) -> list[Vertex]:
    '''
    Breadth-first search that travels through the graph's component
    that contains the initial_vertex.
    '''
    # Queue of vertices to be visited (FIFO)
    queue = deque([initial_vertex])
    
    # Vertices that have already been visited
    visited = set([initial_vertex])
    
    # Visited vertices sorted by the order they were visited
    result: list[Vertex] = [] 
    
    while len(queue) != 0:
        current_vertex = queue.popleft()
        result.append(current_vertex)
        
        for neighbour in graph.neighbors(current_vertex):
            if neighbour not in visited:
                queue.append(neighbour) # Add the vertex in the queue to be explored
                visited.add(neighbour) # Mark the current vertex as visited
                
    return result


# EXERCÍCIO 2
# Para esse exercício, considerei as classes Vertex e Graph implementadas
# na lista 5.
def busca_propriedade(graph: Graph, value: object) -> Vertex | None:
    '''
    Breadth-first search that returns the first visited vertex of the 
    graph whose value attribute is equal to the given value parameter.
    '''
    # Save the vertices that have not been visited yet. Initially, it contains all vertices of the graph
    not_visited = graph.get_vertices() 
    
    # Every iteration of the following while travels through a connected component of the graph
    while len(not_visited) != 0:
        # Define an arbitrary vertex of the connected component to be the initial vertex
        initial_vertex = next(iter(not_visited)) 
        
        if initial_vertex.value == value:
            return initial_vertex
        
        not_visited.remove(initial_vertex) # Mark the vertex as visited
        queue = deque([initial_vertex])
        
        # Travel through the whole connected component
        while len(queue) != 0:
            current_vertex = queue.popleft()    
            
            for neighbour in graph.neighbors(current_vertex):
                if neighbour in not_visited:
                    if neighbour.value == value:
                        return neighbour
                    queue.append(neighbour) # Add the vertex in the queue to be explored
                    not_visited.remove(neighbour) # Mark the current vertex as visited
    
    return None


# EXERCÍCIO 3
def count_islands(map: list[list[str]]) -> int:
    lines = len(map)
    columns = len(map[0])
    
    # Matrix to save the coordinates that have already been visited
    visited = [[False for _ in range(columns)] for _ in range(lines)]
    
    # Directions: (row_offset, col_offset) for N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    islands = 0
    
    for i in range(lines):
        # Iterate through every coordinate of the map. If the current coordinate has already
        # been visited or is water, then it continues to the next iteration.
        for j in range(columns):
            if visited[i][j]:
                continue
            
            visited[i][j] = True
            if map[i][j] == '0':
                continue
            
            # Queue of the neighbour lands to be visited
            queue = deque([(i, j)])
            while len(queue) != 0:
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    # Coordinates of the next neighbour land
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < lines and 0 <= ny < columns: # Check if they are valid coordinates
                        if not visited[nx][ny] and map[nx][ny] == '1': # Check it is a land and has not been visited yet
                            queue.append((nx, ny)) # Add the land in the queue of neighbours to be explored
                        visited[nx][ny] = True # Mark the current coordinate as visited
                        
            # By the end of the while above, another island was completely explored
            islands += 1
    
    return islands

def read_map_and_count_islands(path = 'lista6/new_map.txt'):
    map = []
    with open(path, 'r') as file:
        for line in file:
            map.append(list(line.strip()))
    return count_islands(map)

print(read_map_and_count_islands())

# EXERCÍCIO 4
import math
def find_largest_and_smallest_islands_centroids(map: list[list[str]]):
    '''
    Find the largest and smallest islands and their centroids coordinates.
    '''
    
    # Function with BFS similar to count_islands
    def get_largest_and_smallest_islands(map):
        '''
        Breadth-first search that returns the elements of the largest 
        and smallest islands.
        '''
        lines = len(map)
        columns = len(map[0])
        
        # Matrix to save the coordinates that have already been visited
        visited = [[False for _ in range(columns)] for _ in range(lines)]
        
        # Directions: (row_offset, col_offset) for N, NE, E, SE, S, SW, W, NW
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        largest_size = 0 # Largest island size
        smallest_size = math.inf # Smallest island size
         
        largest = [] # Coordinates of the lands that are in the largest island
        smallest = [] # Coordinates of the lands that are in the smallest island
        
        for i in range(lines):
            for j in range(columns):
                if visited[i][j]:
                    continue
                
                visited[i][j] = True
                if map[i][j] == '0':
                    continue
                
                # Coordinates of the lands of the current islands
                current_island = []
                queue = deque([(i, j)])
                while len(queue) != 0:
                    x, y = queue.popleft()
                    current_island.append((x, y))
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < lines and 0 <= ny < columns:
                            if not visited[nx][ny] and map[nx][ny] == '1':
                                queue.append((nx, ny))
                            visited[nx][ny] = True
                
                # If the current island is larger than the previous largest 
                # island, then it becomes the largest.
                if len(current_island) > largest_size:
                    largest_size = len(current_island)
                    largest = current_island
                
                # If the current island is smaller than the previous smallest 
                # island, then it becomes the smallest.
                if len(current_island) < smallest_size:
                    smallest_size = len(current_island)
                    smallest = current_island
        
        return (largest, smallest)
    
    def calculate_centroid(points: list[tuple[int,int]]):
        '''
        Calculate the centroid coordinate of the given points.
        '''
        size = len(points)
        if size == 0:
            return (0, 0)
        x_sum = 0
        y_sum = 0
        for x, y in points:
            x_sum += x
            y_sum += y
        
        return (x_sum/size, y_sum/size)
    
    largest, smallest = get_largest_and_smallest_islands(map)
    largest_centroid, smallest_centroid = calculate_centroid(largest), calculate_centroid(smallest)
    return (largest_centroid, smallest_centroid)
    

# EXERCÍCIO 5
def is_there_a_lake(map: list[list[str]]) -> int:
    '''
    Breadth-first search to check if there is a lake (a portion of 
    water surrounded by lands in N, E, S, W) in the given map.
    '''
    lines = len(map)
    columns = len(map[0])
    
    # Matrix to save the coordinates that have already been visited
    visited = [[False for _ in range(columns)] for _ in range(lines)]
    
    # Directions: (row_offset, col_offset) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(1, lines-1):
        # Iterate through every coordinate of the map. If the current coordinate has 
        # already been visited or is a land, then it continues to the next iteration.
        for j in range(1, columns-1):
            if visited[i][j]:
                continue
            
            visited[i][j] = True
            if map[i][j] == '1':
                continue
            
            has_lake = True
            # Queue of connected water coordinates
            queue = deque([(i, j)])
            while len(queue) != 0:
                x, y = queue.popleft()
                
                # If one of the neighbour coordinates is in the border of the map, then it is
                # not surrounded by lands. Therefore, the current component is not a lake.
                if x == 0 or x == lines-1 or y == 0 or y == columns-1:
                    has_lake = False
                    break
                
                for dx, dy in directions:
                    # Coordinates of the next neighbour water
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < lines and 0 <= ny < columns: # Check if they are valid coordinates
                        if not visited[nx][ny] and map[nx][ny] == '0': # Check it is water and has not been visited yet
                            queue.append((nx, ny)) # Add in the queue of neighbours to be explored
                        visited[nx][ny] = True # Mark the current coordinate as visited
            
            # If the has_lake boolean remains True after the while iteration, then none of the water elements is in
            # the border of the map. Therefore, it is surrounded by lands
            if has_lake == True:
                return True
    
    return False
