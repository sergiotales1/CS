# https://leetcode.com/problems/happy-number/description/
# Understand better what's happening in here and find ways to explain this implementation
def i(n):
  visited = set()

  while n not in visited:
    visited.add(n)
    arr = [int(c) for c in str(n)]
    n = sum([v**2 for v in arr])
    if n == 1:
      return True
  return False

print(i(2))