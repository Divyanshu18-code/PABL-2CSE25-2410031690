#Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix. 

def matrix_median(mat):
    arr = []
    for row in mat:
        arr.extend(row)
    
    arr.sort()
    n = len(arr)
    return arr[n // 2]


print(matrix_median([[1, 3, 5],[2, 6, 9],[3, 6, 9]]))  #output = 5
