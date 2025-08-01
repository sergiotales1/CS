# https://leetcode.com/problems/remove-element/description/
def i(nums, val):
  w = 0
  for i in range(0, len(nums)):
    if nums[i] == val:
      continue
    else:
      nums[w] = nums[i]
      w+=1
  return w

print(i([0,1,2,2,3,0,4,2], 2))
