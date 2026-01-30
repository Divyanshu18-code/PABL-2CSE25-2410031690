#You are given an array of integers arr[]. You have to reverse the given array.

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

print(reverse_array([1,4,3,2,6,5]))