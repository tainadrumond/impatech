class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_equal(self, point):
        return point.x == self.x and point.y == self.y
        
class Circle():
    def __init__(self, radius: float):
        self.radius = radius
        
    def is_in_circle(self, point):
        return (point.x**2 + point.y**2)**0.5 <= self.radius

class Line_Segment():
    def __init__(self, point1, point2):
        if point1.x == point2.x:
            self.point1 = point1 if point1.y <= point2.y else point2
            self.point2 = point2 if point1.y <= point2.y else point1
        else:
            self.point1 = point1 if point1.x <= point2.x else point2
            self.point2 = point2 if point1.x <= point2.x else point1
            
    def is_in_segment(self, point3):
        if point3.is_equal(self.point1) or point3.is_equal(self.point2):
            return True
        
        if self.point1.x == self.point2.x:
            y_value_is_valid = point3.y >= self.point1.y and point3.y <= self.point2.y
            return self.point1.x == point3.x and y_value_is_valid
        
        x_value_is_valid = point3.x >= self.point1.x and point3.x <= self.point2.x
        inclination1 = (self.point2.y - self.point1.y)/(self.point2.x - self.point1.x)
        inclination2 = (point3.y - self.point1.y)/(point3.x - self.point1.x)     
        
        return x_value_is_valid and inclination1 == inclination2
    
circle = Circle(1.0)
line_segment = Line_Segment(Point(1, 2), Point(2, 2))
print(line_segment.is_in_segment(Point(0.5, 2)))