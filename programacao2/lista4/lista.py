# EXERCÍCIO 1
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
def get_balanced_tree_height(root: TreeNode):
    '''
    Calcula, recursivamente, a altura da árvora balanceada cuja raiz é dada como parâmetro
    e retorna -1 caso a árvore não seja balanceada.
    
    Parameters:
        root (TreeNode): A raiz da árvore
    
    Returns:
        height (int): Se a árvore for balanceada, retorna sua altura. Caso contrário, retorna -1 
    '''
    if root is None:
        return 0
    left_height = get_balanced_tree_height(root.left)
    
    if left_height == -1:
        return -1
    
    right_height = get_balanced_tree_height(root.right)
    
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    
    return max(left_height, right_height) + 1

def is_balanced_tree(root: TreeNode):
    return get_balanced_tree_height(root) != -1


# EXERCÍCIO 2
import random
class my_stack:
    def __init__(self, items=[]):
        self.items: list = items
    
    def pop(self):
        if len(self.items) == 0: # Tratamento para o caso da lista ser vazia
            return None
        
        random_index = random.randint(0, len(self.items)-1) # Sorteia um número aleatório no range do tamanho da lista
        if random_index == len(self.items)-1: # Tratamento para o caso do número sorteado ser o último item
            return self.items.pop() # Remove o último item
        
        removed_item = self.items[random_index] # Remove e salva o item do índice aleatório
        last_item = self.items.pop() # Remove o último item
        self.items[random_index] = last_item # Coloca o último item na posição do item removido
        return removed_item
        
    def push(self, item):
        self.items.append(item)
        
import time
def test_my_stack():
    # Caso 1: Testando a inicialização e push
    pilha = my_stack()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    assert pilha.items == [1, 2, 3], "Erro no teste: pilha não está correta após pushes."

    # Caso 2: Testando pop
    removed_item = pilha.pop()
    assert removed_item in [1, 2, 3], "Erro no teste: item removido não está na pilha inicial."
    assert len(pilha.items) == 2, "Erro no teste: tamanho da pilha deve ser 2 após um pop."

    # Caso 3: Testando pop até esvaziar a pilha
    removed_item = pilha.pop()
    assert removed_item not in pilha.items, "Erro no teste: item removido está na pilha após pop."
    assert len(pilha.items) == 1, "Erro no teste: tamanho da pilha deve ser 1 após um pop."

    removed_item = pilha.pop()
    assert removed_item == 1 or removed_item == 2 or removed_item == 3, "Erro no teste: último item removido não é esperado."
    assert len(pilha.items) == 0, "Erro no teste: pilha deve estar vazia após remover todos os itens."

    # Caso 4: Testando pop em pilha vazia
    assert pilha.pop() is None, "Erro no teste: pop em pilha vazia deve retornar None."

    # Caso 5: Testando push em pilha vazia
    pilha.push(4)
    assert pilha.items == [4], "Erro no teste: pilha deve conter o item 4 após push."
    
    # Função para medir o tempo da operação pop()
    def measure_pop_time(stack, num_operations):
        start_time = time.time()
        for _ in range(num_operations):
            stack.pop()
        end_time = time.time()
        return (end_time - start_time) / num_operations

    # Testando com diferentes tamanhos de listas
    list_sizes = [10**i for i in range(1, 7)]  # Tamanhos de lista variando de 10 a 10^6
    pop_times = []

    for size in list_sizes:
        # Criar uma pilha com números inteiros de 0 até size-1
        stack = my_stack(list(range(size)))
        
        # Medir o tempo médio da operação pop
        pop_time = measure_pop_time(stack, 1000)  # Testar 1000 operações pop
        pop_times.append(pop_time)
        print(f"Tamanho da lista: {size}, Tempo médio por pop: {pop_time:.6f} segundos")
    
test_my_stack()    


# EXERCÍCIO 3
# (a)
# Eu criaria uma classe com dois atributos: um com o valor do nó e outro com
# uma lista com os nós filhos .
# (b) 
# A adição de novos filhos a um nó pode ser feita através de um append no
# atributo da lista de nós filhos.
# (c)
# Eu percorreria a árvore em profundidade recursivamente, adicionando chamadas
# para cada um dos nós filhos. O código seria similar a:
# def profundidade(node):
#   if node is None:
#       return
#   print(node.val)
#   if node.children is None:
#       return
#   for child in node.children:
#       profundidade(child)
#
# Para percorrer em largura, eu utilizaria uma fila na qual adicionaria os
# nós filhos na medida que fosse percorrendo. O código seria similar a:
# from collections import deque
# def largura(root):
#   if root is None:
#       return
#   queue = deque([root])
#   while len(queue) != 0:
#       current = queue.popleft()
#       if current is None:
#           continue
#       print(current.val)
#       if current.children is not None:
#           queue.extend(current.children) # Adiciona todos os filhos na fila
          

# EXERCÍCIO 4
import scipy.stats as stats
import numpy as np
def sortear_pontos(N, x_dist, y_dist, df=5):
    coords = []
    dists = [x_dist, y_dist]
    for dist in dists:
        if dist == 'uniform':
            coord = stats.uniform.rvs(-1, 2, N)
        elif dist == 'normal':
            coord = stats.norm.rvs(0, 0.5, N)
        elif dist == 'student':
            coord = stats.t.rvs(df, 0, 0.5, N)
        else:
            return None
        coords.append(coord)
    return np.column_stack((coords[0], coords[1]))

# EXERCÍCIO 5
from scipy.spatial import ConvexHull
def calculate_convex_hull(points):
    vertices = ConvexHull(points).vertices
    return points[vertices]