import math
## CLASSES A SEREM HERDADAS
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
## FIM DAS CLASSES A SEREM HERDADAS

# EXERCÍCIO 1
def count_ways_of_climbing_stairs(steps: int):
    '''
    Conta, recursivamente, as maneiras de subir uma escada pulando um ou dois degraus.
    
    Args:
        steps (int): Número de degraus na escada.
    
    Returns:
        int: O número de maneiras de subir a escada.
    '''
    if steps == 0:
        return 1
    if steps < 0:
        return 0
    return count_ways_of_climbing_stairs(steps-1) + count_ways_of_climbing_stairs(steps-2)

# EXERCÍCIO 2
class Vector2D(RealVector):
    _dim = 2
    def __init__(self, coord):
        if len(coord) != 2:
            raise ValueError
        super().__init__(self._dim, coord)

    @staticmethod
    def _builder(coord):
        return Vector2D(coord)
    
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
            sum += (c1 ** 2)
        return sum**(1/2)

    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])

    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])

# EXERCÍCIO 3
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
        
class Polynomial(VectorSpace):
    """Polynomial
    Classe que representa um polinômio com um dicionário cujas chaves são os graus e os valores são os coeficientes.
    """
    _field = float
    _dim = math.inf
    def __init__(self, poly: dict[float, float]):
        """
        Inicializa uma instância de Polynomial.

        Args:
            poly (dict[float, float]): dicionário que representa os graus e coeficientes do polinômio. 
                Ex.: {4: 10, 2: 4, 1: -3.7, 0: 9} representa "10x^4 + 4x^2 - 3.7x + 9"
        """
        super().__init__(self._dim, self._field)
        self.poly = poly
        
    def get_highest_degree(self) -> float:
        '''
        Obtém o maior grau com coeficiente não nulo do polinômio.
        
        Returns:
            float: O maior grau com coeficiente não nulo do polinômio. Caso não haja coeficientes não nulos, retorna -1.
        '''
        degrees = self.poly.keys()
        sorted(degrees)
        for degree in degrees:
            if self.poly[degree] != 0:
                return degree
    
        return -1
    
    def evaluate(self, x: float):
        """
        Avalia o polinômio para a variável dada como parâmetro.

        Args:
            x (float): Valor da variável do polinômio

        Returns:
            float: Resultado do polinômio avaliado em x
        """
        
        sum = 0
        for degree, coefficient in self.poly.items():
            sum += coefficient * (x**degree)
        return sum
    
    def __add__(self, other_poly):
        degrees = set(list(self.poly.keys()) + list(other_poly.poly.keys()))
        res = {}
        
        for degree in degrees:
            res[degree] = self.poly.get(degree, 0) + other_poly.poly.get(degree, 0)
            
        return Polynomial(res)
    
    def __mul__(self, alpha):
        res = {}
        for degree, coeff in self.poly.items():
            res[degree] = coeff * alpha
        
        return Polynomial(res)
    
## EXERCÍCIO 5
## Adicionei o método __setitem__
import collections
import random
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value

myDeck = FrenchDeck()
print(myDeck[1])
random.shuffle(myDeck)