#You are given two arrays a[] and b[], return the Union of both the arrays in any order.

def union_array(a, b):
    return list(set(a) | set(b))

print(union_array([1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2]))