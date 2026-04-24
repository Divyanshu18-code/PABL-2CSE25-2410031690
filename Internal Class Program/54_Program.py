#ou are given an array arr[ ], where arr[i] represents the height of the ith person standing in a line. A person i can see another person j if: 
#• height[j] < height[i], 
#• There is no person k standing between them such that height[k] ≥ height[i]. 

def max_visible(arr):
    n = len(arr)
    max_seen = 0

    for i in range(n):
        count = 1
        # left
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                count += 1
            else:
                break
        # right
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                count += 1
            else:
                break

        max_seen = max(max_seen, count)

    return max_seen

print(max_visible([6,2,5,4,5,1,6]))
print(max_visible([1,3,6,4]))