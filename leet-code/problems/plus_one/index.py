# https://leetcode.com/problems/plus-one/

def i(arr):
  l_n_str = ""
  for n in arr:
    n_str =  str(n)
    l_n_str += n_str
  
  l_n = int(l_n_str) + 1
  l_n_str = str(l_n)
  result_arr = []
  for char in l_n_str:
    n = int(char) 
    result_arr.append(n)
  return result_arr


# [2, 5, 9]
# [2, 6, 0]
# construct the integer
# transform to number

arr = [4, 3, 2, 1]

print(i(arr))