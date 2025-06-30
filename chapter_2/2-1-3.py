def insertion_sort(A, n):
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while A[j] > key and j >= 0: # While the element to the left is greater than the key, keep shifting it right.
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = key
  return A

def insertion_sort_decreasing(A, n):
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while A[j] < key and j >= 0: # So we just need to invert this
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = key
  return A
  

    

arr = [2, 5, 1, 3]
print(insertion_sort_decreasing(arr, 4))
