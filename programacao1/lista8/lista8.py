# EXERCÍCIO 1
print("EXERCÍCIO 1:")
def merge_reversed_lists(list1: list[float], list2: list[float]) -> list[float]:
    i = 0
    j = 0
    merged_lists = []
    list1_size = len(list1)
    list2_size = len(list2)
    while i < list1_size or j < list2_size:
        if j == list2_size or (i < list1_size and list1[i] >= list2[j]):
            merged_lists.append(list1[i])
            i += 1
        else:
            merged_lists.append(list2[j])
            j += 1
    return merged_lists

list1 = [10, 8, 6, 4, 3, 2, -1]
list2 = [11, 9, 7, 5]
print(merge_reversed_lists(list1, list2))


# EXERCÍCIO 2
print("\nEXERCÍCIO 2")
# def buy_clothes(number_of_items: int, number_of_repetitions: int, items: list[int]):


# EXERCÍCIO 3
print("\nEXERCÍCIO 3")
def validade_parenthesis(text: str) -> bool:
    opened = 0
    for char in text:
        if char == '(':
            opened += 1
        if char == ')':
            opened -= 1
            if opened == -1:
                return False
    if opened > 0:
        return False
    
    return True

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
