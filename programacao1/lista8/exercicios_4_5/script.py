# EXERCÍCIO 5 - PARTE 2
# script que utiliza os módulos implementados nos exercícios 4 e 5
from polygons import *
from plot_polygons import *

plgns = Polygons()
plgns.load_from_file("polygons_to_plot.txt")
plot_polygons(plgns)