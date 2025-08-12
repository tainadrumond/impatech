import numpy as np

def counting_sort(arr, highest_place, place_to_sort: int):
    max_value = 9
    count_arr = np.zeros(max_value+1, dtype=int)
    
    for num in arr:
        count_arr[num[place_to_sort]] += 1
    
    for i in range(0, max_value+1):
        count_arr[i] += count_arr[i-1]
        
    output_arr = np.zeros((len(arr)+1, highest_place), dtype=object)
    
    for num in reversed(arr):
        idx = count_arr[num[place_to_sort]]
        output_arr[idx] = num.copy()
        count_arr[num[place_to_sort]] -= 1
    
    return output_arr[1:]

def radix_sort(arr):
    def get_highest_place(arr):
        max_value = np.max(arr)
        curr_value = max_value
        count = 0
        while curr_value != 0:
            curr_value = curr_value // 10
            count += 1
        return count
    
    def build_place_matrix(arr, highest_place):
        matrix = np.zeros((len(arr), highest_place), dtype=int)
        
        for i, num in enumerate(arr):
            curr_value = num
            count_places = 0
            while curr_value != 0:
                curr_place = curr_value % 10
                matrix[i][highest_place-count_places-1] = int(curr_place)
                curr_value = curr_value // 10
                count_places += 1
        
        return matrix
    
    highest_place = get_highest_place(arr)
    place_matrix = build_place_matrix(arr, highest_place)
    
    for i in range(highest_place-1,-1,-1):
        print(place_matrix)
        place_matrix = counting_sort(place_matrix, highest_place, i)
    
    return place_matrix
    
radix_sort([11111,112312,1233,1])