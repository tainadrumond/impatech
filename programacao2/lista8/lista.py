# EXERCÍCIO 1
import numpy as np
import matplotlib.pyplot as plt

def polynomial_approximation(points: list[tuple[float, float]], d: int):
    '''
    Approximate the list of points by a polynomial of degree d.
    Returns:
        coeffs (list[float]): list of floats representing the polynomial. The ith element is the coefficient for x^i
    '''
    x_coords = np.array([p[0] for p in points]) # Separate the x coordinates
    X = np.vander(x_coords, d+1, True) # Calculate the Vandermonde matrix of xs
    
    Y = np.array([p[1] for p in points]) # Separate the y coordinates
    
    # Calculate the list of coefficients by solving coeffs = (((X^T)X)^(-1))(X^T)Y
    coeffs = np.linalg.matmul(np.linalg.matmul(np.linalg.inv(np.linalg.matmul(X.transpose(), X)), X.transpose()), Y.transpose())
    return coeffs

points = [(0.45, 0.67), (0.23, 0.89), (0.76, 0.15), (0.34, 0.58), (0.91, 0.41),  (0.64, 0.73), (0.17, 0.29), 
          (0.83, 0.56), (0.49, 0.82), (0.31, 0.92),  (0.78, 0.11), (0.26, 0.63), (0.55, 0.34), (0.72, 0.48), 
          (0.39, 0.77),  (0.87, 0.25), (0.68, 0.39), (0.21, 0.81), (0.93, 0.14), (0.53, 0.62)]

# EXERCÍCIO 1 - TESTE:
coeffs = polynomial_approximation(points, 4)

fx = np.linspace(0, 1, 500)
fy = np.polyval(coeffs[::-1], fx)
plt.scatter(fx, fy, color='red', label='Aproximação')

x, y = zip(*points)
plt.scatter(x, y, color='blue', label='Pontos')
plt.show()


# EXERCÍCIO 2
def eval_poly(poly, x):
    sum = 0
    for i in range(len(poly)):
        sum += poly[i]*(x**i)
        
    return sum

def calculate_r_2(points: list[tuple[float, float]], poly: list[float]):
    '''
    Calculate the coefficient of determination (R^2) for the approximation of the poly
    for the given list of points.
    
    Parameters:
        points (list[tuple[float, float]]): list of the points coordinates
        poly (list[float]): list of floats representing the polynomial. The ith element is the coefficient for x^i
    
    Returns:
        r_2 (float): coefficient of determination
    '''
    rss = 0 # Sum of squared residuals
    sum_y = 0
    for x, y in points:
        f_x = eval_poly(poly, x)
        rss += (f_x - y)**2
        sum_y += y
    
    avrg_y = sum_y/len(points)
    rst = 0 # Total sum of squares
    for x, y in points:
        rst += (y - avrg_y)**2
    
    r_2 = 1 - (rss/rst) # Coefficient of determination
    return r_2

def get_best_approximation_poly_degree(points: list[tuple[float, float]], max_degree: int):
    '''
    Define the best degree in range [1, max_degree] of the polynomial approximation for the given points.
    
    Parameters:
        points (list[tuple[float, float]]): list of the points coordinates
        max_degree (int): the maximum degree to be evaluated
    
    Returns:
        best_r_2_degree (int): the best polynomial approximation degree
    '''
    best_r_2 = 0
    best_r_2_degree = 0
    
    for d in range(1, max_degree + 1):
        poly = polynomial_approximation(points, d)
        r_2 = calculate_r_2(points, poly)
        if r_2 > best_r_2:
            best_r_2 = r_2
            best_r_2_degree = d
    
    return best_r_2_degree

# EXERCÍCIO 2: TESTES
# Nos seguintes teste, eu crio pontos determinados por um polinômio de grau n. 
# A ideia é que a saída da função retorne o mesmo grau do polinômio de entrada,
# pois ele representa a melhor função de aproximação.
def generate_points1(poly, n_points):
    x_coords = np.linspace(-10, 10, n_points)
    points = []
    for x in x_coords:
        y = eval_poly(poly, x)
        points.append((x, y))
    return points

points = generate_points1([1, 3, 2], 100)  # y = 2x^2 + 3x + 1
best_degree = get_best_approximation_poly_degree(points, max_degree=5)
print(f"Teste 1 - Melhor grau esperado: 2, Encontrado: {best_degree}")

points = generate_points1([1, -4, 2, -1], 100)  # y = -x^3 + 2x^2 - 4x + 1
best_degree = get_best_approximation_poly_degree(points, max_degree=5)
print(f"Teste 2 - Melhor grau esperado: 3, Encontrado: {best_degree}")

points = generate_points1([-2, 5], 100)  # y = 5x - 2
best_degree = get_best_approximation_poly_degree(points, max_degree=5)
print(f"Teste 3 - Melhor grau esperado: 1, Encontrado: {best_degree}")

points = generate_points1([-1, 1, 0, -2, 0, 1], 100)  # y = x^5 - 2x^3 + x - 1
best_degree = get_best_approximation_poly_degree(points, max_degree=10)
print(f"Teste 4 - Melhor grau esperado: 5, Encontrado: {best_degree}")

points = generate_points1([1, 1, 2], 100)  # y = 2x^2 + x + 1
best_degree = get_best_approximation_poly_degree(points, max_degree=10)
print(f"Teste 5 - Melhor grau esperado: 2, Encontrado: {best_degree}")

points = generate_points1([3, -5, 2, 0, 7, -4, 1, -8, 6, 9, -2], 100)
best_degree = get_best_approximation_poly_degree(points, max_degree=10)
print(f"Teste 6 - Melhor grau esperado: 10, Encontrado: {best_degree}")


# EXERCÍCIO 3 - ITEM (a)
from scipy.optimize import minimize
def sum_1(coeffs: list, points: list[tuple[float, float]]):
    '''
    Sum of absolute values of a*x + b - y
    '''
    res = 0
    a, b = coeffs[0], coeffs[1]
    for x, y in points:
        res += abs(a*x + b - y) 
    return res   
    
def get_best_linear_coeffs(points):
    best_coeffs = minimize(sum_1, [1, 1], args=(points,), method='Powell').x
    return best_coeffs

# EXERCÍCIO 3 - ITEM (c)
from generate_points import generate_points

def minimized_squares(points: list[tuple[float, float]]):
    '''
    Get a and b that minimize sum_i((a*x_i + b - y_i)^2)
    '''
    n = len(points)
    x_coors, y_coords = zip(*points)
    x_sum = sum(x_coors)
    y_sum = sum(y_coords)
    x_squared_sum = sum([x ** 2 for x in x_coors])
    xy_sum = sum(x*y for x, y in points)
    
    a = ((n*xy_sum) - (x_sum*y_sum))/((n*x_squared_sum) - (x_sum**2))
    b = (y_sum - (a*x_sum))/n
    
    return [a, b]

# EXERCÍCIO 3 - ITEM (b)/ITEM (d)
vars = [64, 128, 256, 512, 1024]
for var in vars:
    # ITEM (b)
    coords_list = generate_points(var)
    points = []
    for i in range(len(coords_list[0])):
        points.append((coords_list[0][i], coords_list[1][i]))
        
    best_coeffs_1 = get_best_linear_coeffs(points)
    best_coeffs_2 = minimized_squares(points)
    
    # ITEM (d)
    # Plot the points and both approximation linear functions 
    x, y = zip(*points)
    plt.scatter(x, y, color='blue', s=5, label='Pontos')
    
    fx = np.linspace(0, 10, 1000)
    
    fy1 = np.polyval(best_coeffs_1, fx)
    plt.scatter(fx, fy1, color='red', s=1, label='Minimização 1')
    
    fy2 = np.polyval(best_coeffs_2, fx)
    plt.scatter(fx, fy2, color='green', s=1, label='Minimização 2')

    plt.show()
    
# EXERCÍCIO 4
# A primeira abordagem tem a vantagem de ser menos sensível a dados de entrada que fogem muito da média.
# Como o método dos mínimos quadrados eleva a distância da avaliação da função para seu valor real ao quadrado,
# valores muito distantes da média têm um peso maior na soma, o que acaba impactando na aproximação final.

# A segunda abordagem tem a vantagem do custo computacional reduzido para ser minimizada. Isso ocorre devido
# à existência da solução analítica direta para encontrar os coeficientes a e b, sem a necessidade de 
# métodos mais complexos de minimização.