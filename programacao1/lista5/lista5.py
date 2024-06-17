# EXERCÍCIO 1
print("EXERCÍCIO 1")
class Node():
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node
    
class Linked_List():
    def __init__(self, head):
        self.head = head
    
    def add_node(self, value):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value, None) # Adiciona o elemento como o próximo do node que aponta para None (o último da lista)
    
    def inverte_ordem(self):
        '''
        Cria uma nova lista com a ordem invertida do objeto em que foi chamado em tempo O(n)
        '''
        if self.head is None:
            return Linked_List(None)
        
        next = self.head.next # O próximo node se tornará o anterior na lista invertida
        current = Node(self.head.value, None)
        while next is not None:
            current = Node(next.value, current) # Cria um node que guarda o valor do próximo node e aponta para o node atual, invertendo a ordem da lista
            next = next.next
        return Linked_List(current) # Retorna a lista invertida, na qual o último node criado é a cabeça

    def __str__(self):
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.value))
            node = node.next
        values.append('None')
        return '->'.join(values)
        
head = Node(1, None)
linked_list = Linked_List(head)
linked_list.add_node(5)
linked_list.add_node(2)
linked_list.add_node(4)
print("Lista original:", linked_list)
inverted_list = linked_list.inverte_ordem()
print("Lista invertida:", inverted_list)

linked_list = Linked_List(None)
print("\nLista original:", linked_list)
inverted_list = linked_list.inverte_ordem()
print("Lista invertida:", inverted_list)

linked_list = Linked_List(Node(3, None))
print("\nLista original:", linked_list)
inverted_list = linked_list.inverte_ordem()
print("Lista invertida:", inverted_list)



# EXERCÍCIO 2
print("\n\nEXERCÍCIO 2")
class Roman_Numeral_Order(): # Classe que guarda as representações de uma ordem numérica em números romanos
    def __init__(self, unity, five_unities, ten_unities):
        self.unity = unity
        self.five_unities = five_unities
        self.ten_unities = ten_unities
    
    def get_order_representation(self, numeral):
        # Casos de representação com subtração de unidades (4 e 9): 
        if numeral == 9:
            return self.unity + self.ten_unities
        if numeral == 4:
            return self.unity + self.five_unities
        
        # Casos de representação com adição de unidades (diferentes de 4 e 9):
        result = self.five_unities if numeral >= 5 else ''
        result += self.unity * (numeral % 5)
        return result
            
def to_roman_numeral(number):
    unities = Roman_Numeral_Order('I', 'V', 'X')
    tens = Roman_Numeral_Order('X', 'L', 'C')
    hundreds = Roman_Numeral_Order('C', 'D', 'M')
    thousands = Roman_Numeral_Order('M', '', '')
    orders_representation = [unities, tens, hundreds, thousands]
    
    number_str = str(number)
    str_len = len(number_str)
    result = ''
    for i in range(str_len):
        # Percorre os algarismos começando do último na string (algarismo das unidades)
        current_numeral = int(number_str[str_len-i-1])
        representation = orders_representation[i].get_order_representation(current_numeral) # Pega a representação correspondente à ordem numérica do algarismo
        result = representation + result
    return result

print("1:", to_roman_numeral(1))
print("3999:", to_roman_numeral(3999))
print("4:", to_roman_numeral(4))
print("9:", to_roman_numeral(9))
print("1666:", to_roman_numeral(1666))
print("1994:", to_roman_numeral(1994))
print("30:", to_roman_numeral(30))
print("3000:", to_roman_numeral(3000))


# EXERCÍCIO 3
print("\n\nEXERCÍCIO 3")
# LETRA A
print("(a)")
def potencia(x, n):
    result = 1
    abs_n = abs(n)
    for i in range(abs_n):
        result *= x
        
    if n < 0:
        return 1/result
    return result

print("2^5 =", potencia(2, 5))
print("2^(-2) =", potencia(2, -2))
print("3^3 =", potencia(3, 3))
print("473^0 =", potencia(473, 0))
print("0^2 =", potencia(0, 2))
print("1^10000 =", potencia(1, 10000))

# LETRA B
print("\n(b)")
def potencia_b(x, n):
    '''
    Função que escreve n como uma soma de potências de 2 
    e calcula x elevado a cada uma dessas potências separadamente em tempo log(n)
    '''
    abs_n = abs(n)
    n_reverse_binary = ''
    # Escreve n em sua representação em binário de trás para frente (para determinar as somas de potências de 2 equivalentes a n):
    while abs_n != 0:
        n_reverse_binary += str(abs_n % 2)
        abs_n //= 2
        
    power = 1
    result = 1
    # Calcula x elevado a cada uma das potências de 2, utilizando a representação em binário de n como referência:
    for i in n_reverse_binary:
        if power == 1:
            power = x
        else:
            power *= power
        if i == '1':
            # Multiplica os resultados de x elevado às potências de 2 correspondentes às casas com algarismo 1 na representação em binário de n:
            result *= power
    
    if n < 0:
        return 1/result
    return result

print("2^5 =", potencia_b(2, 5))
print("2^(-2) =", potencia_b(2, -2))
print("3^3 =", potencia_b(3, 3))
print("473^0 =", potencia_b(473, 0))
print("0^2 =", potencia_b(0, 2))
print("1^10000 =", potencia_b(1, 10000))

# EXERCÍCIO 4
print("\n\nEXERCÍCIO 4")
def find_unique_number(numbers):
    unique_numbers_dict = {} # Dicionário que guarda os números que só apareceram uma única vez em numbers
    for n in numbers:
        if unique_numbers_dict.get(n) is None:
            unique_numbers_dict[n] = 1
        else: # Se o elemento já estava no dicionário, então ele é duplicado
            unique_numbers_dict.pop(n) # Remove o elemento duplicado
    return list(unique_numbers_dict.keys())[0]

print("Número único de [1, 2, 3, 4, 1, 3, 4]:", find_unique_number([1, 2, 3, 4, 1, 3, 4]))
print("Número único de [4, 3, 2, 4, 1, 3, 2]:", find_unique_number([4, 3, 2, 4, 1, 3, 2]))
print("Número único de [2, 2, 1]:", find_unique_number([2, 2, 1]))
print("Número único de [99]:", find_unique_number([99]))
print("Número único de [5, 4, 4, 6, 6]:", find_unique_number([5, 4, 4, 6, 6]))

# EXERCÍCIO 5
# A complexidade do algoritmo a seguir é O(nm), onde n é o número de strings e m é o tamanho da menor string da lista
print("\n\nEXERCÍCIO 5")
def longest_common_prefix(strings):
    result = ''
    if len(strings) == 0:
        return result
    for i in range(len(strings[0])):
        letter = strings[0][i]
        for string in strings:
            try:
                if string[i] != letter: # Checa se a letra nessa posição é igual para todas as strings da lista
                    return result
            except IndexError: # Ultrapassou o tamanho de uma das strings. A partir desse ponto, o prefixo deixaria de ser o mesmo para essa string
                return result
        result += letter # Se essa letra é comum a todas as strings na posição i, então adiciona ela no resultado
    return result

print("['flower', 'flow', 'flight']:", longest_common_prefix(['flower', 'flow', 'flight']))
print("['test', 'test', 'test']:", longest_common_prefix(['test', 'test', 'test']))
print("['a', 'ab', 'abc']:", longest_common_prefix(['a', 'ab', 'abc']))
print("['abc', 'bcd', 'cde']:", longest_common_prefix(['abc', 'bcd', 'cde']))
print("[]:", longest_common_prefix([]))
print("['flower']:", longest_common_prefix(['flower']))
              
        
