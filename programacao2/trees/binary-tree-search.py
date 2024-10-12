from collections import deque

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class BinaryTree(): 
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        
        while True:
            next = None
            
            if val == current.val:
                continue
            
            if val < current.val:
                next = current.left   
                if next is None:
                    current.left = Node(val)
                    break
            else:
                next = current.right
                if next is None:
                    current.right = Node(val)
                    break
            
            current = next
    
    def __init__(self, nums: list):
        self.root = None
        for n in nums:
            self.insert(n)
                   
    def bfs(self):
        queue = deque([self.root])
        while len(queue) != 0:
            current = queue.popleft()
            print(current.val, end=' ')
            
            if current.left is not None:
                queue.append(current.left)
            
            if current.right is not None:
                queue.append(current.right)
            
    def dfs(self):
        stack = [self.root]
        visited = {}
        while len(stack) != 0:
            current = stack[-1] 
            if (current.left is None) or (current.left.val in visited):
                visited[current.val] = True
                print(current.val, end=' ')
                stack = stack[:-1]
                
                if (current.right is None) or (current.right.val in visited):
                    continue
                stack.append(current.right)
            else:
                stack.append(current.left)

tree = BinaryTree([128, 64, 256, 32, 96, 512, 80, 112, 384])
tree.dfs()
print()
tree.bfs()


                
        
        
            
            