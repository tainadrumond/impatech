def nested_sum(nested_list):
    numbers_sum = 0
    for numbers_list in nested_list:
        for num in numbers_list:
            numbers_sum += num
    return numbers_sum

nested_list = [[1, 2], [3], [4, 5, 6]]
numbers_sum = nested_sum(nested_list)
print(numbers_sum)