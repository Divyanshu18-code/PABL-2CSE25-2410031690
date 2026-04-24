#Given a lowercase string array arr[]. Each element in the array represents a vote cast for a candidate. Return the name of the candidate who received the maximum number 
#of votes and the count of votes he received. In case of a tie between two or more candidates, return the lexicographically smallest name. 

from collections import Counter

def winner(arr):
    freq = Counter(arr)
    max_votes = max(freq.values())
    
    candidates = [k for k, v in freq.items() if v == max_votes]
    return [min(candidates), str(max_votes)]

# Example
print(winner(["john", "johnny", "john"]))  