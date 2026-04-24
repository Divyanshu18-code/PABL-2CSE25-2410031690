#Count Unique Vowel Strings

import math
from collections import Counter

def vowel_strings(s):
    vowels = 'aeiou'
    count = Counter(s)
    
    unique = [v for v in vowels if v in count]
    
    ways = 1
    for v in unique:
        ways *= count[v]
    
    return ways * math.factorial(len(unique))

# Example
print(vowel_strings("aeiou"))  # Output: 120