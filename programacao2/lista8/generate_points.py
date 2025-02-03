# python 3

import numpy as np

def generate_points(m):
    np.random.seed(1)
    a = 6
    b = -3
    x = np.linspace(0, 10, m)
    y = a*x + b + np.random.standard_cauchy(size=m)

    return (x,y)

def save_points(points, path = 'test_points.txt' ):
    with open(path, 'wt') as f:
        for x, y in zip(points[0], points[1]):
            f.write(f'{x} {y}\n')


if __name__ == "__main__":
    points = generate_points(10)
    save_points(points)