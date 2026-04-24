#Count Even Letters 

from collections import Counter

def count_even(s):
    freq = Counter(s)
    return sum(1 for v in freq.values() if v % 2 == 0)

# Example
print(count_even("abacaba"))  # Output: 2