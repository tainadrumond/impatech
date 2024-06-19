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
            raise KeyError()
        return self.entries[i]
    
    def change_entry(self, value, index):
        '''
        Changes the i-th entry of the vector to the given value.
        '''
        if index >= self.length:
            raise KeyError
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
    
    def __sub__(self, other_vector):
        if other_vector.length != self.length:
            raise KeyError()
        new_entries = []
        for i in range(self.length):
            new_entries.append(self.entries[i]-other_vector.entries[i])
        return Vector(new_entries)
    
    def __add__(self, other_vector):
        if other_vector.length != self.length:
            raise KeyError()
        new_entries = []
        for i in range(self.length):
            new_entries.append(self.entries[i]+other_vector.entries[i])
        return Vector(new_entries)
    
    def __str__(self):
        entries_str = []
        for entry in self.entries:
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
            raise KeyError()
        for i in range(len(lines)-1):
            if lines[i].length != lines[i+1].length:
                raise KeyError()
            
        self.lines = lines
        self.number_of_lines = len(lines)
        self.number_of_columns = lines[0].length
        
    def at(self, i, j):
        '''
        Returns the entry at line i and column j.
        '''
        if i >= self.number_of_lines:
            raise KeyError()
        return self.lines[i].at(j)
    
    def change_line(self, vector: Vector, i):
        '''
        Changes the i-th line for the given vector
        '''
        if vector.length != self.number_of_columns:
            raise KeyError()
        self.lines[i] = vector
        
    def change_entry(self, value, i, j):
        '''
        Changes the entry at the i-th line and j-th column for the given value
        '''
        if i >= self.number_of_lines:
            raise KeyError()
        self.lines[i].change_entry(value, j)
        
    def copy(self):
        '''
        Returns a copy of the matrix.
        '''
        new_lines = []
        for line in self.lines:
            new_lines.append(line.copy())
        return Matrix(new_lines)
    
    def permut(self, line_1, line_2):
        '''
        Permuts line_1 with line_2.
        '''
        if line_1 >= self.number_of_lines or line_2 >= self.number_of_lines:
            raise KeyError()
        self.lines[line_1], self.lines[line_2] = self.lines[line_2], self.lines[line_1]
    
    def __mul__(self, scalar):
        new_lines = []
        for line in self.lines:
            new_lines.append(line*scalar)
        return Matrix(new_lines)
    
    def __str__(self):
        lines_str = []
        for line in self.lines:
            lines_str.append(str(line))
        return '\n'.join(lines_str)