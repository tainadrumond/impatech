# python 3

import random
from copy import deepcopy

def generate_maze(m, n, room = 0, wall = 1, cheese = '.'):
    # Initialize a (2m + 1) x (2n + 1) matrix with all walls (1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Directions: (row_offset, col_offset) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        """Recursive DFS to generate the maze."""
        # Mark the current cell as visited by making it a path (room)
        maze[2 * x + 1][2 * y + 1] = room

        # Shuffle the directions to create a random path
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # New cell coordinates
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Open the wall between the current cell and the new cell
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                print_maze(maze)
                print()
                # Recursively visit the new cell
                dfs(nx, ny)
    
    def dfs_itrv():
        """Iterative DFS to generate the maze."""
        
        # Initializes the stack that saves the previous cell visited and the next direction to visit
        stack = [{'prev': (0, 0), 'dir': (0, 0)}]
        
        while len(stack) != 0:
            el = stack.pop()
            px, py = el['prev'] # Previous cell coordinates
            dx, dy = el['dir'] # Next direction
            x, y = px + dx, py + dy  # New cell coordinates
            
            if not(0 <= x < m and 0 <= y < n and maze[2 * x + 1][2 * y + 1] == wall):
                continue
            
            # Open the wall between the previous cell and the new cell
            maze[2 * px + 1 + dx][2 * py + 1 + dy] = room
            # Mark the current cell as visited by making it a path (room)
            maze[2 * x + 1][2 * y + 1] = room
            
            random.shuffle(directions)
            
            for dx, dy in directions:
                stack.append({'prev': (x, y), 'dir': (dx, dy)})  # Adds the next cell to be visited in the stack

    # Start DFS from the top-left corner (0, 0) of the logical grid
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

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))
        
def find_cheese(maze, room, wall, cheese):
    m = len(maze)
    n = len(maze[0])
    visited = [[False] * (2 * n + 1) for _ in range(2 * m + 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maze_path = deepcopy(maze)
    
    def dfs(cell_coordinates):
        x, y = cell_coordinates
        visited[x][y] = True
        
        if maze[x][y] == cheese:
            return True
        
        found_cheese = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != wall and not visited[nx][ny]:
                if dfs((nx, ny)):
                    found_cheese = True
        
        if found_cheese == True:
            maze_path[x][y] = '.'
        
        return found_cheese
    
    dfs((1, 1))
    print_maze(maze_path)
    

# Example usage:
if __name__ == '__main__':
    m, n = 5, 7  # Grid size
    random.seed(10110134514351)
    maze = generate_maze(m, n)
    print('Maze 1')
    print_maze(maze)

    room = ' '
    wall = 'H'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze 2')
    print_maze(maze)
    print()
    find_cheese(maze, room, wall, cheese)