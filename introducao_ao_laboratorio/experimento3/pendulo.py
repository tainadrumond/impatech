from io_utils import read_graphs_file
from graphs_visualization import generate_multiple_points_graph
import numpy as np

file_name = input("Insira o nome do arquivo: ")
data = read_graphs_file(f'tracker_data/{file_name}')
t = data[0]
parsed_t = []
for i in t:
    parsed_t.append(i - t[0])

t = np.array(data[0])
y = np.array(data[1])
v = np.array(data[2])

a = 9.8
m = 0.1

kinetic_energy = 0.5*m*(v**2)
gravitational_potential_energy = m*a*y
mechanical_energy = kinetic_energy + gravitational_potential_energy

generate_multiple_points_graph([
    {'x': parsed_t, 'y': kinetic_energy, 'label': 'Energia cinética (J)'},
    {'x': parsed_t, 'y': gravitational_potential_energy, 'label': 'Energia potencial gravitacional (J)'},
    {'x': parsed_t, 'y': mechanical_energy, 'label': 'Energia mecânica (J)'}
    ], 'Energia mecânica', 'Tempo (s)')