#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array. 


import heapq
def kth_smallest(arr, k):
   heapq.heapify(arr)
   #k-1 element remove from heap
   for _ in range(k-1):
     heapq.heappop(arr)
   return heapq.heappop(arr)  
   

print(kth_smallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4))   # output = 5
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))     # output = 7
