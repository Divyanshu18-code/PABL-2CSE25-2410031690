#Given a string s, the task is to arrange the string according to the frequency of each character, in ascending order. If two elements have the same frequency, then they are 
#sorted in lexicographical order.

from collections import Counter

def sort_freq(s):
    freq = Counter(s)
    return ''.join(sorted(s, key=lambda x: (freq[x], x)))

# Example
print(sort_freq("geeksforgeeks"))  # Output: forggkksseee