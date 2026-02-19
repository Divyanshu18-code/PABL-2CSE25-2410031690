#Given an array arr[] of integers, calculate the median. 

def find_median(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


print(find_median([90, 100, 78, 89, 67]))  #output = 89
