#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. 

def searchRange(nums, target):
    def findFirst():
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    def findLast():
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    return [findFirst(), findLast()]

print(searchRange([5,7,7,8,8,10], 8))  #output = [3, 4]