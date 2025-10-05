import numpy as np
from numpy.typing import NDArray
from typing import Literal

def to_standard_equality_form(
    type: Literal["min", "max"], 
    A: NDArray[np.float64], 
    b: NDArray[np.float64], 
    c: NDArray[np.float64], 
    restriction_types: list[str], 
    non_negative_variables: list[bool] = []
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Converts a linear programming problem to an equivalent problem in standard equality form.
    Parameters:
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
    # Number of constraints and number of variables
    m, n = A.shape

    # Convert minimization to maximization
    if type == "min":
        c = -c
        
    # Impose non-negativity on variables
    count_free = 0
    for (i, non_negative) in enumerate(non_negative_variables):
        if not non_negative:
            curr_i = i + count_free
            # Adjusting the objective function
            c = np.insert(c, curr_i+1, -c[curr_i])
            
            # Adjusting the constraint matrix
            A = np.insert(A, curr_i+1, -A[:, curr_i], axis=1)
            n += 1
            count_free += 1
            
    # Convert inequalities to equalities
    for (i, restriction) in enumerate(restriction_types):
        if restriction == "<=":
            # Add slack variable
            slack = np.zeros((m, 1))
            slack[i, 0] = 1
            A = np.hstack((A, slack))
            c = np.hstack((c, [0]))
            n += 1
        elif restriction == ">=":
            # Add surplus variable
            surplus = np.zeros((m, 1))
            surplus[i, 0] = -1
            A = np.hstack((A, surplus))
            c = np.hstack((c, [0]))
            n += 1
        
    return A, b, c