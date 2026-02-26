#You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0. 

def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps

print(jump( [2,3,1,1,4]))  #output = 2