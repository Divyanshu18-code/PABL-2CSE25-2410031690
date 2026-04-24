#Given two strings txt and pat having lowercase letters, the task is to check if any permutation of pat is a substring of txt. 

from collections import Counter

def check_perm(txt, pat):
    k = len(pat)
    pat_count = Counter(pat)
    
    for i in range(len(txt) - k + 1):
        if Counter(txt[i:i+k]) == pat_count:
            return True
    return False

# Example
print(check_perm("geeks", "eke"))  # Output: True