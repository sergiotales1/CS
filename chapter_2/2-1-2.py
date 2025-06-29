def sum_array(A, n):
  sum = 0
  for i in range(0, n): 
    sum += A[i]
  return sum

arr = [2, 5]
print(sum_array(arr, len(arr)))