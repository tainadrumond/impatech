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
import derivation
import graphs_visualization

def read_graphs_file(file_name):
    x = []
    t = []
    try:
        with open(file_name, 'r') as arquivo:
            for linha in arquivo:
                if (linha.startswith('t')):
                    continue
                values = linha.split('	')
                t.append(float(values[0]))
                x.append(float(values[1].removesuffix('\n')))
    except:
        raise ValueError('Formato de arquivo inválido!')
    return [x, t]

file_name = str(input('Insira o nome do arquivo de dados: '))
graphs = read_graphs_file(file_name)
position = graphs[0]
time = graphs[1]

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

# POSITION:
position_moving_average = moving_average.make_moving_average(position, pace)
length = len(time)
time = time[pace:length-pace] # necessary because the moving average reduces the total of points

graphs_visualization.generate_graph(time, position_moving_average, 'Tempo (s)', 'Posição (m)', 'Posição x Tempo')

# VELOCITY:
velocity = derivation.calculate_derivation(position_moving_average, time)
time = time[1:]
graphs_visualization.generate_graph(time, velocity, 'Tempo (s)', 'Velocidade (v)', 'Velocidade x Tempo')


# ACCELERATION:
parsed_velocity = velocity
if (apply_moving_average_in_velocity == "S"):
    parsed_velocity = moving_average.make_moving_average(velocity, pace)
    length = len(time)
    time = time[pace:length-pace] # necessary because the moving average reduces the total of points

acceleration = derivation.calculate_derivation(parsed_velocity, time)
time = time[1:]

graphs_visualization.generate_graph(time, acceleration, 'Tempo', 'Aceleração', 'AxT')
