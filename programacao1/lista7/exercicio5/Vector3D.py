class Vector3D():
    def __init__(self, entries):
        self.entries = entries
    
    def __add__(self, other):
        new_entries = []
        for i in range(3):
            sum = self.entries[i] + other.entries[i]
            new_entries.append(sum)
        return Vector3D(new_entries)

    def __mul__(self, scalar):
        new_entries = []
        for entry in self.entries:
            new_entries.append(entry*scalar)
        return Vector3D(new_entries)
    
    def __rmul__(self, scalar):
        new_entries = []
        for entry in self.entries:
            new_entries.append(entry*scalar)
        return Vector3D(new_entries)      
    
    def __str__(self):
        return str(self.entries)

if __name__ == '__main__':
    vector1 = Vector3D([1, 2, 3])
    vector2 = Vector3D([1, 0, 0])
    
    print(vector1+vector2)
    print(vector1*2)
    print(vector1+(3*vector2))
    
        