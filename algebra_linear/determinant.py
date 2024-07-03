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
    def __init__(self, entries = [], size = 0):
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
    
    def at(self, i):
        '''
        Returns the i-th entry of the vector.
        '''
        if i >= self.length:
            raise DimentionError()
        return self.entries[i]
    
    def change_entry(self, value, index):
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
    
    def __mul__(self, scalar):
        new_entries = []
        for entry in self.entries:
            new_entries.append(entry * scalar)
        return Vector(new_entries)
    
    def __matmul__(self, other):
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
    def __init__(self, lines: list):
        if len(lines) == 0:
            raise DimentionError()
        
        for i in range(len(lines)-1):
            if len(lines[i]) == 0 or len(lines[i]) != len(lines[i+1]):
                raise DimentionError()
        
        vectors = []
        for i in range(len(lines)):
            vectors.append(Vector(lines[i]))
        
        self.lines = vectors
        self.number_of_lines = len(lines)
        self.number_of_columns = len(lines[0])
        
    def at(self, i, j):
        '''
        Returns the entry at line i and column j.
        '''
        if i >= self.number_of_lines:
            raise DimentionError()
        return self.lines[i].at(j)
    
    def change_line(self, vector: Vector, i):
        '''
        Changes the i-th line for the given vector
        '''
        if vector.length != self.number_of_columns:
            raise DimentionError()
        self.lines[i] = vector
        
    def change_entry(self, value, i, j):
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
    
    def permut(self, line_1, line_2):
        '''
        Permuts line_1 with line_2.
        '''
        if line_1 >= self.number_of_lines or line_2 >= self.number_of_lines:
            raise DimentionError()
        self.lines[line_1], self.lines[line_2] = self.lines[line_2], self.lines[line_1]
    
    def __mul__(self, scalar):
        new_lines = []
        for line in self.lines:
            new_lines.append((line*scalar).entries.copy())
        return Matrix(new_lines)
    
    def __matmul__(self, other):
        if self.number_of_columns != other.number_of_lines:
            raise DimentionError()
        
        result = [[0 for _ in range(other.number_of_columns)] for _ in range(self.number_of_lines)]
        for i in range(self.number_of_lines):
            for j in range(other.number_of_columns):
                result[i][j] = self.lines[i]@other.lines[j]
        return result
    
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

def determinant(A: list[list[float]]) -> dict:
    '''
    Computes the determinant of the given square matrix
    '''
    U = Matrix(A)
    det = 1
    
    for i in range(min(U.number_of_columns, U.number_of_lines)):
        if U.at(i, i) == 0: # If the current pivot position has a 0, then the lines are permuted
            first_non_zero_pivot_line_index = find_first_non_zero_pivot_line_index(U, i)
            if first_non_zero_pivot_line_index == -1:
                return 0 # If there isn't any entry different from 0 for this column, then the det is 0
            U.permut(i, first_non_zero_pivot_line_index)
            det *= -1 # Changes the det based on the change of the P matrix's det
        
        multiplier = U.lines[i].at(i)
        U.change_line(U.lines[i]*(1/multiplier), i) # Changes the line i to turn the pivot into 1
        det *= multiplier # Changes the det based on the change of the L matrix's det
            
        for k in range(i+1, U.number_of_lines): # Eliminates every entry below the current column pivot
            if U.at(k, i) == 0:
                continue
            multiplier = U.at(k, i)
            U.change_line(U.lines[k]-(U.lines[i]*multiplier), k)
    
    return det
