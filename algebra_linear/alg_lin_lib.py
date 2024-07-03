class DimentionError(Exception):
    def __init__(self):
        super().__init__("Inconsistent dimentions.")
        
    def __str__(self):
        return f"Error: {self.args[0]}"

class Vector():
    '''
    Class that represents a vector in R^n.
    Vector objects have imutable dimentions.
    '''
    def __init__(self, entries: list[float] = [], size = 0):
        '''
        Creates a vector with the given entries or
        with the given size initialized with 0s.
        '''
        if len(entries) == 0 and size != 0:
            self.entries = [0]*size
            self.length = size
        else:
            self.entries = entries
            self.length = len(entries)
    
    def at(self, i: int) -> float:
        '''
        Returns the i-th entry of the vector.
        '''
        if i >= self.length:
            raise DimentionError()
        return self.entries[i]
    
    def change_entry(self, value: float, index: int):
        '''
        Changes the i-th entry of the vector to the given value.
        '''
        if index >= self.length:
            raise DimentionError
        self.entries[index] = value 
        
    def copy(self):
        '''
        Returns a copy of the vector
        '''
        return Vector(self.entries.copy())

    def to_list(self) -> list[float]:
        '''
        Converts the vector to list
        '''
        return self.entries
    
    def to_matrix_list(self) -> list[list[float]]:
        '''
        Converts the vector to a list in its matrix for
        '''
        matrix = []
        for entry in self.entries:
            matrix.append([entry])
        return matrix
    
    def __mul__(self, scalar: float):
        '''
        Multiplication by scalar
        '''
        new_entries = []
        for entry in self.entries:
            new_entries.append(entry * scalar)
        return Vector(new_entries)
    
    def __matmul__(self, other) -> float:
        '''
        Inner product
        '''
        if self.length != other.length:
            raise DimentionError()
        result = 0
        for i in range(self.length):
            result += self.entries[i] * other.entries[i]
        return result
    
    def __sub__(self, other_vector):
        if other_vector.length != self.length:
            raise DimentionError()
        new_entries = []
        for i in range(self.length):
            new_entries.append(self.entries[i]-other_vector.entries[i])
        return Vector(new_entries)
    
    def __add__(self, other_vector):
        if other_vector.length != self.length:
            raise DimentionError()
        new_entries = []
        for i in range(self.length):
            new_entries.append(self.entries[i]+other_vector.entries[i])
        return Vector(new_entries)
    
    def __str__(self):
        entries_str = []
        for entry in self.entries:
            if entry == 0:
                entry = 0
            elif entry == int(entry):
                entry = int(entry)
            entries_str.append(str(entry)) 
        return '[' + ' '.join(entries_str) + ']'
            
class Matrix():
    '''
    Class that represents a matrix in R^(nxm).
    Each of its lines are represented as objects of Vector.
    Matrix objects have imutable dimentions.
    '''
    def __init__(self, lines: list[list[float]]):
        if len(lines) == 0:
            raise DimentionError()
        
        for i in range(len(lines)-1):
            if len(lines[i]) == 0 or len(lines[i]) != len(lines[i+1]):
                raise DimentionError()
        
        vectors = []
        for i in range(len(lines)):
            vectors.append(Vector(lines[i]))
        
        self.lines: list[Vector] = vectors
        self.number_of_lines = len(lines)
        self.number_of_columns = len(lines[0])
        
    def at(self, i: int, j: int) -> float:
        '''
        Returns the entry at line i and column j.
        '''
        if i >= self.number_of_lines:
            raise DimentionError()
        return self.lines[i].at(j)
    
    def change_line(self, vector: Vector, i: int):
        '''
        Changes the i-th line for the given vector
        '''
        if vector.length != self.number_of_columns:
            raise DimentionError()
        self.lines[i] = vector
        
    def change_entry(self, value: float, i: int, j: int):
        '''
        Changes the entry at the i-th line and j-th column for the given value
        '''
        if i >= self.number_of_lines:
            raise DimentionError()
        self.lines[i].change_entry(value, j)
        
    def copy(self):
        '''
        Returns a copy of the matrix.
        '''
        new_lines = []
        for line in self.lines:
            new_lines.append(line.entries.copy())
        return Matrix(new_lines)
    
    def permut(self, line_1: int, line_2: int):
        '''
        Permuts line_1 with line_2.
        '''
        if line_1 >= self.number_of_lines or line_2 >= self.number_of_lines:
            raise DimentionError()
        self.lines[line_1], self.lines[line_2] = self.lines[line_2], self.lines[line_1]
    
    def to_list(self) -> list[list[float]]:
        '''
        Converts the matrix to a list of lists
        '''
        lines: list[list[float]] = []
        for line in self.lines:
            lines.append(line.to_list())
        return lines
    
    def to_vector(self) -> Vector:
        '''
        Turns a single column matrix into a Vector object
        '''
        if self.number_of_columns != 1:
            raise DimentionError()
        entries: list[float] = []
        for line in self.lines:
            entries.append(line.at(0))
        return Vector(entries)
    
    def __mul__(self, scalar):
        '''
        Multiplication by scalar
        '''
        new_lines = []
        for line in self.lines:
            new_lines.append((line*scalar).entries.copy())
        return Matrix(new_lines)
    
    def __matmul__(self, other):
        '''
        Matrix multiplication
        '''
        if self.number_of_columns != other.number_of_lines:
            raise DimentionError()
        
        result = [[0 for _ in range(other.number_of_columns)] for _ in range(self.number_of_lines)]
        for i in range(self.number_of_lines):
            for j in range(other.number_of_columns):
                sum = 0.0
                for k in range(self.number_of_columns):
                    sum += self.at(i, k) * other.at(k, j)
                result[i][j] = sum
        return Matrix(result)
    
    def __str__(self):
        lines_str = []
        for line in self.lines:
            lines_str.append(str(line))
        return '\n'.join(lines_str)

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

def gaussian_elimination(A: list[list[float]]) -> dict[str, Matrix]:
    '''
    Computes the gaussian elimination for matrix A and returns the matrixes P, L and U of PA = LU factorization
    '''
    U = Matrix(A)
    P = build_identity_matrix(U.number_of_lines)
    matrix_of_0s = [[0 for _ in range(U.number_of_lines)] for _ in range(U.number_of_lines)]
    L = Matrix(matrix_of_0s)
    
    number_of_pivots = min(U.number_of_columns, U.number_of_lines)
    
    for i in range(number_of_pivots):
        if U.at(i, i) == 0: # If the current pivot position has a 0, then the lines are permuted
            first_non_zero_pivot_line_index = find_first_non_zero_pivot_line_index(U, i)
            if first_non_zero_pivot_line_index == -1:
                L.change_entry(1, i, i)
                continue # If there isn't any entry different from 0 for this column, it simply maintains the column of 0s in U
            U.permut(i, first_non_zero_pivot_line_index)
            P.permut(i, first_non_zero_pivot_line_index)
            L.permut(i, first_non_zero_pivot_line_index)
        
        multiplier = U.lines[i].at(i)
        U.change_line(U.lines[i]*(1/multiplier), i) # Changes the line i to turn the pivot into 1
        L.change_entry(multiplier, i, i)
            
        for k in range(i+1, U.number_of_lines): # Eliminates every entry below the current column pivot
            if U.at(k, i) == 0:
                continue
            multiplier = U.at(k, i)
            U.change_line(U.lines[k]-(U.lines[i]*multiplier), k)
            L.change_entry(multiplier, k, i)
    
    return {'P': P, 'L': L, 'U': U}

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    '''
    Function that transposes a matrix
    '''
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def forward_substitution(L: Matrix, b: Vector) -> Vector:
    '''
    Function that solves and returns y for the system Ly=b
    where L is a lower triangular matrix
    '''
    y = Vector(size=L.number_of_columns) # Initializes y as a vector of 0s
    for i in range(L.number_of_lines):
        if L.at(i, i) == 0:
            continue
        previous_terms_sum = 0.0
        for j in range(i):
            previous_terms_sum += L.at(i, j) * y.at(j)
        current_variable_value = (b.at(i) - previous_terms_sum) / L.at(i, i) 
        y.change_entry(current_variable_value, i)
    return y

def backward_substitution(U: Matrix, y: Vector) -> Vector:
    '''
    Function that solves and returns x for the system Ux=y
    where U is an upper triangular matrix
    '''
    x = Vector(size=U.number_of_columns) # Initializes x as a vector of 0s
    number_of_pivots = min(U.number_of_columns, U.number_of_lines)
    for k in range(number_of_pivots):
        i = number_of_pivots-k-1
        if U.at(i, i) == 0:
            continue
        previous_terms_sum = 0.0
        for j in range(i+1, U.number_of_columns):
            previous_terms_sum += U.at(i, j) * x.at(j)
        current_variable_value = (y.at(i) - previous_terms_sum) / U.at(i, i) 
        x.change_entry(current_variable_value, i)
    return x

def solve_linear_system(A: list[list[float]], b:list[float]) -> Vector:
    gaussian_elimination_result = gaussian_elimination(A)
    P: Matrix = gaussian_elimination_result['P']
    L: Matrix = gaussian_elimination_result['L']
    U: Matrix = gaussian_elimination_result['U']
    
    b_matrix = Matrix(Vector(b).to_matrix_list())
    permuted_b = (P@b_matrix).to_vector()

    y = forward_substitution(L, permuted_b)
    x = backward_substitution(U, y)

    return x

def is_basis(vectors: list[list[float]]) -> bool:
    '''
    Function that checks if the list of vetors can be a base
    by checking if they are linearly independents
    '''
    matrix = transpose(vectors)
    gaussian_elimination_result = gaussian_elimination(matrix)
    U = gaussian_elimination_result['U']

    if U.number_of_columns > U.number_of_lines:
        return False
    
    allowed_number_of_zero_lines = U.number_of_lines-U.number_of_columns
    number_of_zero_lines = U.number_of_lines
    for line in U.lines:
        for entry in line.entries:
            if entry != 0:
                number_of_zero_lines -= 1
                break
        
    return number_of_zero_lines == allowed_number_of_zero_lines

def get_coordinates(v: list[float], base: list[list[float]]):
    parsed_matrix = transpose(base)
    coordinates = solve_linear_system(parsed_matrix, v)
    return coordinates.to_list()

def is_orthonormal_basis(B: list[list[float]]) -> bool:
    is_base = is_basis(B)
    if not is_base:
        return False
    
    vectors = []
    for vector in B:
        vectors.append(Vector(vector))
    
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            inner_product = vectors[i]@vectors[j]
            if i != j and inner_product != 0:
                return False
            if i == j and inner_product != 1:
                return False

    return True

def get_coordinates_in_orthonormal_basis(v: list[float], B: list[list[float]]):
    coordinates = []
    
    vector = Vector(v)
    for v_i in B:
        vector_i = Vector(v_i)
        coordinates.append(vector@vector_i)
    
    return coordinates