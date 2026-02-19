#Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false. 

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def all_palindromes(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


print(all_palindromes([111, 222, 333, 444, 555]))  #output = True
