def calculate_derivation(x: list, y: list):
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
    derivation = []
    for i in range(1, length):
        dx = x[i]-x[i-1]
        dy = y[i]-y[i-1]
        derivation.append(dx/dy)
    return derivation
    