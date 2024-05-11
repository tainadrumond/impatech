import os

def read_graphs_file(file_path):
    file_content = read_file(file_path)
    parsed_file_data = parse_file_data(file_content)
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
    
    for line in lines:
        if (line.startswith('t')):
            continue
        numbers = line.split('	')
        if (len(numbers) != 2): # in case one of the data columns doesn't have value for this line
            continue
        if ((numbers[0] != '') & (numbers[1] != '')):
            t.append(float(numbers[0]))
            y.append(float(numbers[1]))
    return [t, y]
        
        
    
    # for linha in arquivo:
            #     if (linha.startswith('t')):
            #         continue
            #     values = linha.split('	')
            #     t.append(float(values[0]))
            #     x.append(float(values[1].removesuffix('\n')))

def create_output_dir(input_file_path: str) -> str:
    file_name = input_file_path.split('/')[:-1]
    file_str = file_name.split('.')[0]
    output_dir = 'parsed_data/' + file_str 
    os.makedirs(output_dir)
    return output_dir
