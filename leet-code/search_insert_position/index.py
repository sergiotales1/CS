# https://leetcode.com/problems/search-insert-position/description/
# not right, we need to know what is binary search

def i(nums, target):
  
  numsLength = len(nums)
  for i, n in enumerate(nums):
    if n == target:
      return i

    if target < n:
      return i
      
    if i == numsLength - 1:
      return i + 1
    
    if i < numsLength - 1:
      if target > n and target < nums[i+1]:
        return i + 1



nums = [1,3,5,6]
target = 7
print(i(nums, target))