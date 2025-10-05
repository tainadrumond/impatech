import numpy as np
from numpy.typing import NDArray
from typing import Literal
from simplex_phase1 import phase_one_simplex
from simplex_phase2 import phase_two_simplex

def solve_lp(
    type: Literal["min", "max"],
    A: NDArray[np.float64], 
    b: NDArray[np.float64], 
    c: NDArray[np.float64],
    z: np.float64, 
    restriction_types: list[str], 
    non_negative_variables: list[bool] = []
) -> tuple[NDArray[np.float64], float]:
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
        A tuple containing:
        - x : 1D array
            Solution vector.
        - opt_value : float
            Optimal value of the objective function.
    '''
    try: 
        # Step 0: Phase 1 - find a basic feasible solution
        A, b, B = phase_one_simplex(A, b)
        
        # Step 1: Phase 2 - solve the original problem starting from the basic feasible solution found in Phase 1
        return phase_two_simplex(type, B, A, b, c, z, restriction_types, non_negative_variables)
    
    except ValueError as e:
        print(e)
        return None, None