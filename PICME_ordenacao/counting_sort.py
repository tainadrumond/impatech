'''
Implementation of the Counting Sort algorithm (stable version).
This implementation suports the sorting of arrays of positive integers.
'''
import numpy as np

def counting_sort(arr):
    max_value = np.max(arr)
    count_arr = np.zeros(max_value+1, dtype=int)
    
    for num in arr:
        count_arr[num] += 1
    
    # from now on the code is meant to preserve stability
    for i in range(1, max_value+1):
        count_arr[i] += count_arr[i-1]
        
    output_arr = np.zeros(len(arr)+1, dtype=int)
    
    for num in reversed(arr):
        idx = count_arr[num]
        output_arr[idx] = num
        count_arr[num] -= 1
    
    return output_arr[1:]

if __name__ == "__main__":
    print(counting_sort([1,3,2,4,1,5]))