class VectorSpace:
    """VectorSpace:
    Abstract Class of vector space used to model basic linear structures
    """
    
    def __init__(self, dim: int, field: 'Field'):
        """
        Initialize a VectorSpace instance.

        Args:
            dim (int): Dimension of the vector space.
            field (Field): The field over which the vector space is defined.
        """
        self.dim = dim
        self._field = field
        
    def getField(self):
        """
        Get the field associated with this vector space.

        Returns:
            Field: The field associated with the vector space.
        """
        return self._field
    
    def getVectorSpace(self):
        """
        Get a string representation of the vector space.

        Returns:
            str: A string representing the vector space.
        """
        return f'dim = {self.dim!r}, field = {self._field!r}'
        # return self.__repr__()

    def __repr__(self):
        """
        Get a string representation of the VectorSpace instance.

        Returns:
            str: A string representing the VectorSpace instance.
        """
        # return f'dim = {self.dim!r}, field = {self._field!r}'
        return self.getVectorSpace()
    
    def __mul__(self, f):
        """
        Multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError
    
    def __rmul__(self, f):
        """
        Right multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Returns:
            The result of multiplication.

        Note:
            This method is defined in terms of __mul__.
        """
        return self.__mul__(f)
    
    def __add__(self, v):
        """
        Addition operation on the vector space (not implemented).

        Args:
            v: The vector to be added.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError

class RealVector(VectorSpace):
    _field = float
    def __init__(self, dim, coord):
        super().__init__(dim, self._field)
        self.coord = coord
    

    @staticmethod
    def _builder(coord):
        raise NotImplementedError


    def __add__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1+c2)
        return self._builder(n_vector)


    def __mul__(self, alpha):
        n_vector = []
        for c in self.coord:
            n_vector.append(alpha*c)
        return self._builder(n_vector)
    
    
    def iner_prod(self, other_vector):
        res = 0
        for c1, c2 in zip(self.coord, other_vector.coord):
            res += c1*c2
        return res


    def __str__(self):
        ls = ['[']
        for c in self.coord[:-1]:
            ls += [f'{c:2.2f}, ']
        ls += f'{self.coord[-1]:2.2f}]'
        s =  ''.join(ls)
        return s

class Vector3D(RealVector):
    _dim = 3
    def __init__(self, coord):
        if len(coord) != 3:
            raise ValueError
        super().__init__(self._dim, coord)

    @staticmethod
    def _builder(coord):
        return Vector3D(coord)
    
    def __sub__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1-c2)
        return self._builder(n_vector)
    
    def __neg__(self):
        n_vector = []
        for c1 in self.coord:
            n_vector.append(-c1)
        return self._builder(n_vector)
    
    def __abs__(self):
        sum = 0
        for c1 in self.coord:
            sum += (c1**2)
        return sum**(1/2)
    
    def cross_product(self, other_vector):
        '''
        Calcula o produto vetorial entre o vetor atual e outro vetor em R^3
        
        Args:
            other_vector: O outro vetor para calcular o produto vetorial
        
        Returns:
            O resultado do produto vetorial.
        '''
        # Cálculo do valor de cada coordenada do produto vetorial:
        x = (self.coord[1] * other_vector.coord[2]) - (self.coord[2] * other_vector.coord[1]) 
        y = -1 * ((self.coord[0] * other_vector.coord[2]) - (self.coord[2] * other_vector.coord[0]))
        z = (self.coord[0] * other_vector.coord[1]) - (self.coord[1] * other_vector.coord[0])
        
        return self._builder([x, y, z])