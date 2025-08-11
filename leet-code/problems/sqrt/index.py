# https://leetcode.com/problems/sqrtx/

def i(x):
  l, r = 0, x
  res = 0

  while l <= r:
      m = l + ((r - l) // 2)
      if m * m > x:
          r = m - 1
      elif m * m < x:
          l = m + 1
          res = m
      else:
          return m
  return res




print(i(9)) # 1
# print(i(4)) # 2

# The time complexity is O(square root of n) because we run the loop until n * n > x.
# This means the loop will stop when n is greater than the square root of x.
# For example, if x is 9, the loop will run for n = 1, 2 and 3. 
# When n = 4, 4 * 4 (16) is greater than 9, so the loop terminates.
# The number of iterations is roughly equal to the square root of x.  
def linear(x):
  if x == 1 or x == 0:
    return x
  
  for n in range(1, x + 1):
    if n * n > x:
      return n - 1

# print(linear(2)) # 1