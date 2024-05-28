class Vector():
    def __init__(self, values):
        """
        Initializes the vector with the given values.
        """
        self.values = values
        self.dim = len(self.values)
        
    def add(self, other_vector):
        if other_vector.dim != self.dim:
            return []
        new_vector = [0] * self.dim
        for i in range(self.dim):
            new_vector[i] = self.values[i] + self.values[i]
        return new_vector

v = Vector([0.0, 2.0, 3.5])
u = Vector([1.0, 0.5])
w = Vector([2.0, 1.5])
print(v.add(u))
print(u.add(w))