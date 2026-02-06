#Given an array arr[] denoting heights of n towers and a positive integer k.

def min_height(arr, k):
    n = len(arr)
    result = arr[-1]-arr[0]
    small = arr[0] + k
    big = arr[-1] - k
    if small > big:
        small, big = big, small
    for i in range(1, n):
        subtract = arr[i] - k
        add = arr[i] + k
        new_min = min(small, subtract)
        new_max = max(big, add)
        result = min(result, new_max - new_min)

    return result

print(min_height([1,5,8,10], 2))   # output = 5
print(min_height([3,9,12,16,20], 3))   # output = 11
