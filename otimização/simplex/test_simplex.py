import numpy as np
from numpy.typing import NDArray
from simplex import solve_lp

# Exemplos
FREE = False; POSITIVE = True

ex = [
    'x = 1 com x livre. max x',
    '5x <= 2 com x livre. min -3x',
    '10x >= 3 com x livre. max 9x',
    '15x <= 4 com x positivo/0. min -27x',
    '20x >= 5 com x positivo/0. max 81x',
    'x + y <= 10 com x,y positivos/0. max 2x+3y',
    'x + y <= 20 com x,y livres. max 2x+2.001y',
    'exemplo 2.1.1 infeasible',
    'exemplo 2.1.2 unbounded',
    'exemplo 2.1.3 optimal',
    'exemplo 1.1.1 do conj teste 2 optimal',
]

A = [
    np.array([[1]],dtype=float),
    np.array([[5]],dtype=float),
    np.array([[10]],dtype=float),
    np.array([[15]],dtype=float),
    np.array([[20]],dtype=float),
    np.array([[1,1]],dtype=float),
    np.array([[1,1]],dtype=float),
    np.array([[4,10,-6,-2],[-2,2,-4,1],[-7,-2,0,4]],dtype=float),
    np.array([[1,1,-3,1,2],[0,1,-2,2,-2],[-2,-1,4,1,0]],dtype=float),
    np.array([[1,-2,1,0,2],[0,1,-1,1,3]],dtype=float),
    np.array([[11,7,6,5,0,0],[4,6,5,4,0,0],[8,5,5,6,-1,0],[7,8,7,4,0,-1],[0,0,0,0,1,0],[0,0,0,0,0,1]],dtype=float),
    np.array([],dtype=float),
]

b = [
    np.array([1],dtype=float),
    np.array([2],dtype=float),
    np.array([3],dtype=float),
    np.array([4],dtype=float),
    np.array([5],dtype=float),
    np.array([10],dtype=float),
    np.array([20],dtype=float),
    np.array([6,5,3],dtype=float),
    np.array([7,-2,-3],dtype=float),
    np.array([2,4],dtype=float),
    np.array([700,500,0,0,600,650],dtype=float),
    np.array([],dtype=float),
]

c = [
    np.array([1],dtype=float),
    np.array([-3],dtype=float),
    np.array([9],dtype=float),
    np.array([-27],dtype=float),
    np.array([81],dtype=float),
    np.array([2,3],dtype=float),
    np.array([2,2.001],dtype=float),
    np.array([1,1,1,1],dtype=float),
    np.array([-1,0,3,7,-1],dtype=float),
    np.array([0,-1,-2,0,-3],dtype=float),
    np.array([300,260,220,180,-8,-6],dtype=float),
    np.array([],dtype=float),
]

comp = [
    ['='],
    ['<='],
    ['>='],
    ['<='],
    ['>='],
    ['<='],
    ['<='],
    ['=','=','='],
    ['=','=','='],
    ['=','='],
    ['<=','<=','<=','<=','<=','<='],
    [],
]

zobj = [ #se sua objetivo somar constante
    0,0,0,0,0,0,0,0,0,
    3,
    0,
]

x = [
    np.array([FREE],dtype=float),
    np.array([FREE],dtype=float),
    np.array([FREE],dtype=float),
    np.array([POSITIVE],dtype=float),
    np.array([POSITIVE],dtype=float),
    np.array([POSITIVE,POSITIVE],dtype=float),
    np.array([FREE,FREE],dtype=float),
    np.array([POSITIVE,POSITIVE,POSITIVE,POSITIVE],dtype=float),
    np.array([POSITIVE,POSITIVE,POSITIVE,POSITIVE,POSITIVE],dtype=float),
    np.array([POSITIVE,POSITIVE,POSITIVE,POSITIVE,POSITIVE],dtype=float),
    np.array([POSITIVE,POSITIVE,POSITIVE,POSITIVE,POSITIVE,POSITIVE],dtype=float),
    np.array([],dtype=float),
]

tipo = [
    'max',
    'min',
    'max',
    'min',
    'max',
    'max',
    'max',
    'max',
    'max',
    'max',
    'max',
    '',
]


for i in range(len(ex)):
    print(f'\nExemplo: {ex[i]}')
    x_sol, opt_sol = solve_lp(tipo[i], A[i], b[i], c[i], zobj[i], comp[i], x[i])
    print(f'Solução (seu solver): x = {x_sol}')
    print(f'Valor ótimo (seu solver): z = {opt_sol}')
    print('-----------------------------------')