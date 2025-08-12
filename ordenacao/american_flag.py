import numpy as np
from collections import defaultdict

def count_keys(arr, char_chain, idx):
    count = defaultdict(int, {k:0 for k in [-1]+char_chain})
    for el in arr:
        if len(el) < idx:
            count[el[idx]] += 1
        else:
            count[-1] += 1
    
    sum = 0
    for key in count.keys():
        aux = count[key]
        count[key] = sum
        sum += aux

def american_flag(arr, char_chain):
    def sort_aux(idx, begin, end):
        keys_count = count_keys(arr, char_chain, idx)
        
        for i in range(begin, end):
            el = arr[i]
            
            destiny = 0
            if len(el) < idx:
                destiny = keys_count[el[idx]]
            else:
                destiny = keys_count[-1]
                
            pos = keys_count[destiny]
            temp = arr[pos]
            arr[pos] = el
            arr[i] = temp
            keys_count[destiny] += 1
    
    sort_aux(0)
    
american_flag(['abc', 'abc', 'bca'], ['a', 'b', 'c'])