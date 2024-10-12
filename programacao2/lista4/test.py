import unittest
import numpy as np
from lista import get_balanced_tree_height, TreeNode, sortear_pontos

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_get_balanced_tree_height():
    # Caso 1: Árvore vazia
    root = None
    assert get_balanced_tree_height(root) == 0, "Erro no teste: árvore vazia"

    # Caso 2: Árvore com um único nó (balanceada)
    root = TreeNode(1)
    assert get_balanced_tree_height(root) == 1, "Erro no teste: árvore com um único nó"

    # Caso 3: Árvore balanceada (2 níveis)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert get_balanced_tree_height(root) == 2, "Erro no teste: árvore balanceada de 2 níveis"

    # Caso 4: Árvore balanceada (3 níveis)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert get_balanced_tree_height(root) == 3, "Erro no teste: árvore balanceada de 3 níveis"

    # Caso 5: Árvore desbalanceada (subárvore esquerda mais profunda)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert get_balanced_tree_height(root) == -1, "Erro no teste: árvore desbalanceada (esquerda profunda)"

    # Caso 6: Árvore desbalanceada (subárvore direita mais profunda)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert get_balanced_tree_height(root) == -1, "Erro no teste: árvore desbalanceada (direita profunda)"
    
    # Caso 7: Árvore completamente cheia (3 níveis)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert get_balanced_tree_height(root) == 3, "Erro no teste: árvore cheia de 3 níveis"

    # Caso 8: Árvore com uma subárvore muito mais profunda (desbalanceada)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    assert get_balanced_tree_height(root) == -1, "Erro no teste: árvore desbalanceada com subárvore esquerda profunda"

    # Caso 9: Árvore balanceada com subárvore direita mais profunda em um nível
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    assert get_balanced_tree_height(root) == 3, "Erro no teste: árvore balanceada com subárvore direita mais profunda"

    # Caso 10: Árvore com subárvore esquerda mais profunda em um nível
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    assert get_balanced_tree_height(root) == 3, "Erro no teste: árvore balanceada com subárvore esquerda mais profunda"

    # Caso 11: Árvore desbalanceada com diferença de altura exata de 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right = TreeNode(5)
    assert get_balanced_tree_height(root) == -1, "Erro no teste: árvore desbalanceada com diferença de altura igual a 2"

    # Caso 12: Árvore com apenas um lado completo (direita vazia)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    assert get_balanced_tree_height(root) == -1, "Erro no teste: árvore com lado direito vazio"

    # Caso 13: Árvore com profundidade mínima (um nó por nível à esquerda)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert get_balanced_tree_height(root) == -1, "Erro no teste: árvore com profundidade mínima (lado esquerdo único)"

    # Caso 14: Árvore balanceada com subárvores de altura igual
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert get_balanced_tree_height(root) == 3, "Erro no teste: árvore balanceada com subárvores de altura igual"

    # Caso 15: Árvore com raiz sem filhos (apenas um nó)
    root = TreeNode(1)
    assert get_balanced_tree_height(root) == 1, "Erro no teste: árvore com um único nó"

    print("Todos os testes passaram!")

# Execute os testes
test_get_balanced_tree_height()

def testar_sortear_pontos():
    # Caso 1: Testar a distribuição uniforme
    pontos_uniforme = sortear_pontos(100, 'uniform', 'uniform')
    assert pontos_uniforme.shape == (100, 2), "Erro: Deve retornar um array com 100 pontos."
    assert np.all((-1 <= pontos_uniforme[:, 0]) & (pontos_uniforme[:, 0] <= 1)), "Erro: Coordenadas x fora do intervalo."
    assert np.all((-1 <= pontos_uniforme[:, 1]) & (pontos_uniforme[:, 1] <= 1)), "Erro: Coordenadas y fora do intervalo."
    
    # Caso 2: Testar a distribuição normal
    pontos_normal = sortear_pontos(100, 'normal', 'normal')
    assert pontos_normal.shape == (100, 2), "Erro: Deve retornar um array com 100 pontos."
    assert np.all(np.isclose(np.mean(pontos_normal[:, 0]), 0, atol=0.1)), "Erro: Média x fora do esperado."
    assert np.all(np.isclose(np.std(pontos_normal[:, 0]), 0.5, atol=0.1)), "Erro: Desvio padrão x fora do esperado."
    
    # Caso 3: Testar a distribuição t de Student
    pontos_student = sortear_pontos(100, 'student', 'student')
    assert pontos_student.shape == (100, 2), "Erro: Deve retornar um array com 100 pontos."
    assert np.all(np.isclose(np.mean(pontos_student[:, 0]), 0, atol=0.1)), "Erro: Média x fora do esperado."
    assert np.all(np.isclose(np.std(pontos_student[:, 0]), 0.5, atol=0.1)), "Erro: Desvio padrão x fora do esperado."
    
    # Caso 4: Testar entradas inválidas
    resultado_invalido = sortear_pontos(100, 'invalid', 'uniform')
    assert resultado_invalido is None, "Erro: Deveria retornar None para distribuição inválida."
    
    # Caso 5: Testar N igual a 0
    pontos_zero = sortear_pontos(0, 'normal', 'normal')
    assert pontos_zero.shape == (0, 2), "Erro: Deve retornar um array vazio quando N=0."
    
    print("Todos os testes passaram!")

# Executando os testes
# testar_sortear_pontos()