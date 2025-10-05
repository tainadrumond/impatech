import numpy as np
from numpy.typing import NDArray
from typing import Literal
from standard_equality_form import to_standard_equality_form
from canonical_form import to_canonical_form
from itertools import combinations
from scipy.linalg import lu

def find_basis(A: NDArray[np.float64]) -> list[int]:
    m, n = A.shape

    # Find a basic feasible solution by checking combinations of columns
    for B in combinations(range(n), m):
        N = [j for j in range(n) if j not in B]
        
        # Extract the submatrix corresponding to the chosen columns
        Ab = A[:, B]
        # Perform LU decomposition to check if B is invertible
        P, L, U = lu(Ab)
        if np.all(np.diag(U) != 0):  # Check if Ab is non-singular
            return list(B)
    
    raise ValueError("No basic feasible solution found; the problem may be infeasible.")

def solve_lp(
    type: Literal["min", "max"], 
    A: NDArray[np.float64], 
    b: NDArray[np.float64], 
    c: NDArray[np.float64],
    z: np.float64, 
    restriction_types: list[str], 
    non_negative_variables: list[bool] = []
):
    '''
    Solves a linear programming problem using the Simplex method.
    Parameters:
    type : str
        Type of the problem, either "min" for minimization or "max" for maximization.
    A : 2D array
        Coefficient matrix of the constraints.
    b : 1D array
        Right-hand side vector of the constraints.
    c : 1D array
        Coefficient vector of the objective function.
    z : 1D array
        Constant term in the objective function.
    restriction_types : list of str
        List indicating the type of each constraint ('<=', '>=', '=').
    non_negative_variables : list of bool, optional
        List indicating whether each variable is non-negative. If empty, all variables are assumed to be non-negative.
    Returns:
        A : 2D array
    '''
    try:
        # Step 0: Convert to standard equality form first
        A, b, c = to_standard_equality_form(type, A, b, c, restriction_types, non_negative_variables)
        
        m, n = A.shape
        B = find_basis(A)
        N = [j for j in range(n) if j not in B]
        
        while True:        
            # Step 1: Convert to canonical form
            A, x, b, c, z = to_canonical_form(B, N, A, b, c, z)
            
            # Step 2: Reached optimal solution
            if c[N].max() <= 0:
                print("Optimal solution found.")
                print('Solução ótima: x =', x)
                opt_value = z + c @ x
                print('Valor ótimo da função objetivo: z =', opt_value)
                return x, opt_value
            
            # Step 3: Select k such that c[k] > 0
            k = 0
            for i in N:
                if c[i] > 0:
                    k = i
                    break
            
            # Step 4: If A_k <= then stop (the problem is unbounded)
            if A[:, k].max() <= 0:
                raise ValueError("The problem is unbounded.")
            
            # Step 5: Determine the index r and the value t for the next iteration of the simplex method.
            ratios = []
            for i in range(len(b)):
                if A[i, k] > 0:
                    ratios.append((b[i] / A[i, k], i))
            t, r = min(ratios, key=lambda x: x[0])
            
            # Step 6: Let l be the rth basis element
            l = B[r]
            
            # Step 7: Set B = B \ {l} ∪ {k} and N = N \ {k} ∪ {l}
            B[r] = k
            
            N.remove(k)
            N.append(l)

            # 2.6 Atualiza A, b, c, z (pivot)
            Ab = A[:, B]
            Ab_inv = np.linalg.inv(Ab)
            A = Ab_inv @ A
            b = Ab_inv @ b
            y = np.linalg.solve(Ab.T, c[B])
            z = z + y @ b
            c = c - y @ A
        
    except ValueError as e:
        print(e)
        return None, None
    