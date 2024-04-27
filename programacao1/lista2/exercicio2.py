def two_sum(nums: list, target: int):
    nums_length = len(nums)
    r = range(0, nums_length)
    for i in r:
        r2 = range(i+1, nums_length)
        for j in r2:
            if (nums[i]+nums[j] == target):
                return [i, j]

indexes = two_sum([7, 3, 5, 2, 11, 15], 9)
print(indexes)