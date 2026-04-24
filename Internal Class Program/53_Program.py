#You are given an array arr[]. The task is to determine whether the array contains a 132 pattern, i.e., three indices i,  j and k such that i < j < k , arr[i] < arr[j] > 
#arr[k] and arr[i] < arr[k]. 

def find132(arr):
    stack = []
    third = float('-inf')

    for num in reversed(arr):
        if num < third:
            return True
        while stack and stack[-1] < num:
            third = stack.pop()
        stack.append(num)

    return False

print(find132([4,7,11,5,13,2]))
print(find132([11,11,12,9]))