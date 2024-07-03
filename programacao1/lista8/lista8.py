# EXERCÍCIO 1
print("EXERCÍCIO 1:")
def merge_reversed_lists(list1: list[float], list2: list[float]) -> list[float]:
    '''
    Une duas listas ordenadas em ordem decrescente em outra lista ordenada em ordem
    decrescente em tempo O(n+m), onde n e m são o tamanho de cada uma das listas
    '''
    i = 0
    j = 0
    merged_lists = []
    list1_size = len(list1)
    list2_size = len(list2)
    while i < list1_size or j < list2_size: # Itera enquanto ainda não percorreu todos os elementos das duas listas
        if j == list2_size or (i < list1_size and list1[i] >= list2[j]): # Se atingiu o último elemento da lista 2 ou se o elemento atual da lista 1 é maior
            merged_lists.append(list1[i])
            i += 1
        else: # Se atingiu o último elemento da lista 1 ou se o elemento atual da lista 2 é maior
            merged_lists.append(list2[j])
            j += 1
    return merged_lists

list1 = [10, 8, 6, 4, 3, 2, -1]
list2 = [11, 9, 7, 5]
print(merge_reversed_lists(list1, list2))
list1 = []
list2 = [11, 9, 7, 5]
print(merge_reversed_lists(list1, list2))
list1 = [3, 2, -1]
list2 = []
print(merge_reversed_lists(list1, list2))


# EXERCÍCIO 2
print("\nEXERCÍCIO 2")
def is_in_previous_elements(element: int, elements: list[int], previous_elements_to_check: int) -> bool:
    '''
    Checa se o elemento passado como parâmetro é igual a algum dos últimos K elementos
    da lista passada. O inteiro K é determinado pelo parâmetro previous_elements_to_check
    '''
    i = len(elements) - 1 # Index de um elemento a ser checado, começando do último
    lim = len(elements) - previous_elements_to_check # Index do primeiro elemento a ser checado 
    while i >= 0 and i >= lim:
        if elements[i] == element: # Compara se é igual a um dos últimos elementos a serem checados 
            return True
        i -= 1
    return False
    
def buy_clothes(number_of_items: int, previous_items_to_check: int, items: list[int]):
    purchased_items = [] # Itens válidos a serem comprados
    for item in items:
        if not is_in_previous_elements(item, purchased_items, previous_items_to_check): # Compara se é igual a um dos últimos itens já comprados a serem checados
            purchased_items.append(item) # Se não for igual a um dos últimos elementos, então é válido para ser comprado
    return len(purchased_items) # Retorna o número de itens a serem comprados

print(buy_clothes(5, 2, [1, 1, 1, 1, 1]))
print(buy_clothes(5, 2, [1, 2, 3, 1, 1]))
print(buy_clothes(5, 2, [1, 2, 3, 1, 2]))
print(buy_clothes(5, 2, [1, 2, 3, 4, 5]))


# EXERCÍCIO 3
print("\nEXERCÍCIO 3")
def validade_parenthesis(text: str) -> bool:
    '''
    Compara se o número total de parêntesis abertos na string
    é igual ao número total de parêntesis fechados e valida se
    em nenhum momento existem mais parêntesis fechados do que abertos.
    '''
    opened = 0 # Número de parêntesis abertos
    for char in text:
        if char == '(':
            opened += 1
        if char == ')':
            opened -= 1
            if opened == -1: # Se tem mais parêntesis fechados do que abertos, então a string é inválida
                return False
    
    return opened == 0 # Compara se o número total de parêntesis abertos na string é igual ao número total de parêntesis fechados

text = "A reunião (que estava marcada para sexta-feira) foi adiada."
print(text, validade_parenthesis(text))
text = "Comprei frutas (maçãs, bananas (e laranjas)) ontem."
print(text, validade_parenthesis(text))
text = "(Ela) mencionou que estava cansada (mas continuou trabalhando)."
print(text, validade_parenthesis(text))
print()
text = "A reunião (que estava marcada para sexta-feira (às 14h) foi adiada."
print(text, validade_parenthesis(text))
text = "Comprei frutas (maçãs, bananas (e laranjas ontem."
print(text, validade_parenthesis(text))
text = "Ela mencionou (que estava cansada (mas continuou trabalhando)."
print(text, validade_parenthesis(text))
