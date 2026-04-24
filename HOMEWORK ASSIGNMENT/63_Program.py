#Given an array arr[] of time strings in 24-hour clock format "HH:MM:SS", return the minimum difference in seconds between any two time strings in the arr[]. 
#The clock wraps around at midnight, so the time difference between "23:59:59" and "00:00:00" is 1 second. 

def time_to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h*3600 + m*60 + s

def min_diff(arr):
    times = sorted([time_to_sec(t) for t in arr])
    res = float('inf')
    
    for i in range(len(times)):
        diff = (times[(i+1) % len(times)] - times[i]) % (24*3600)
        res = min(res, diff)
    
    return res

# Example
print(min_diff(["00:00:01", "23:59:59", "00:00:05"]))  # Output: 2