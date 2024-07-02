# EXERCÍCIO 1 - CÓDIGO 1
print("EXERCÍCIO 1")
def generate_points(begin, end, amount):
    '''
    Função que avalia o polinômio x^8-3x^4+2x^3-2x^2-x+2 para
    a quantidade de pontos dada por amount no intervalo [begin, end]
    '''
    points = []
    pace = (end-begin)/(amount-1) # Distância entre cada valor de x a ser avaliado
    for i in range(amount):
        x = begin+(i*pace) # Valor de x a ser avaliado
        y = (x**8)-3*(x**4)+2*(x**3)-2*(x**2)-x+2 # Resultado de x avaliado no polinômio x^8-3x^4+2x^3-2x^2-x+2
        points.append(str(x)+' '+str(y)) # Gera cada linha do arquivo no formato "x y"
    return '\n'.join(points) # Une as linhas com uma quebra de linha
    
points = generate_points(-3/2, 3/2, 1000) # Gera 1000 pontos no intervalo [-3/2,3/2]
f = open('points.txt', mode='w')
f.write(points) # Escreve os pontos gerados no arquivo
f.close()

# EXERCÍCIO 1 - CÓDIGO 2
import matplotlib.pyplot as plt
f = open('points.txt', mode='r')
text = f.read() # Lê o conteúdo do arquivo
f.close()

xs = []
ys = []
for line in text.split('\n'): # Percorre cada linha do arquivo
    coordinates = line.split(' ') # Separa as coordenadas x e y com base no formato do arquivo
    xs.append(float(coordinates[0]))
    ys.append(float(coordinates[1]))
plt.plot(xs, ys) # Passa as coordenadas x e y obtidas através do arquivo
plt.show()


# EXERCÍCIO 2
print("\nEXERCÍCIO 2")
def are_intervals_overlaid(interval1, interval2):
    '''
    Função que checa se os intervalos passados como parâmetro são sobrepostos
    '''
    begin_is_overlaid = interval1[0] <= interval2[0] and interval1[1] >= interval2[0] # Checa se o primeiro ponto do segundo intervalo está contido no primeiro intervalo
    end_is_overlaid = interval1[0] <= interval2[1] and interval1[1] >= interval2[1] # Checa se o último ponto do segundo intervalo está contido no primeiro intervalo
    return begin_is_overlaid or end_is_overlaid

def generate_smallest_container_range(intervals):
    '''
    Função que gera o menor intervalo que contém todos os intervalos passados como parâmetro
    '''
    left_bound = float('+inf') # Extremo esquerdo do intervalo
    right_bound = float('-inf') # Extremo direito do intervalo
    for i in intervals:
        if i[0] < left_bound:
            left_bound = i[0] # Salva o menor ponto como extremo esquerdo do intervalo
        if i[1] > right_bound:
            right_bound = i[1] # Salva o maior ponto como extremo diretiro do intervalo
    return [left_bound, right_bound]

def merge_intervals(intervals):
    '''
    Função que retorna o conjunto dos menores intervalos não sobrepostos 
    que contêm todos os intervalos dados como parâmetro
    '''
    merged_intervals = []
    for i in intervals:
        current_merged_intervals = [] # Conjunto dos intervalos mesclados após a iteração atual
        overlaid_intervals = [i] # Conjunto dos intervalos já avaliados que se tornam sobrepostos com o intervalo atual
        for m in merged_intervals:
            if are_intervals_overlaid(m, i): # Checa se o intervalo atual é sobreposto com algum dos intervalos já avaliados
                overlaid_intervals.append(m)
            else:
                current_merged_intervals.append(m) # Se o intervalo não é sobreposto com nenhum outro, ele é adicionado nos intervalos mesclados da iteração atual
        union_interval = generate_smallest_container_range(overlaid_intervals) # Gera a união dos intervalos sobrepostos
        current_merged_intervals.append(union_interval) # Adiciona a união dos intervalos sobrepostos nos intervalos mesclados da iteração atual
        merged_intervals = current_merged_intervals # Atualiza os intervalos mesclados com a iteração atual
        
    return merged_intervals

t = [[2,6], [1,3], [8,10], [15,18]]
print(merge_intervals(t))
t = [[1,4], [4,5]]
print(merge_intervals(t))
t = [[1, 10], [2, 3], [4, 7], [6, 11]]
print(merge_intervals(t))
t = [[1, 4]]
print(merge_intervals(t))

# EXERCÍCIO 3
print("\nEXERCÍCIO 3")
def missing_int(numbers):
    '''
    Função que implementa uma busca binária para encontrar o número ausente 
    na lista de inteiros ordenados dada como parâmetro.
    
    O critério de divisão da lista para a busca é dado pela discrepância entre
    o número de elementos no intervalo selecionado e a diferença entre o maior 
    e o menor número nesse intervalo. Essa discrepância indica a falta de um número 
    na sequência.
    '''
    left_bound = 0
    right_bound = len(numbers)-1

    while right_bound - left_bound > 1:
        middle_index = (left_bound+right_bound)//2 # Seleciona o elemento do meio do intervalo atual
        difference_of_elements_at_left = numbers[middle_index] - numbers[left_bound] # Diferença entre o maior e o menor número do intervalo à esquerda do elemento do meio
        number_of_elements_at_left = middle_index - left_bound # Número de elementos à esquerda do elemento do meio
        if difference_of_elements_at_left != number_of_elements_at_left: # Se há uma discrepância entre os valores, então o número faltante está à esquerda do elemento do meio
            right_bound = middle_index 
            continue
        
        difference_of_elements_at_right = numbers[right_bound] - numbers[middle_index] # Diferença entre o maior e o menor número do intervalo à direita do elemento do meio
        number_of_elements_at_right = right_bound - middle_index # Número de elementos à direita do elemento do meio
        if difference_of_elements_at_right != number_of_elements_at_right: # Se há uma discrepância entre os valores, então o número faltante está à direita do elemento do meio
            left_bound = middle_index
            continue
        return None # Se não há discrepância em nenhum dos dois intervalos, então não existe um número faltante
           
    return numbers[left_bound] + 1

l = [5, 6, 7, 8, 9, 12, 14]
print(missing_int(l))


# EXERCÍCIO 4
print("\nEXERCÍCIO 4")
def is_palindrome(linked_list):
    associated_list = [] # Lista que guarda os valores dos nós da lista encadeada
    node = linked_list.head
    while node is not None:
        associated_list.append(node.value) # Adiciona o valor de cada nó da lista encadeada na lista associada
        node = node.next
    
    is_valid_palindrome = True # Variável que guarda a validade da lista como palíndromo
    list_size = len(associated_list)
    for i in range(list_size//2):
        j = list_size-i-1 # Elemento correspondente ao índice i na lista inversa
        if associated_list[i] != associated_list[j]: # Se os elementos correspondentes são diferentes, então a lista não é um palíndromo
            is_valid_palindrome = False
            break
    
    return is_valid_palindrome # Será verdadeiro apenas se, após avaliar todos os elementos, nenhuma discrepância foi encontrada