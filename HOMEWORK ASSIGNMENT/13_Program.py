#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position. 

def min_jumps(arr):
    n = len(arr)

    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    
    maxReach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n):
        if i == n -1:
            return jump
        maxReach = max(maxReach, i + arr[i])
        step -= 1

        if step == 0:
            jump += 1
            if i >= maxReach:
                return -1
            step = maxReach - 1
    return -1


print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))   # output = 3
print(min_jumps([1, 4, 3, 2, 6, 7]))   # output = 2
print(min_jumps([0, 10, 20]))   # output = -1