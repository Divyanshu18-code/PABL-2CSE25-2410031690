#ou are given an integer array arr[ ]. For every element in the array, your task is to determine its Previous Smaller Element (PSE). 

def previous_smaller(arr):
    stack = []
    result = []

    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(x)

    return result


print(previous_smaller([1,6,2]))
print(previous_smaller([1,5,0,3,4,5]))