#Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements. 

def marge_array(a, b):
    n = len(a)
    m = len(b)

    for i in range(n):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            b.sort()
    return a, b

print(marge_array([2, 4, 7, 10], [2, 3] ))   # output = ([2, 2, 3, 4], [7, 10])
print(marge_array([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))   # output = ([1, 2, 3, 5, 8, 9], [10, 13, 15, 20])
print(marge_array([0, 1], [2, 3]))   # output = ([0, 1], [2, 3])