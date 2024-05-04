def average(nums: list):
    sum = 0
    for num in nums: # soma todos os números da lista na variável sum
        sum += num
    size = len(nums)
    return sum/size

avrg = average([.5, .25, .5, .25, 1.5, 0])
print(avrg)