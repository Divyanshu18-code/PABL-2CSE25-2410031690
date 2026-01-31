# Given an array arr, rotate the array by one position in clockwise direction.

def rotate_by_one(arr):
    n = len(arr)
    list = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = list
    return arr

print(rotate_by_one([1, 2, 3, 4, 5]))