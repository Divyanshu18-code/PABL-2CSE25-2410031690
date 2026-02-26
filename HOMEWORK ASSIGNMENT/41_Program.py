#Given an integer array nums of unique elements, return all possible subsets (the power set). 

def subsets(nums):
    result = [[]]
    
    for num in nums:
        result += [curr + [num] for curr in result]
    
    return result

print(subsets([1,2,3]))  #output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]