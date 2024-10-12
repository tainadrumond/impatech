import numpy as np

# EXERCÍCIO 1 (classe)
class MyArray():
    def __init__(self):
        self.array = np.empty(1)
        self.size = 1
        self.current = 0
    
    def resize(self, new_size):
        '''
        Resizes the internal array to a new size.
    
        Parameters:
            new_size (int): The new size for the array.
        '''
        self.array = np.resize(self.array, new_size)
        self.size = new_size
    
    def append(self, item):
        '''
        Appends an item in the last position of the array.
        
        Parameters:
            item (any): item to be appended in the array
        '''
        if self.current >= self.size:
            self.resize(self.size*2)
        
        self.array[self.current] = item
        self.current += 1
    
    def pop(self):
        '''
        Removes the last item from the array
        
        Returns:
            item (any): the removed item
        '''
        if self.current == 0:
            return
        
        removed_item = self.array[self.current - 1]
        self.current -= 1
        if self.current < self.size//2:
            self.resize(self.size//2)
            
        return removed_item

# EXERCÍCIO 2
class Toro(np.ndarray):
    def __new__(cls, input_array):
        '''
        Creates an instance of Toro with the given input_array.
        
        Parameters:
            input_array (array-like): Array to be created as a Toro instance.
        
        Returns:
            obj (Toro): The created instance. 
        '''
        obj = np.asarray(input_array).view(cls)
        return obj

    def __init__(self, input_array):
        self.dim = len(input_array)
    
    def __getitem__(self, key):
        '''
        Returns the item at the mod of the given key by the array size
        
        Parameters:
            key (int): The item key
        
        Returns:
            item: The item at the given key 
        '''
        return super(Toro, self).__getitem__(key % self.dim)

    def __setitem__(self, key, value):
        '''
        Sets the item at the mod of the given key by the array size
        
        Parameters:
            key (int): The item key
            value: The value to be put at the index
        
        Returns:
            item: The item at the given key 
        '''
        return super(Toro, self).__setitem__(key % self.dim, value)
    

# EXERCÍCIO 3
# Para mostrar que n^2 + 1000n = O(n^2), consideramos a função f(n) = n^2 + 1000n.
# Pela definição de big-O, precisamos encontrar constantes c e N tais que f(n) <= c * n^2 para n >= N.
# Por exemplo, com c = 2 e N = 1000, temos 1 + 1000/n <= 2 para n >= 1000.
# Com c = 101 e N = 10, temos 1 + 1000/n <= 101 para n >= 10.
# Com c = 1001 e N = 1, temos 1 + 1000/n <= 1001 para n >= 1.
# Assim, n^2 + 1000n é de fato O(n^2) para essas escolhas de c e N.

# EXERCÍCIO 4
# Para mostrar que g é O(f) se e somente se f é Ω(g), consideramos as definições.
# g é O(f) se existem constantes c > 0 e N > 0 tais que g(n) <= c * f(n) para n >= N.
# f é Ω(g) se existem constantes k > 0 e M > 0 tais que f(n) >= k * g(n) para n >= M.
# Se g é O(f), então f cresce pelo menos tão rapidamente quanto g, o que implica que f é Ω(g).
# Da mesma forma, se f é Ω(g), então g não pode crescer mais rápido que f, implicando que g é O(f).
# Portanto, g é O(f) se e somente se f é Ω(g).

# EXERCÍCIO 5
# Para mostrar que g é Θ(f) se e somente se f é Θ(g), consideramos as definições.
# g é Θ(f) se existem constantes c1, c2 > 0 e N > 0 tais que c1 * f(n) <= g(n) <= c2 * f(n) para n >= N.
# f é Θ(g) se existem constantes k1, k2 > 0 e M > 0 tais que k1 * g(n) <= f(n) <= k2 * g(n) para n >= M.
# Se g é Θ(f), isso implica que g é O(f) e g é Ω(f), ou seja, f e g crescem a taxas comparáveis.
# Da mesma forma, se f é Θ(g), então f e g têm o mesmo crescimento assintótico.
# Portanto, g é Θ(f) se e somente se f é Θ(g).
