from canonical_form import to_canonical_form
from simplex import solve_lp
import numpy as np

# unfeasible example
# A = np.array([[4, 10, -6, -2], [-2, 2, -4, 1], [-7, -2, 0, 4]])
# b = np.array([6, 5, 3])
# z = 0  # termo constante do objetivo
# c = np.array([0, 0, 0, 0], dtype=np.float64)

# solve_lp("max", A, b, c, np.array([z], dtype=np.float64), ["=", "=", "="], [True, True, True, True, True])

# unbounded example
A = np.array([[1, 1, -3, 1, 2], [0, 1, -2, 2, -2], [-2, -1, 4, 1, 0]])
b = np.array([7, -2, -3])
c = np.array([-1, 0, 3, 7, -1])
z = 0  # termo constante do objetivo

# c = np.array([0.14, 0.12, 0.2, 0.75, 0.15])  # Minimizar o preço dos alimentos

# A = np.array(
#     [
#         [23, 171, 65, 112, 188],  # Calorias por porção
#         [0.1, 0.2, 0, 9.3, 16],  # Gordura por porção
#         [0.6, 3.7, 2.2, 7, 7.7],  # Proteina por porção
#         [6, 30, 13, 0, 2],  # Carboidrato por porção
#     ]
# )

# b = np.array([2000, 50, 100, 250])

# Definição para o solucionar com o SIMPLEX próprio

# Problema (a) - Minimizar soma total de salários

# Variáveis: x0 = Raw carrots, x1 = Baked potatoes, x2 = Wheat, x3 = Bread, x4 = Cheddar cheese, x5 = Peanut butter

# Vetor de custos (preço por porção)
c = np.array([0.14, 0.12, 0.2, 0.75, 0.15])

# Matriz A das restrições (cada linha é uma restrição nutricional)
A = np.array([
    [23, 171, 65, 112, 188],   # Calorias por porção
    [0.1, 0.2, 0, 9.3, 16],    # Gordura por porção
    [0.6, 3.7, 2.2, 7, 7.7],   # Proteína por porção
    [6, 30, 13, 0, 2]          # Carboidrato por porção
])

# Vetor b do lado direito (mínimos diários)
b = np.array([2000, 50, 100, 250])

# Todas as restrições são do tipo >=
restriction_types = ['>=', '>=', '>=', '>=']

# Todas as variáveis são não-negativas (não pode comprar porções negativas)
non_negative_variables = [True, True, True, True, True]


c = np.array([1, 1, 1, 1, 1, 1])  # Queremos calcular o minimo dos salários somados

A = np.array(
    [
        [-1, 1, 0, 0, 0, 0],  # Peter - Tom
        [-1, 0, 0, 1, 0, 0],  # Nina - Tom
        [-1, 0, 1, 0, 0, 0],  # Samir - Tom
        [-1, -1, 0, 0, 1, 0],  # Gary - (Tom + Peter)
        [0, 0, 0, 0, -1, 1],  # Linda - Gary
    ]
)

restriction_types = [">=", ">=", ">=", ">=", ">="]

b = np.array([5000, 5000, 5000, 0, 200])

# Chame seu resolvedor
x, opt = solve_lp("min", A, b, c, 0, restriction_types)
print("Porções ótimas:", x)
print("Custo mínimo:", opt)
