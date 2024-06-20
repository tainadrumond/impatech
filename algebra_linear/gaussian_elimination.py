from matrix import Vector, Matrix

MIN_NUMBER = -99999999999999999999 

def build_identity_matrix(n: int) -> Matrix:
    '''
    Returns an identity matrix of size n x n.
    '''
    lines = []
    for i in range(n):
        lines.append([0]*n)
        lines[i][i] = 1
    return Matrix(lines)

def find_first_non_zero_pivot_line_index(A: Matrix, j: int) -> int:
    '''
    Returns the index of the first line with a non zero element at the j-th column.
    If there isn't any, returns -1.
    '''
    for i in range(j, A.number_of_lines):
        if A.at(i, j) != 0:
            return i
    return -1

def gaussian_elimination(A: list) -> dict:
    '''
    Computes the gaussian elimination for matrix A and returns the matrixes P, L and U of PA = LU factorization
    '''
    U = Matrix(A)
    identity = build_identity_matrix(U.number_of_lines)
    P = identity.copy()
    L = identity.copy()
    
    number_of_pivots = min(U.number_of_columns, U.number_of_lines)
    
    for i in range(number_of_pivots):
        if U.at(i, i) == 0: # If the current pivot position has a 0, then the lines are permuted
            first_non_zero_pivot_line_index = find_first_non_zero_pivot_line_index(U, i)
            if first_non_zero_pivot_line_index == -1:
                continue # If there isn't any entry different from 0 for this column, it simply maintains the column of 0s in U
            U.permut(i, first_non_zero_pivot_line_index)
            P.permut(i, first_non_zero_pivot_line_index)
        
        multiplier = U.lines[i].at(i)
        U.change_line(U.lines[i]*(1/multiplier), i)
        L.change_entry(multiplier, i, i)
            
        for k in range(i+1, U.number_of_lines): # Eliminates every entry below the column pivot
            if U.at(k, i) == 0:
                continue
            multiplier = U.at(k, i)/U.at(i, i)
            U.change_line(U.lines[k]-(U.lines[i]*multiplier), k)
            L.change_entry(multiplier, k, i)
    
    return {'P': P, 'L': L, 'U': U}
    

            
        