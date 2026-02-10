#Given an array arr[] with non-negative integers representing the height of blocks.If the width of each block is 1,compute how much water can be trapped between the blocks during the rainy season.  

def trap_water(arr):
    n = len(arr)
    
    left_max = [0]*n
    right_max = [0]*n
    
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])
    
    right_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])
    
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]
    
    return water


print(trap_water([3, 0, 1, 0, 4, 0, 2]))  # output = 
print(trap_water([3, 0, 2, 0, 4]))  # output = 