def average(nums: list):
    sum = 0
    for num in nums:
        sum += num
    size = len(nums)
    return sum/size

def minus_num(nums: list, num_to_subtract: float):
    result = []
    for num in nums:
        result.append(num-num_to_subtract)
    return result      

def std_deviation(nums: list):
    avrg = average(nums)
    subtracted_nums = minus_num(nums, avrg)
    sum = 0
    for num in subtracted_nums:
        sum += num**2
    return (sum/len(subtracted_nums))**(1/2)

std_dvtn = std_deviation([.5, .25, .5, .25, 1.5, 0])
print(std_dvtn)