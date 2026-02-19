#Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j]. 
#Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

def min_swaps(arr, k):
    n = len(arr)
    
    count = sum(1 for i in arr if i <= k)
    bad = sum(1 for i in range(count) if arr[i] > k)
    
    ans = bad
    
    for i in range(n - count):
        if arr[i] > k:
            bad -= 1
        if arr[i + count] > k:
            bad += 1
        ans = min(ans, bad)
    
    return ans


print(min_swaps([2, 1, 5, 6, 3], 3))  #output = 1
