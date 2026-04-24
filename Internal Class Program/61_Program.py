#You are given a string s consisting only of the characters '(' and ')'. Your task is to determine the minimum number of parentheses (either '(' or ')') that must be inserted at 
#any positions to make the string s a valid parentheses string. 

def min_add(s):
    balance = 0
    add = 0
    
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                add += 1
    
    return add + balance

# Example
print(min_add("(()("))  # Output: 2