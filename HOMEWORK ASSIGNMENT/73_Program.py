#Balancing Consonants and Vowels Ratio

def is_vowel(c):
    return c in 'aeiou'

def balanced(arr):
    count = 0
    
    for i in range(len(arr)):
        v = 0
        c = 0
        for j in range(i, len(arr)):
            for ch in arr[j]:
                if is_vowel(ch):
                    v += 1
                else:
                    c += 1
            if v == c:
                count += 1
    
    return count

# Example
print(balanced(["ab", "be"]))  # Output: 3