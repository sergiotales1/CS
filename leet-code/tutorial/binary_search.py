arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
def binary_search(target, left, right):
  while left <= right:

    mid = (left + right) // 2

    if target == arr[mid]:
      return mid

    if arr[mid] < target:
      left = mid + 1 
    else:
      right = mid - 1
    
print(binary_search(8, 0, len(arr) - 1))



