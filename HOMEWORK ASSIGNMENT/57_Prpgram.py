#Given an array arr[] of integers and an integer k, select k elements from the array such that the minimum absolute difference between any two of the selected elements 
#is maximized. Return this maximum possible minimum difference. 

def max_min_diff(arr, k):
    arr.sort()

    def possible(mid):
        count = 1
        prev = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - prev >= mid:
                count += 1
                prev = arr[i]
        return count >= k

    low, high = 0, arr[-1] - arr[0]
    ans = 0

    while low <= high:
        mid = (low + high)//2
        if possible(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

print(max_min_diff([2,6,2,5], 3))
print(max_min_diff([1,4,9,0,2,13,3], 4))