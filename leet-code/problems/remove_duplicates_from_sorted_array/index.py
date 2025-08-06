# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def i(nums):
  w = 1
  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      nums[w] = nums[i]
      w+=1
  return len(nums[:w])
    



print(i([0,0,1,1,1,2,2,3,3,4]))