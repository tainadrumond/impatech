from standard_equality_form import to_standard_equality_form
import numpy as np

def test_to_standard_equality_form1():
    A = np.array([
        [1, 2, 4, 7, 3],
        [2, 8, 9, 0, 0],
        [1, 1, 0, 2, 6],
        [-3, 4, 3, 1, -1]
    ], dtype=np.float64)
    b = np.array([1, 2, 3, 4], dtype=np.float64)
    c = np.array([2, -1, 4, 2, 4], dtype=np.float64)
    restriction_types = ["<=", "=", ">=", ">="]
    non_negative_variables = [True, True, False, True, False]

    A_sef, b_sef, c_sef = to_standard_equality_form("min", A, b, c, restriction_types, non_negative_variables)

    expected_A_sef = np.array([
        [1, 2, 4, -4, 7, 3, -3, 1, 0, 0],
        [2, 8, 9, -9, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 2, 6, -6, 0, -1, 0],
        [-3, 4, 3, -3, 1, -1, 1, 0, 0, -1]
    ], dtype=np.float64)

    expected_b_sef = np.array([1, 2, 3, 4], dtype=np.float64)

    expected_c_sef = np.array([-2, 1, -4, 4, -2, -4, 4, 0, 0, 0], dtype=np.float64)

    assert np.array_equal(A_sef, expected_A_sef), f"A_sef does not match expected.\n Got \n {A_sef} \n Expected \n {expected_A_sef}"
    assert np.array_equal(b_sef, expected_b_sef), f"b_sef does not match expected.\n Got \n {b_sef} \n Expected \n {expected_b_sef}"
    assert np.array_equal(c_sef, expected_c_sef), f"c_sef does not match expected.\n Got \n {c_sef} \n Expected \n {expected_c_sef}"
    
    print("All tests passed!")

test_to_standard_equality_form1()