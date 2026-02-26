#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. 
#Each number in candidates may only be used once in the combination. 

def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result


print(combinationSum2([10,1,2,7,6,1,5],8))  #output = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]