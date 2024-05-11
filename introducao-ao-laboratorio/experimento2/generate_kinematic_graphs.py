'''
input:
    - file_name: str for the name of the file with the time and position entries
        - file format:
            t   x
            []	[]
            obs.: 1- t is the column for time (s) and x is for position (m)
                  2- it is important to leave the right amount of space 
                  between the two variables entries (sugestion: copy the 
                  space from the file format example above)
    - paces: int for the number of paces used as a lower and upper bound in the
             moving average function
output:
    displays the position moving average, velocity and acceleration graphs
'''

import moving_average
import derivative
import graphs_visualization
import io_utils

file_path = str(input('Insira o caminho do arquivo de dados: '))
graphs = io_utils.read_graphs_file(file_path)
time = graphs[0]
position = graphs[1]

temp = list(time)
time = []
for t in temp:
    time.append(t - temp[0])
parsed_time = list(time)

pace = int(input('Insira o número de passos usado como delimitador da média móvel: '))
if pace < 1:
    raise ValueError("O número de passos não pode ser menor que 1")

apply_moving_average_in_velocity = str(input("Deseja aplicar a média móvel sobre a velocidade? (S/N) "))
if ((apply_moving_average_in_velocity != "S") & (apply_moving_average_in_velocity != "N")):
    raise ValueError("Resposta inválida!")

velocity_pace = 0
if (apply_moving_average_in_velocity == "S"):
    velocity_pace = int(input("Insira o número de passos usado como delimitador da média móvel para a velocidade: "))
    if (velocity_pace < 1):
        raise ValueError("O número de passos não pode ser menor que 1")

apply_moving_average_in_acceleration = str(input("Deseja aplicar a média móvel sobre a aceleração? (S/N) "))
if ((apply_moving_average_in_acceleration != "S") & (apply_moving_average_in_acceleration != "N")):
    raise ValueError("Resposta inválida!")

acceleration_pace = 0
if (apply_moving_average_in_acceleration == "S"):
    acceleration_pace = int(input("Insira o número de passos usado como delimitador da média móvel para a aceleração: "))
    if (acceleration_pace < 1):
        raise ValueError("O número de passos não pode ser menor que 1")

# POSITION:
position_moving_average = moving_average.make_moving_average(position, pace)
length = len(parsed_time)
parsed_time = parsed_time[pace:length-pace] # necessary because the moving average reduces the total of points

graphs_visualization.generate_points_graph(parsed_time, position_moving_average, 'Tempo (s)', 'Posição (m)', 'Posição x Tempo')

# VELOCITY:
velocity = derivative.calculate_points_derivative(position_moving_average, parsed_time)
parsed_time = parsed_time[1:]

parsed_velocity = velocity
if (apply_moving_average_in_velocity == "S"):
    parsed_velocity = moving_average.make_moving_average(velocity, velocity_pace)
    length = len(parsed_time)
    parsed_time = parsed_time[velocity_pace:length-velocity_pace] # necessary because the moving average reduces the total of points

graphs_visualization.generate_points_graph(parsed_time, parsed_velocity, 'Tempo (s)', 'Velocidade (m/s)', 'Velocidade x Tempo')


# ACCELERATION:
acceleration = derivative.calculate_points_derivative(parsed_velocity, parsed_time)
parsed_time = parsed_time[1:]

parsed_acceleration = acceleration
if (apply_moving_average_in_acceleration == "S"):
    parsed_acceleration = moving_average.make_moving_average(acceleration, acceleration_pace)
    length = len(parsed_time)
    parsed_time = parsed_time[acceleration_pace:length-acceleration_pace] # necessary because the moving average reduces the total of points

graphs_visualization.generate_points_graph(parsed_time, parsed_acceleration, 'Tempo (s)', 'Aceleração (m/s²)', 'AxT')


# MECHANICAL ENERGY

OBJ_MASS = 0.001

# KINETIC ENERGY
parsed_time = time
velocity_without_moving_average =  derivative.calculate_points_derivative(position, parsed_time)
parsed_time = parsed_time[1:]

kinetic_energy = []
for v in velocity_without_moving_average:
    kinetic_energy.append(OBJ_MASS * (v**2)/2)
    
# GRAVITATIONAL PONTENTIAL ENERGY
acceleration_without_moving_average = derivative.calculate_points_derivative(velocity_without_moving_average, parsed_time)
parsed_time = parsed_time[1:]

acceleration_sum = 0.0
for a in acceleration_without_moving_average:
    acceleration_sum += a
acceleration_average = (-1.0) * acceleration_sum / len(acceleration_without_moving_average)

gravitational_potential_energy = []
for i in range(2, len(position)):
    gravitational_potential_energy.append(OBJ_MASS * acceleration_average * (-1.0) * (position[len(position)-1] - position[i]))

mechanical_energy = []
kinetic_energy = kinetic_energy[1:]
for i in range(len(kinetic_energy)):
    mechanical_energy.append(kinetic_energy[i] + gravitational_potential_energy[i])
    
graphs_visualization.generate_multiple_points_graph([
    {'x': parsed_time, 'y': kinetic_energy, 'label': 'Energia cinética (J)'},
    {'x': parsed_time, 'y': gravitational_potential_energy, 'label': 'Energia potencial gravitacional (J)'},
    {'x': parsed_time, 'y': mechanical_energy, 'label': 'Energia mecânica (J)'}
    ], 'Energia mecânica', 'Tempo (s)')