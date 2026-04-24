#Given a string s consisting of balanced parentheses, calculate the score of the string based on the following rules:

def score(s):
    stack = [0]
    
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            val = stack.pop()
            stack[-1] += max(2 * val, 1)
    
    return stack[0]

# Example
print(score("(()(()))"))  # Output: 6