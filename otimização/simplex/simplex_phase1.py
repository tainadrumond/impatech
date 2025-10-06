import numpy as np
from numpy.typing import NDArray

def phase_one_simplex(A: NDArray[np.float64], b: NDArray[np.float64]):
    """
    Simplex Phase I: finds an initial feasible basis for Ax = b, x >= 0.

    Returns:
        feasible_basis : list[int] or None if the LP is infeasible.
    """
    m, n = A.shape

    # Add artificial variables to each constraint
    I_art = np.eye(m)
    A1 = np.hstack((A, I_art))
    c1 = np.zeros(n + m)
    c1[n:] = 1.0  # Minimize the sum of artificial variables

    # Initial basis: artificial variables
    B = list(range(n, n + m))
    N = [j for j in range(n)]

    max_iter = 1000
    for _ in range(max_iter):
        # Step 1: Compute inverse of the current basis matrix
        A_B = A1[:, B]
        try:
            A_B_inv = np.linalg.inv(A_B)
        except np.linalg.LinAlgError:
            return None

        # Basic feasible solution
        x_B = A_B_inv @ b

        # Step 2: Compute reduced costs
        c_B = c1[B]
        c_N = c1[N]
        y = c_B @ A_B_inv
        reduced_costs = c_N - y @ A1[:, N]

        # Step 3: Check optimality (all reduced costs ≥ 0 → optimum)
        if np.all(reduced_costs >= -1e-10):
            # Verify if artificial variables remaining in basis are zero
            for i, j in enumerate(B):
                if j >= n and abs(x_B[i]) > 1e-10:
                    return None  # infeasible
            break

        # Step 4: Choose entering variable (most negative reduced cost)
        enter_idx = np.argmin(reduced_costs)
        entering = N[enter_idx]

        # Step 5: Compute direction vector
        direction = A_B_inv @ A1[:, entering]
        if np.all(direction <= 1e-10):
            return None  # unbounded (should not occur in Phase I)

        # Step 6: Minimum ratio test
        ratios = [(x_B[i] / direction[i], i) for i in range(m) if direction[i] > 1e-10]
        if not ratios:
            return None
        _, leave_pos = min(ratios, key=lambda x: (x[0], x[1]))
        leaving = B[leave_pos]

        # Step 7: Update basis and non-basis sets
        B[leave_pos] = entering
        N[enter_idx] = leaving
        B.sort()
        N.sort()

    # Step 8: Extract feasible basis for the original problem
    feasible_B = [j for j in B if j < n]

    # Step 9: Complete the basis if necessary
    if len(feasible_B) < m:
        for j in range(n):
            if j not in feasible_B:
                trial_basis = feasible_B + [j]
                if np.linalg.matrix_rank(A[:, trial_basis]) == len(trial_basis):
                    feasible_B = trial_basis
                    if len(feasible_B) == m:
                        break

    return feasible_B if len(feasible_B) == m else None
