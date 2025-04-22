from io_utils import read_phyphox_file
from graphs_visualization import generate_multiple_points_graph
import numpy as np

file_name = input("Insira o nome do arquivo: ")
data = read_phyphox_file(f'tracker_data/{file_name}')
t = data[0]
x = data[1]
y = data[2]
z = data[3]
a = data[4]

generate_multiple_points_graph([
    {'x': t, 'y': a, 'label': 'Aceleração (m/s²)'},
    # {'x': parsed_t, 'y': gravitational_potential_energy, 'label': 'Energia potencial gravitacional (J)'},
    # {'x': parsed_t, 'y': mechanical_energy, 'label': 'Energia mecânica (J)'}
    ], 'Aceleração (m/s²) x Tempo (s)', 'Tempo (s)')