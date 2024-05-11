def calculate_points_derivative(x: list, y: list):
    '''
    input:
        - x: list of floats
        - y: list of floats
    output:
        list of floats representing the derivated points (dx/dy)
    '''
    length = len(x)
    dx = 0.0
    dy = 0.0
    derivative = []
    for i in range(1, length):
        dx = x[i]-x[i-1]
        dy = y[i]-y[i-1]
        derivative.append(dx/dy)
    return derivative

def calculate_polynomial_derivative(coeficients_list):
    derivated_coeficients_list = []
    polynomial_degree = len(coeficients_list) - 1
    for i in range(polynomial_degree):
        current_degree = polynomial_degree - i
        derivated_coeficients_list.append(current_degree * coeficients_list[i])
    
    return derivated_coeficients_list