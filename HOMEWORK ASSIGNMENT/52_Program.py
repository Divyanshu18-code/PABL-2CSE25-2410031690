#You are given an integer array arr[ ]. Your task is to count the number of subarrays where the first element is the minimum element of that subarray. 

def count_subarrays(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        min_val = arr[i]
        for j in range(i, n):
            if arr[j] < min_val:
                break
            count += 1

    return count

print(count_subarrays([1,2,1]))
print(count_subarrays([1,3,5,2]))