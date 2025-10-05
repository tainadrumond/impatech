import numpy as np
from numpy.typing import NDArray
from typing import Tuple, List
from simplex_phase2 import phase_two_simplex  # seu método Phase 2

def phase_one_simplex(
    A: NDArray[np.float64],
    b: NDArray[np.float64],
    tol: float = 1e-8
) -> Tuple[NDArray[np.float64], NDArray[np.float64], List[int]]:
    """
    Phase One of the Simplex Method to find an initial basic feasible solution.
    Assumes the problem is already in Standard Equality Form (SEF).
    Parameters:
        A : 2D array (m x n)
            Coefficient matrix of the constraints.
        b : 1D array (m)
            Right-hand side vector of the constraints.
        tol : float
            Tolerance for detecting zero.
    Returns:
        A_new : 2D array
            Updated coefficient matrix with artificial variables removed.
        b : 1D array
            Right-hand side vector (unchanged).
        B : list[int]
            Indices of the basis columns in the updated matrix.
    """

    m, n = A.shape
    artificial_vars = []

    # Step 1: Add artifiacial variables to each constraint
    for i in range(m):
        col = np.zeros((m, 1))
        col[i, 0] = 1.0
        A = np.hstack((A, col))
        artificial_vars.append(n + i)

    # Step 2: Objective function for Phase 1 to minimize sum of artificial variables
    c_aux = np.zeros(A.shape[1])
    for var in artificial_vars:
        c_aux[var] = 1.0
    z_aux = 0.0

    # Step 3: Initialize basis with artificial variables
    B_aux = artificial_vars.copy()

    # Step 4: Solve the auxiliary problem using Phase 2 Simplex
    x_aux, opt_value = phase_two_simplex(
        type="min",
        B=B_aux,
        A=A,
        b=b,
        c=c_aux,
        z=z_aux,
        restriction_types=['='] * m,
        non_negative_variables=[True] * A.shape[1]
    )

    # Step 5: Check if is unfeasible
    if opt_value is None or opt_value > tol:
        raise ValueError("No feasible solution found; the original problem may be infeasible.")

    # Step 6: Remove artificial variables
    A_new = np.delete(A, artificial_vars, axis=1)

    # Remove artificial variables from basis
    B_new = []
    for idx in B_aux:
        if idx not in artificial_vars:
            B_new.append(idx)
            
    # If the basis is not complete, add other variables to complete it
    remaining = [i for i in range(A_new.shape[1]) if i not in B_new]
    while len(B_new) < m:
        for i in remaining:
            trial_B = B_new + [i]
            if np.linalg.matrix_rank(A_new[:, trial_B], tol=tol) == len(trial_B):
                B_new.append(i)
                remaining.remove(i)
                break

    return A_new, b, B_new
