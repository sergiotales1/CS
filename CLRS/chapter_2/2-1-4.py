def linear_search(A, x):
  for i in range(0, len(A)):
    if A[i] == x:
      return i
  return None


arr = [2, 8, 1 , 5, 3]
print(linear_search(arr, 8))