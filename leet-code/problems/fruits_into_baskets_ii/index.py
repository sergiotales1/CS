# https://leetcode.com/problems/fruits-into-baskets-ii/description/?envType=daily-question&envId=2025-08-05
def i(fruits, baskets):
  u_f = 0
  for i in fruits:
    for j in range(len(baskets)):
      if baskets[j] >= i:
        baskets[j] = 0
        break
      elif j == len(baskets) - 1:
        u_f += 1
  print(baskets)
  return u_f

# two loops | i = fruits | j = baskets
# keep track of unplaced fruits | u_f = 0
# if j >= i j = 0
# u_f = 0 
fruits, baskets = [8, 5], [1, 8]
# fruits, baskets = [4, 2, 5], [3, 5, 4]
print(i(fruits, baskets))
