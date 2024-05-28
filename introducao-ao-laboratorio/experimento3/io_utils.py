import os

def read_graphs_file(file_path):
    file_content = read_file(file_path)
    parsed_file_data = parse_file_data(file_content)
    return parsed_file_data

def read_phyphox_file(file_path):
    file_content = read_file(file_path)
    parsed_file_data = parse_phyphox_file_data(file_content)
    return parsed_file_data

def read_file(file_path):
    try:
        with open(file_path, 'r') as arquivo:
            return arquivo.read()
    except:
        raise ValueError('Caminho do arquivo inválido!')
    
def parse_file_data(file_content: str):
    replaced_file_content = file_content.replace(",", ".")
    lines = replaced_file_content.split('\n')
    
    t = []
    y = []
    v = []
    
    for line in lines:
        if (line.startswith('t')):
            continue
        numbers = line.split(';')
        if (len(numbers) != 3): # in case one of the columns doesn't have data for this line
            continue
        if ((numbers[0] != '') & (numbers[1] != '')):
            t.append(float(numbers[0]))
            y.append(float(numbers[1]))
            v.append(float(numbers[2]))
    return [t, y, v]

def parse_phyphox_file_data(file_content: str):
    lines = file_content.split('\n')
    
    t = []
    x = []
    y = []
    z = []
    a = []
    
    for line in lines:
        if (line.startswith('"')):
            continue
        numbers = line.split(',')
        if (len(numbers) != 5): # in case one of the columns doesn't have data for this line
            continue
        if ((numbers[0] != '') & (numbers[1] != '')):
            t.append(float(numbers[0]))
            x.append(float(numbers[1]))
            y.append(float(numbers[2]))
            z.append(float(numbers[3]))
            a.append(float(numbers[4]))
    return [t, x, y, z, a]

def create_output_dir(input_file_path: str) -> str:
    file_name = input_file_path.split('/')[:-1]
    file_str = file_name.split('.')[0]
    output_dir = 'parsed_data/' + file_str 
    os.makedirs(output_dir)
    return output_dir
