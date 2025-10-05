import numpy as np
from numpy.typing import NDArray
from scipy.linalg import lu

def to_canonical_form(
    B: list[int],
    N: list[int],
    A: NDArray[np.float64], 
    b: NDArray[np.float64], 
    c: NDArray[np.float64], 
    z: np.float64
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Converts a linear programming problem to an equivalent problem in canonical form.
    Parameters:
    B: list of int
        List of indices representing the basic variables.
    N: list of int
        List of indices representing the non-basic variables.
    A : 2D array
        Coefficient matrix of the constraints.
    b : 1D array
        Right-hand side vector of the constraints.
    c : 1D array
        Coefficient vector of the objective function.
    restriction_types : list of str
        List indicating the type of each constraint ('<=', '>=', '=').
    non_negative_variables : list of bool, optional
        List indicating whether each variable is non-negative. If empty, all variables are assumed to be non-negative.
    """
    m, n = A.shape

    # Extract the submatrix corresponding to the chosen columns
    Ab = A[:, B]
    
    Ab_inv = np.linalg.inv(Ab)
    A_canon = Ab_inv @ A
    b_canon = Ab_inv @ b # b_canon is the solution for the basic variables
    
    if np.all(b_canon >= 0):  # Check if the solution is feasible (non-negative)
        # Transform to canonical form
        y = np.linalg.solve(Ab.T, c[list(B)]) # y = (A_b ^T)^-1 * c_b
        z_canon = z + y @ b
        c_canon = c - y @ A
        x_canon = np.zeros(n)
        x_canon[list(B)] = b_canon
        return A_canon, x_canon, b_canon, c_canon, z_canon
            
    raise ValueError("No basic feasible solution found; the problem may be infeasible.")