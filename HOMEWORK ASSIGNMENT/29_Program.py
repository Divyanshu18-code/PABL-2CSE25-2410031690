#You are given an m x n integer matrix matrix with the following two properties: 
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row. 

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  #output = True
