import numpy as np
import random

def get_highest_order(arr):
    highest = -1
    
    for num in arr:
        curr_value = num
        count_orders = 0
        while curr_value != 0:
            curr_value = curr_value // 10
            count_orders += 1
        
        if count_orders > highest:
            highest = count_orders
    
    return highest

def create_order_matrix(arr, highest_order):
    matrix = np.zeros((len(arr), highest_order))
    
    for i, num in enumerate(arr):
        curr_value = num
        count_orders = 0
        while curr_value != 0:
            curr_order = curr_value % 10
            matrix[i][highest_order-count_orders-1] = int(curr_order)
            curr_value = curr_value // 10
            count_orders += 1
    
    return matrix

def create_order_dict(arr):
    highest_order = get_highest_order(arr)
    order_matrix = create_order_matrix(arr, highest_order)
    order_dict = {}
    
    for i in range(highest_order-1):
        for alg in range(10):
            for num in order_matrix:
                curr_order = num[i]
                
                if curr_order != alg:
                    continue 
                
                curr_dict = order_dict
                for j in range(i):
                    curr_dict = curr_dict[int(num[j])]
                if alg not in curr_dict:
                    curr_dict[alg] = {}
    
    for alg in range(10):
            for i, num in enumerate(order_matrix):
                curr_order = num[highest_order-1]
                if curr_order != alg:
                    continue
                
                curr_dict = order_dict
                for j in range(highest_order-1):
                    curr_dict = curr_dict[int(num[j])]
                if alg not in curr_dict:
                    curr_dict[alg] = [arr[i]]
                else:
                    curr_dict[alg].append(arr[i])
    
    return order_dict

sorted_array = []
def order_dict_to_sorted_array(dict):
    def dive_into_dict(dict):
        global sorted_array
        if isinstance(dict, list):
            sorted_array += dict
            return
        for key in dict.keys():
            order_dict_to_sorted_array(dict[key])
    dive_into_dict(dict)
    return sorted_array

arr = [random.randint(1, 1000) for _ in range(10)]
print(arr)
order_dict = create_order_dict(arr)
sorted_array = order_dict_to_sorted_array(order_dict)
print(sorted_array)