# EXERCÍCIO 5 - PARTE 2
from polygons import *
import turtle

def plot_polygons(plgns: Polygons):
    t = turtle.Turtle()
    for polygon in plgns.polygons.values():
        if len(polygon.points) == 0:
            continue
        t.penup()
        t.color(polygon.color)
        t.goto(polygon.points[0].coord)
        t.pendown()
        for point in polygon.points[1:]:
            t.goto(point.coord)
        t.goto(polygon.points[0].coord)
    turtle.done()