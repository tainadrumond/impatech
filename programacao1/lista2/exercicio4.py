def minus_num(nums: list, num_to_subtract: float):
    result = []
    for num in nums:
        # guarda em result todos os números subtraídos pelo número dado
        result.append(num-num_to_subtract)
    return result

subtracted_list = minus_num([.5, .25, .5, .25, 1.5, 0], 0.5)
print(subtracted_list)