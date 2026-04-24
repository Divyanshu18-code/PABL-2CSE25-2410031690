# Given a sorted array arr[] containing distinct non negative integers that has been rotated at some unknown pivot, and a value x. Your task is to count the number of 
# elements in the array that are less than or equal to x. 

def count_less_equal(arr, x):
    return sum(1 for num in arr if num <= x)

print(count_less_equal([4,5,8,1,3], 6))
print(count_less_equal([6,10,12,15,2,4,5], 14))