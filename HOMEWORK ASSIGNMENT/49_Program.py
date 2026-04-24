#You are given an array arr[] of size n , where arr[i] denotes the range of working hours a person at position i can cover. 
#• If arr[i] ≠ -1, the person at index i can work and cover the time interval [i - arr[i], i + arr[i]]. 
#• If arr[i] = -1, the person is unavailable and cannot cover any time.

def min_people(arr):
    n = len(arr)
    intervals = []

    for i in range(n):
        if arr[i] != -1:
            l = max(0, i - arr[i])
            r = min(n-1, i + arr[i])
            intervals.append((l, r))

    intervals.sort()

    count = 0
    i = 0
    curr_end = 0
    max_end = 0

    while curr_end < n:
        while i < len(intervals) and intervals[i][0] <= curr_end:
            max_end = max(max_end, intervals[i][1])
            i += 1

        if max_end == curr_end:
            return -1

        count += 1
        curr_end = max_end + 1

    return count

print(min_people([1,2,1,0]))
print(min_people([2,3,4,-1,2,0,0,-1,0]))