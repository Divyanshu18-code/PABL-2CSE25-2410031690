#Given an array arr[] of size n, your task is to divide the array in two subsets such that the absolute difference between the sum of elements in the two subsets is equal 
#to zero (i.e., both subsets have the same sum). 
#• If n is even, both subsets must contain exactly n/2 elements. 
#• If n is odd, one subset must contain (n-1)/2 elements and the other subset must contain (n+1)/2 elements.

from itertools import combinations

def partition(arr):
    n = len(arr)
    total = sum(arr)
    half = total // 2

    best = None

    for comb in combinations(arr, n//2):
        if sum(comb) == half:
            other = list(arr)
            for x in comb:
                other.remove(x)
            return [list(comb), other]

print(partition([1,2,3,4]))
print(partition([5,10,15]))