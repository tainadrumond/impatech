def sum_cummulative(numbers_list):
    sum = 0
    sums_list = []
    for num in numbers_list:
        sum += num
        sums_list.append(sum)
    return sums_list

numbers_list = [-2 , 3 , 4 , -1, 1]
sums_list = sum_cummulative(numbers_list)
print(sums_list)

        