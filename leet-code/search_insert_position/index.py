# https://leetcode.com/problems/search-insert-position/description/
# not right, we need to know what is binary search

def i(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
  



nums = [1,3,5,6]
target = -3
print(i(nums, target, ))