import math

arr = ["a", "b", "c", "x", "y", "z"]
def find_me(target, start, end):
  if start > end:
    return "not found"
  
  middle = math.floor((start + end) / 2)

  if arr[middle] == target:
    return "Found it at index {}".format(middle)

  if arr[middle] > target:
    return find_me(target, start, middle - 1)

  if arr[middle] < target:
    return find_me(target,  middle + 1, end)

print(find_me("z", 0, 5))