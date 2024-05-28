# EXERCÍCIO 1
# 
# a) 
# 1
# 2
# 
# b)
# Value is bad
# 
# c)
# que massa!
# 
# d)
# [1, 2, 5, 4]


# EXERCÍCIO 2 
# 
# a)
# Renomear a função __ints__ para __init__
# 
# b)
# A saída esperada será:
# []
# [2.0, 1.0]
# 
# c)
# A função add não faz de fato o que ela documenta. A linha 20 (new_vector[i] = self.values[i] + self.values[i])
# faz com a função add multiplique por 2 as entradas do vetor na qual ela foi chamada, e não com que adicione o vetor passado
# como parâmetro. Caso a função realmente adicionasse os dois vetores, a linha 20 seria:
# new_vector[i] = self.values[i] + other_vector.values[i]


# EXERCÍCIO 3
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_same(self, point):
        return point.x == self.x and point.y == self.y
        
class Circle():
    def __init__(self, radius: float):
        self.radius = radius
        
    def is_in_circle(self, point):
        return (point.x**2 + point.y**2)**0.5 <= self.radius

class Line_Segment():
    def __init__(self, point1, point2):
        if point1.x == point2.x: # ordena os pontos a partir do valor de y
            self.point1 = point1 if point1.y <= point2.y else point2
            self.point2 = point2 if point1.y <= point2.y else point1
        else: # ordena os pontos a partir do valor de x
            self.point1 = point1 if point1.x <= point2.x else point2
            self.point2 = point2 if point1.x <= point2.x else point1
            
    def is_in_segment(self, point3):
        if point3.is_same(self.point1) or point3.is_same(self.point2): # caso em que o ponto está em uma das extremidades do segmento
            return True
        
        if self.point1.x == self.point2.x: # caso em que os pontos estão no mesmo segmento vertical
            y_value_is_valid = point3.y >= self.point1.y and point3.y <= self.point2.y
            return self.point1.x == point3.x and y_value_is_valid
        
        # análise para o caso em que o segmento não é vertical:
        x_value_is_valid = point3.x >= self.point1.x and point3.x <= self.point2.x
        inclination1 = (self.point2.y - self.point1.y)/(self.point2.x - self.point1.x)
        inclination2 = (point3.y - self.point1.y)/(point3.x - self.point1.x)     
        
        return x_value_is_valid and inclination1 == inclination2

print("\nExercício 3")
circle = Circle(3.0)
print("a) ", circle.is_in_circle(Point(0, 3.0)))
line_segment = Line_Segment(Point(1, 1), Point(1, 2))
print("b) ", line_segment.is_in_segment(Point(1, 1.5)))


# EXERCÍCIO 4
def is_line_segment_in_circle(line_segment, circle):
    point1_is_in_circle = circle.is_in_circle(line_segment.point1)
    point2_is_in_circle = circle.is_in_circle(line_segment.point2)
    return point1_is_in_circle and point2_is_in_circle

print("\nExercício 4")
print(is_line_segment_in_circle(line_segment, circle))


# EXERCÍCIO 5
class Vector():
    def __init__(self, entries):
        self.entries = entries
        
    def dyadic_product(self, vector):
        matrix = []
        for i in self.entries:
            line = []
            for j in vector.entries:
                line.append(i*j)
            matrix.append(line.copy())
        return matrix

u = Vector([0.0, 2.0, 3.5])
v = Vector([1.0, 0.5])
print("\nExercício 5")
print(u.dyadic_product(v))
print(v.dyadic_product(u))
