# https://leetcode.com/problems/merge-sorted-array/
# https://www.youtube.com/watch?v=P1Ic85RarKY
def i(nums1, m, nums2, n):
  last = m + n - 1

  while n > 0 and m > 0:
    if nums1[m - 1] > nums2[n - 1]:
      nums1[last] = nums1[m - 1]
      m -= 1
    else:
      nums1[last] = nums2[n - 1]
      n -= 1
    last -= 1

  while n > 0:
    nums1[last] = nums2[n - 1]
    n, last = n - 1, last - 1

  return nums1

nums1, m = [1,2,3,0,0,0], 3
nums2, n = [2,5,6], 3

# nums1[m-1] = 3 | nums2[n - 1] = 6

print(i(nums1, m, nums2, n))

# def i(nums1, m, nums2, n):
#   cur = 0
#   for i in range(m, n + m):
#     nums1[i] = nums2[cur]
#     print(nums1[i], nums1[cur])
#     cur+=1
#   nums1.sort()
#   return nums1