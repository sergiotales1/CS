# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
def i(nums):
  hillsAndValleys = 0
  numsLength = len(nums)
  for i, n in enumerate(nums):
    if i == 0 or i == numsLength - 1:
      continue
    
    neighbor = i
    while neighbor < numsLength - 1 and n == nums[neighbor]:
      neighbor+=1
    
    if n > nums[neighbor] and n > nums[i - 1]:
      hillsAndValleys+=1
      
    if n < nums[neighbor] and n < nums[i - 1]:
      hillsAndValleys+=1
    
  return hillsAndValleys


nums = [6,6,5,5,4,1]
print(i(nums))