#You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.

def row_with_max_ones(arr):
    max_row_index = -1
    max_count = 0
    
    for i in range(len(arr)):
        count = arr[i].count(1)
        if count > max_count:
            max_count = count
            max_row_index = i
    
    return max_row_index


print(row_with_max_ones([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]))  #output = 2
