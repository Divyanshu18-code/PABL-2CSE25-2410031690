#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


print(two_sum([2, 7, 11, 15], 9))
