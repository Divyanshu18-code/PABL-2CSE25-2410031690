#Given two integers n and k, the task is to find all valid combinations of k numbers that adds up to n based on the following conditions: 
#• Only numbers from the range [1, 9] used. 
#• Each number can only be used at most once.

def combinationSum3(k, n):
    res = []

    def backtrack(start, path, total):
        if len(path) == k and total == n:
            res.append(path[:])
            return
        for i in range(start, 10):
            if total + i > n:
                break
            backtrack(i+1, path+[i], total+i)

    backtrack(1, [], 0)
    return res

print(combinationSum3(3,9))
print(combinationSum3(3,3))