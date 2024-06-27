# EXERCÍCIO 1 - CÓDIGO 1
# print("EXERCÍCIO 1")
# def generate_points(begin, end, amount):
#     points = []
#     pace = (end-begin)/(amount-1)
#     for i in range(amount):
#         x = begin+(i*pace)
#         y = (x**8)-3*(x**4)+2*(x**3)-x+2
#         points.append(str(x)+' '+str(y))
#     return '\n'.join(points)
    
# points = generate_points(-3/2, 3/2, 1000)
# f = open('points.txt', mode='w')
# f.write(points)
# f.close()

# # EXERCÍCIO 1 - CÓDIGO 2
# import matplotlib.pyplot as plt
# f = open('points.txt', mode='r')
# text = f.read()
# f.close()
# xs = []
# ys = []
# for line in text.split('\n'):
#     coordinates = line.split(' ')
#     xs.append(float(coordinates[0]))
#     ys.append(float(coordinates[1]))
# plt.plot(xs, ys)
# plt.show()


# EXERCÍCIO 2
print("\nEXERCÍCIO 2")
def are_intervals_overlaid(interval1, interval2):
    '''
    Função que checa se os intervalos passados como
    parâmetro são sobrepostos
    '''
    begin_is_overlaid = interval1[0] <= interval2[0] and interval1[1] >= interval2[0]
    end_is_overlaid = interval1[0] <= interval2[1] and interval1[1] >= interval2[1]
    return begin_is_overlaid or end_is_overlaid

def generate_smallest_container_range(intervals):
    '''
    Função que gera o menor intervalo que contém todos os 
    intervalos passados como parâmetro
    '''
    left_bound = float('+inf')
    right_bound = float('-inf')
    for i in intervals:
        if i[0] < left_bound:
            left_bound = i[0]
        if i[1] > right_bound:
            right_bound = i[1]
    return [left_bound, right_bound]

def merge_intervals(intervals):
    merged_intervals = []
    for i in intervals:
        current_merged_intervals = []
        overlaid_intervals = [i]
        for m in merged_intervals:
            if are_intervals_overlaid(m, i):
                overlaid_intervals.append(m)
            else:
                current_merged_intervals.append(m)
        resultant_interval = generate_smallest_container_range(overlaid_intervals)
        current_merged_intervals.append(resultant_interval)
        merged_intervals = current_merged_intervals
        
    return merged_intervals

t = [[2,6], [1,3], [8,10], [15,18]]
print(merge_intervals(t))
t = [[1,4], [4,5]]
print(merge_intervals(t))
t = [[1, 10], [2, 3], [4, 7], [6, 11]]
print(merge_intervals(t))


# EXERCÍCIO 3
print("\nEXERCÍCIO 3")
def missing_int(numbers):
    '''
    Função que implementa uma busca binária para encontrar o
    número ausente em uma lista ordenada de inteiros.
    '''
    left_bound = 0
    right_bound = len(numbers)-1

    while right_bound - left_bound > 1:
        middle_index = (left_bound+right_bound)//2
        left_numbers_distance = numbers[middle_index] - numbers[left_bound]
        left_indexes_distance = middle_index - left_bound
        if left_numbers_distance != left_indexes_distance:
            right_bound = middle_index
            continue
        right_numbers_distance = numbers[right_bound] - numbers[middle_index]
        right_indexes_distance = right_bound - middle_index
        if right_numbers_distance != right_indexes_distance:
            left_bound = middle_index
            continue
        return None
           
    return numbers[left_bound] + 1

l = [5, 6, 7, 8, 9, 12, 14]
print(missing_int(l))


# EXERCÍCIO 4
print("\nEXERCÍCIO 4")
def is_palindrome(linked_list):
    associated_list = []
    node = linked_list.head
    while node is not None:
        associated_list.append(node.value)
        node = node.next
    
    is_valid = True
    list_size = len(associated_list)
    for i in range(list_size):
        j = list_size-i-1
        if associated_list[i] != associated_list[j]:
            is_valid = False
            break
    
    return is_valid
    
        

        

        



