#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case. 

def smallest_subarray(x, arr):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return 0 if min_len == n + 1 else min_len

print(smallest_subarray(51, [1, 4, 45, 6, 0, 19]))  #output = 3 