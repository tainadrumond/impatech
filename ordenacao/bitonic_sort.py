'''
Bitonic sort for lists of 2^k elements. 
'''
import numpy as np

def bitonic_merge(increasing_arr, decreasing_arr, level):
    k = len(increasing_arr)
    for i in range(k):
        if increasing_arr[i] > decreasing_arr[i+k]:
            increasing_arr[i], decreasing_arr[i+k] = decreasing_arr[i+k], increasing_arr[i]
    if level == 2:
        return increasing_arr + decreasing_arr
    else:
        res = []
        new_level = level/2
        # res += 
         
        bitonic_merge(increasing_arr)
    