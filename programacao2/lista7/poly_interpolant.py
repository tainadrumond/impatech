# Python 3
import numpy as np


class interpolater:

    def evaluate(self, X):
        raise NotImplementedError

    def __call__(self,  X):
        return self.evaluate(X)


class VandermondeMatrix(interpolater):
    def __init__(self, x, y):
        if len(x) != len(y):
            raise RuntimeError(f"Dimensions must be equal len(x) = {len(x)} != len(y) = {len(y)}")
        self.data = [x, y]
        self._degree = len(x) -1
        self._buildMatrix()
        self._poly = np.linalg.solve(self.matrix, self.data[1])

    def _buildMatrix(self):
        self.matrix = np.ones([self._degree+1, self._degree+1])
        for i, x in enumerate(self.data[0]):
            self.matrix[i, 1:] = np.multiply.accumulate(np.repeat(x, self._degree))
    
    def evaluate(self, X):
        r = 0.0
        for c in self._poly[::-1]:
            r = c+r*X
        return r


def random_sample(intv, N):
    r = np.random.uniform(intv[0], intv[1], N-2)
    r.sort()
    return np.array([intv[0]] + list(r) + [intv[1]])

def error_pol(f, P, intv, n = 1000):
    x = random_sample(intv, n)
    vectError = np.abs(f(x)-P(x))
    return np.sum(vectError)/n, np.max(vectError)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    DataX = [10.7       , 11.075     , 11.45      , 11.825     , 12.2       , 12.5]
    DataY = [-0.25991903,  0.04625002,  0.16592075,  0.13048074,  0.13902777, 0.2]

    Pvm = VandermondeMatrix(DataX, DataY)

    X = np.linspace(min(DataX)-0.2, max(DataX)+0.2, 100)
    Y = Pvm(X)

    _, ax = plt.subplots(1)
    ax.plot(X,Y)
    ax.axis('equal')
    ax.plot(DataX, DataY, 'o')
    plt.show()