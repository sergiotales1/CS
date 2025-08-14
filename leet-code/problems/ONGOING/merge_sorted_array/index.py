# https://leetcode.com/problems/merge-sorted-array/
# https://www.youtube.com/watch?v=P1Ic85RarKY
def i(nums1, m, nums2, n):
  var = 0
  p2 = 0
  for i in range(m + n):
    if nums1[i] < nums2[p2]:
      continue
    else:
      if var == 0 :
        var = nums1[i]
        nums1[i] = nums2[p2]
        p2+=1
      if var > 0 and var < nums2[p2]:
        nums1[i] = var
        var = 0
        continue
  return

nums1, m = [1,2,3,0,0,0], 3
nums2, n = [2,5,6], 3

# [1, 2, 3, 2, 0, 0] 3 | 5
# var = 3
# p1 = 3 | p2 = 2
# [1, 2, 3, 0, 0, 0] 
# [2, 5, 6] 
# nums[3] = nums[0]
print(i(nums1, m, nums2, n))

# def i(nums1, m, nums2, n):
#   cur = 0
#   for i in range(m, n + m):
#     nums1[i] = nums2[cur]
#     print(nums1[i], nums1[cur])
#     cur+=1
#   nums1.sort()
#   return nums1