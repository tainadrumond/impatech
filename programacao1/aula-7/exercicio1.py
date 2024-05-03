import math
import MYLIM

def f29(x: float):
    return (x-9)/(math.sqrt(x)-3)

def f30(x: float):
    return (4-x)/(2-math.sqrt(x))

def f31(x: float):
    if x <= 3:
        return x-1
    return (3*x)-7

print('f29:')
esquerda = MYLIM.limReal(f29, False, 9, 1000, False)
print(f'esquerda: {esquerda}')
direita = MYLIM.limReal(f29, True, 9, 1000, False)
print(f'direita: {direita}')

print('\n')

print('f30:')
esquerda = MYLIM.limReal(f30, False, 4, 1000, False)
print(f'esquerda: {esquerda}')
direita = MYLIM.limReal(f30, True, 4, 1000, False)
print(f'direita {direita}:')

print('\n')

print('f31:')
esquerda = MYLIM.limReal(f31, False, 3, 1000, False)
print(f'esquerda: {esquerda}')
direita = MYLIM.limReal(f31, True, 3, 1000, False)
print(f'direita: {direita}')
