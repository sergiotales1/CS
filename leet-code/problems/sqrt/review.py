# https://leetcode.com/problems/sqrtx/

def r(x):
  l, r = 0, x
  res = 0

  while l <= r:
    mid = l + ((r - l) // 2) # (2 + 4) // 2

    if mid * mid < x:
      l = mid + 1
      res = mid
    elif mid * mid > x:
      r = mid - 1
    else:
      return mid
  return res




# 0 up to x
# [0, 1, 2, 3, x]
# l = 0 (mid + 1)
# loop from 1 to x
print(r(9)) # 3
print(r(49)) # 3
print(r(2)) # 3