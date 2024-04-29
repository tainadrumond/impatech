import math

def newtonsMethodFunction(a: float, x: float):
    return (1/2)*(x+(a/x))

def findSquareRoot(a: float, verbose = True):
    if (verbose):
        print(f'Calculando raiz quadrada de {a}:')
    x = a
    for i in range(6):
        x = newtonsMethodFunction(a, x)
        if (verbose):
            print(x)
    return x

findSquareRoot(3.0)
print(f'Resultado da biblioteca math: {math.sqrt(3.0)}')

findSquareRoot(4.0)
print(f'Resultado da biblioteca math: {math.sqrt(4.0)}')

findSquareRoot(5.0)
print(f'Resultado da biblioteca math: {math.sqrt(5.0)}')

findSquareRoot(7.0)
print(f'Resultado da biblioteca math: {math.sqrt(7.0)}')

