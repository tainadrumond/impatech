# EXERCÍCIO 1
print("EXERCÍCIO 1")
def search_insert(ord_list: list, value: int) -> int:
    '''
    Função que implementa uma busca binária para retornar o índice de
    um valor na lista recebida em tempo O(log(n))
    '''
    left_bound = 0
    right_bound = len(ord_list)-1
    current_index = (left_bound + right_bound)//2
    
    while left_bound != right_bound and ord_list[current_index] != value:
            if (ord_list[current_index] < value):
                left_bound = current_index+1
            elif (ord_list[current_index] > value):
                right_bound = current_index-1
            current_index = (left_bound+right_bound)//2
    return current_index

t = [0, 2, 3, 4, 7]
print(t)
print("Posição de 5:", search_insert(t, 5))
print("Posição de 2:", search_insert(t, 2))


# EXERCÍCIO 2
print("\nEXERCÍCIO 2")
def build_pascal_triangle(n: int) -> list:
    '''
    Constrói o Triângulo de Pascal de n linhas em tempo O(n²)
    '''
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        previous_line = triangle[i-1]
        new_line = [1] # Adiciona o 1 da borda esquerda da linha
        for j in range(len(previous_line)-1):
            term1 = previous_line[j]
            term2 = previous_line[j+1]
            new_line.append(term1+term2) # Adiciona a soma dos dois números acima
        new_line.append(1) # Adiciona o 1 da borda direita da linhaS
        triangle.append(new_line)
    return triangle
            
print(build_pascal_triangle(7))


# EXERCÍCIO 3
print("\nEXERCÍCIO 3")
class List_Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_List():
    def __init__(self, head: List_Node):
        self.head = head
        
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        self.length = length
    
    def delete_node(self, value):
        if self.head is None:
            return
        if self.head.val == value:
            self.head = self.head.next
            return
        
        previous = self.head
        current = self.head.next
        while current is not None:
            if current.val == value:
                previous.next = current.next
            previous = current
            current = current.next
            
    def copy(self):
        '''
        Returns a copy of the linked list
        '''
        if self.head is None:
            return Linked_List(None)
        
        new_head = List_Node(self.head.val)
        new_node = new_head
        self_node = self.head.next
        
        while self_node is not None:
            new_node.next = List_Node(self_node.val)
            new_node = new_node.next
            self_node = self_node.next
            
        return Linked_List(new_head)
        
    def __add__(self, other_list):
        self_copy = self.copy()
        other_copy = other_list.copy()
        
        # Se uma das listas for vazia, retorna a outra como resultado:
        if self_copy.head is None:
            return other_copy
        elif other_copy.head is None:
            return self_copy
        
        node = self_copy.head
        while node.next is not None:
            node = node.next
        node.next = other_copy.head # Adiciona a cópia de other_list no fim da cópia da lista atual
        
        new_list = Linked_List(self_copy.head) # Cria um novo objeto para que o tamanho da lista resultante seja calculado pelo construtor
        return new_list
        
    def __str__(self):
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.val))
            node = node.next
        values.append('None')
        return '->'.join(values)

n1 = List_Node(4)
n2 = List_Node(3, n1)
n3 = List_Node(2, n2)
n4 = List_Node(1, n3)
l1 = Linked_List(n4)
print("Lista 1:", l1)
l1.delete_node(2)
print("Lista 1 sem o 2:", l1)

n5 = List_Node(8)
n6 = List_Node(7, n5)
n7 = List_Node(6, n6)
n8 = List_Node(5, n7)
l2 = Linked_List(n8)
print("Lista 2:", l2)

l3 = l1 + l2
print("Lista 1 + Lista 2:", l3)


# EXERCÍCIO 4
print("\nEXERCÍCIO 4")
def add_polynomial_term_to_dict(term: str, poly_dict: dict):
    if term == "":
        return
    
    if 'x' not in term: # Trata o caso do termo de grau 0 com o 'x^0' implícito
        coefficient = int(term)
        exponent = 0
    elif '^' not in term: # Trata o caso do termo de grau 1 com '^1' implícito
        term_without_x = term[:-1] # Retira o x do fim da string
        coefficient_is_explicit_number = len(term_without_x) != 0 and term_without_x != '+' and term_without_x != '-'
        coefficient = int(term_without_x) if coefficient_is_explicit_number else 1  # Trata o caso do coeficiente '1' implícito
        exponent = 1
    else: # Trata dos casos com o expoente explícito
        numerical_entries = term.split('x^') # Usa o termo 'x^' como separador para obter o coeficiente e o expoente
        if len(numerical_entries) == 2:
            coefficient_is_explicit_number = numerical_entries[0] != '+' and numerical_entries[1] != '-'
            coefficient = int(numerical_entries[0]) if coefficient_is_explicit_number else 1 # Pega o coeficiente e trata o caso do coeficiente '1' implícito
            exponent = int(numerical_entries[1])
        else:
            coefficient = 1 # Caso do coeficiente 1 implícito
            exponent = int(numerical_entries[0])
    
    if poly_dict.get(exponent) is None:
        poly_dict[exponent] = coefficient
    else:
        poly_dict[exponent] += coefficient
    
def polynomial_str_to_dict(polynomial: str) -> dict:
    poly_dict = {}
    current_term = ""
    for i in polynomial:
        if i == '+' or i == '-': # Adiciona o último termo no dicionário e inicia a obtenção do próximo termo
            add_polynomial_term_to_dict(current_term, poly_dict)
            current_term = i
        else:
            current_term += i
    add_polynomial_term_to_dict(current_term, poly_dict) # Adiciona o último termo (que não tem os separadores '+' ou '-' depois dele)
    return poly_dict

poly_dict = polynomial_str_to_dict("2x^3+x^2-4x+5")
print(poly_dict)

# EXERCÍCIO 5
print("\nEXERCÍCIO 5")
def polynomial_dict_to_str(polynomial: dict) -> str:
    exponents = sorted(list(polynomial.keys()), reverse=True)
    poly_str = ""
    for exponent in exponents:
        coefficient = polynomial[exponent]
        
        # Trata do coeficiente:
        if coefficient == 0:
            continue
        poly_str += '+' if coefficient > 0 else '-'
        absolute_value = abs(coefficient)
        if absolute_value != 1:
            poly_str += str(absolute_value)
        
        # Trata do expoente:
        if exponent == 0:
            continue
        poly_str += 'x'
        if exponent == 1:
            continue
        poly_str += f"^{exponent}"
        
    if poly_str[0] == '+':
        poly_str = poly_str[1:]
    return poly_str

print(polynomial_dict_to_str(poly_dict))
        
            
        
            
        

            
    