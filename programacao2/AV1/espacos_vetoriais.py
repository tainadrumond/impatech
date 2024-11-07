# Python 3

class VectorSpace:
    def __init__(self, dim: int, field):
        self.dim = dim
        self._field = field
        
    def getField(self):
        return self._field
    
    def getVectorSpace(self):
        return f'dim = {self.dim!r}, field = {self._field!r}'

    def __repr__(self):
        return self.getVectorSpace()
    
    def __mul__(self, f):
        raise NotImplementedError
    
    def __rmul__(self, f):
        return self.__mul__(f)
    
    def __add__(self, v):
        raise NotImplementedError
    
    def __sub__(self, v):
        return self.__add__(-1*v)
    
    def __neg__(self):
        return self.__mul__(-1)

class RealVector(VectorSpace):
    _field = float
    def __init__(self, dim, coord):
        super().__init__(dim, self._field)
        self.coord = coord

    @staticmethod
    def _builder(coord):
        raise NotImplementedError
    
    def norm_L2(self):
        return sum([x**2 for x in self.coord])**.5

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
            ls += [f'{c}, ']
        ls += f'{self.coord[-1]}]'
        s =  ''.join(ls)
        return s


class Vector2D(RealVector):
    _dim = 2
    def __init__(self, coord):
        if len(coord) != 2:
            raise ValueError
        super().__init__(self._dim, coord)

    @staticmethod
    def _builder(coord):
        return Vector2D(coord)
    
    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])
    
    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])
    
class Polinomio_Lista(VectorSpace):
    """
    Representação de polinômio usando lista de python,
    onde o indice [i] da lista representa o grau do monômio X^i 
    """
    _field = float
    def __init__(self, coefs: list):
        super().__init__('INF', self._field)
        self.coefs = coefs
        self._fix_grau()

    def _fix_grau(self):
        while self.coefs[-1] == 0:
            self.coefs.pop()

    def _soma_1(self, other_pol):
        r = []
        sv = self if self.grau < other_pol.grau else other_pol
        gv = self if self.grau >= other_pol.grau else other_pol
        for i in range(sv.grau+1):
            r.append(sv[i] + gv[i])
        r += gv[sv.grau+1:]
        return Polinomio_Lista(r)

    def _soma_2(self, other_pol):
        r = [0]*max(self.grau+1,other_pol.grau+1)
        sv = self if self.grau < other_pol.grau else other_pol
        gv = self if self.grau >= other_pol.grau else other_pol
        for i in range(sv.grau+1):
            r[i] = sv[i] + gv[i]
        for i in range(sv.grau+1, gv.grau+1):
            r[i] = gv[i]
        return Polinomio_Lista(r)
    
    def _mult_escalar_1(self, escalar):
        r = []
        for c in self:
            r.append(c*escalar)
        return Polinomio_Lista(r)

    def _mult_escalar_2(self, escalar):
        r = [0]*(self.grau+1)
        for i in range(self.grau+1):
            r[i] = self[i]*escalar
        return Polinomio_Lista(r)

    def __getitem__(self, index):
        return self.coefs[index]

    def __repr__(self):
        return " + ".join([f"{c}x^{i}" if i > 0 else str(c) for i, c in enumerate(self.coefs) if c != 0])
    
    def eval1(self, x):
        r = 0.0
        for c in self[::-1]:
            r = c + r*x
        return r

    def eval2(self, x):
        r = 0.0
        for i, c in enumerate(self):
            r += c*x**i
        return r

    @property
    def grau(self):
        return len(self.coefs) - 1


if __name__ == '__main__':
#############  Vector2D  ###############
    print('**** Vector2D ****')
    V2 = Vector2D([.1, .2]) 
    print('V2 = ', V2) 
# Saída: V2 =  [0.10, 0.20]
    W2 = Vector2D([.3, .6])
    print('-W2 = ', -W2) 
# Saída: -W2 =  [-0.30, -0.60]
    print(V2.getVectorSpace()) 
# Saída: dim = 2, field = <class 'float'>
    r = V2+4*W2-(1.5*V2-W2)
    print('V2+4*W2-(1.5*V2-W2) =', r) 
# Saída: V2 + 4*W2 = [1.30, 2.60]
    print('(V2+4*W2-(1.5*V2-W2)).CW() = ', r.CW()) 
# Saída: (V2 + 4*W2).CW() =  [-2.60, 1.30]
    print('W2.CCW() = ', W2.CCW()) 
# Saída: W2.CCW() =  [0.60, -0.30]
    print('V2.iner_prod(W2) = ', V2.iner_prod(W2)) 
# Saída: V2.iner_prod(W2) =  0.15
    print('3*V2 =', 3*V2, '    W2 = ', W2 )
# Saída: 3*V2 = [0.30, 0.60]     W2 =  [0.30, 0.60]
    print('3*V2 == W2', 3*V2 == W2)
# Saída: False


#############  Polinomio  ###############
    print('\n**** Polinomio ****')
    P1 = Polinomio_Lista([1, 2, 3, 4])
    P2 = Polinomio_Lista([0, 4, 0, 0, 2, 0])
    print(P1, '  --  ', P2 )
# Saída: 1 + 2x^1 + 3x^2 + 4x^3   --   4x^1 + 2x^4
    print(P1.grau, P2.grau)
# Saída: 3 4
    print(P1._soma_1(P2))
# Saída: 1 + 6x^1 + 3x^2 + 4x^3 + 2x^4
    print(P2._mult_escalar_1(.5))
# Saída: 2.0x^1 + 1.0x^4
    print(P2.eval1(2))
# Saída: 40.0

