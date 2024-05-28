from exercicio3 import Circle
from exercicio3 import Line_Segment

def is_line_segment_in_circle(line_segment, circle):
    return line_segment.is_in_circle(circle)

circle = Circle(1.0)
line_segment = Line_Segment(1, 0, 1, 0)
print(is_line_segment_in_circle(line_segment, circle))



    # def is_in_circle(self, circle):
    #     point1_is_in_circle = circle.is_in_circle(self.x1, self.y1)
    #     point2_is_in_circle = circle.is_in_circle(self.x2, self.y2)
    #     return point1_is_in_circle and point2_is_in_circle
    
