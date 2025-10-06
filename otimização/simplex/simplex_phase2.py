import numpy as np
from numpy.typing import NDArray
from typing import Literal
from standard_equality_form import to_standard_equality_form
from canonical_form import to_canonical_form

def phase_two_simplex(
    type: Literal["min", "max"],
    B: list[int], 
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
    B: list of int, optional
        List of indices representing the basic variables.
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
    
    m, n = A.shape
    N = [j for j in range(n) if j not in B]
    
    while True:        
        # Step 1: Convert to canonical form
        A, x, b, c, z = to_canonical_form(B, N, A, b, c, z)
        
        # Step 2: Reached optimal solution
        if c[N].max() <= 0:
            opt_value = z + c @ x
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
