#Shortest substring containing all vowels

def shortest_sub(s1, s2):
    need = set(s1)
    left = 0
    count = {}
    formed = 0
    min_len = float('inf')
    
    for right in range(len(s2)):
        ch = s2[right]
        if ch in need:
            count[ch] = count.get(ch, 0) + 1
            if count[ch] == 1:
                formed += 1
        
        while formed == len(need):
            min_len = min(min_len, right - left + 1)
            if s2[left] in count:
                count[s2[left]] -= 1
                if count[s2[left]] == 0:
                    formed -= 1
            left += 1
    
    return min_len if min_len != float('inf') else -1

# Example
print(shortest_sub("ae", "acbaudeq"))  # Output: 4