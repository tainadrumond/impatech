import math

def newton_raphson_method(rooting: float, index: float, x: float):
    return x - (((x**index)-rooting)/(rooting*(x**(index-1))))

def find_root(rooting: float, index: float, verbose = True):
    if (verbose):
        print(f'Calculando raiz quadrada de {rooting}:')
    x = rooting
    for i in range(100):
        x = newton_raphson_method(rooting, index, x)
        if (verbose):
            print(x)
    return x

root = find_root(3.0, 2.0, False)
print(f'Resultado do método de Newton-Raphson: {root}')
print(f'Resultado usando a operação nativa do Python: {3.0**(1/2)}\n')

root = find_root(4.0, 2.0, False)
print(f'Resultado do método de Newton-Raphson: {root}')
print(f'Resultado usando a operação nativa do Python: {4.0**(1/2)}\n')

root = find_root(5.0, 2.0, False)
print(f'Resultado do método de Newton-Raphson: {root}')
print(f'Resultado usando a operação nativa do Python: {5.0**(1/2)}\n')

root = find_root(7.0, 2.0, False)
print(f'Resultado do método de Newton-Raphson: {root}')
print(f'Resultado usando a operação nativa do Python: {7.0**(1/2)}\n')

