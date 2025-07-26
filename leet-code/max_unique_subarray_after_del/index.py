def i(nums):
  arr = []
  for n in nums:
    if n in arr:
      continue

    if n <= 0:
      continue
    
    arr.append(n)
  
  total = 0
  for n in arr:
    total+=n

  return total
  

print(i([1,2,3,4,5]))