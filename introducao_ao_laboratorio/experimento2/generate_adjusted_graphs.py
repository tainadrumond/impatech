import io_utils
import derivative
import curve_adjustment
import graphs_visualization

def evaluate_polynomial(polynomial, x):
    polynomial_degree = len(polynomial) - 1
    value = 0.0
    for i in range(polynomial_degree):
        value += polynomial[i] * (x ** (polynomial_degree - i))
    value += polynomial[polynomial_degree]
    return value

file_path = str(input('Insira o caminho do arquivo de dados: '))
graphs = io_utils.read_graphs_file(file_path)
time = graphs[0]
position = graphs[1]

parsed_time = []
for t in time:
    parsed_time.append(t - time[0])

adjusted_position_polynomial_coeficients = curve_adjustment.quadratic_adjustment(parsed_time, position)
print(adjusted_position_polynomial_coeficients)
graphs_visualization.generate_polynomial_graph(adjusted_position_polynomial_coeficients,  'Tempo (s)', 'Posição (m)', 'Posição x Tempo', parsed_time[0])

velocity_polynomial_coeficients = derivative.calculate_polynomial_derivative(adjusted_position_polynomial_coeficients)
graphs_visualization.generate_polynomial_graph(velocity_polynomial_coeficients,  'Tempo (s)', 'Velocidade (m/s)', 'Velocidade x Tempo', parsed_time[0])

acceleration_polynomial_coeficients = derivative.calculate_polynomial_derivative(velocity_polynomial_coeficients)
graphs_visualization.generate_polynomial_graph(acceleration_polynomial_coeficients,  'Tempo (s)', 'Aceleração (m/s²)', 'Aceleração x Tempo', parsed_time[0])

# MECHANICAL ENERGY

OBJ_MASS = 0.001

# KINETIC ENERGY
acceleration = acceleration_polynomial_coeficients[0] * (-1)
kinetic_energy = []
for t in parsed_time:
    v = evaluate_polynomial(velocity_polynomial_coeficients, t) * (-1.0)
    kinetic_energy.append(OBJ_MASS * (v**(2.0))/2.0)
    
# GRAVITATIONAL PONTENTIAL ENERGY
gravitational_potential_energy = []
final_position = evaluate_polynomial(adjusted_position_polynomial_coeficients, parsed_time[-1])
for t in parsed_time:
# for i in range(len(position)):
    # current_position = (position[len(position)-1] - position[i]) * (-1.0)
    current_position = evaluate_polynomial(adjusted_position_polynomial_coeficients,  t)
    gravitational_potential_energy.append(OBJ_MASS * acceleration * (final_position - current_position) * (-1.0))

mechanical_energy = []
for i in range(len(kinetic_energy)):
    mechanical_energy.append(kinetic_energy[i] + gravitational_potential_energy[i])
    
graphs_visualization.generate_multiple_points_graph([
    {'x': parsed_time, 'y': kinetic_energy, 'label': 'Energia cinética (J)'},
    {'x': parsed_time, 'y': gravitational_potential_energy, 'label': 'Energia potencial gravitacional (J)'},
    {'x': parsed_time, 'y': mechanical_energy, 'label': 'Energia mecânica (J)'}
    ], 'Energia mecânica', 'Tempo (s)')