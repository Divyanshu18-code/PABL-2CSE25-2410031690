#Lexicographically Largest String After K Deletions

def largest_string(s, k):
    stack = []
    
    for ch in s:
        while k and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    return ''.join(stack[:len(s)-k])

# Example
print(largest_string("ritz", 2))  # Output: tz