#Given an array arr[] of strings of equal length, where each string consists of lowercase English letters, find the total number of pairs of strings that differ in exactly one character position.

def one_mismatch(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count == 1

def count_pairs(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if one_mismatch(arr[i], arr[j]):
                count += 1
    return count

# Example
print(count_pairs(["abc", "abd", "bbd"]))  # Output: 2