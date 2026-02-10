#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n. 

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return list(map(int, str(result)))

print(factorial(5))  # output = [1, 2, 0]
print(factorial(10)) # output = [3, 6, 2, 8, 8, 0, 0]