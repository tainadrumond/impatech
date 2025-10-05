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

solve_lp("max", A, b, c, np.array([z], dtype=np.float64), ["=", "=", "="], [True, True, True, True, True])
