def two_sum(nums: list, target: int):
    nums_length = len(nums)
    for i in range(0, nums_length):
        for j in range(i+1, nums_length): #itera por todos os números depois de i
            if (nums[i]+nums[j] == target):
                # retorna os índices dos primeiros elementos cuja soma seja o alvo
                return [i, j]

indexes = two_sum([7, 3, 5, 2, 11, 15], 9)
print(indexes)