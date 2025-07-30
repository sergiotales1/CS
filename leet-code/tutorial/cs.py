def findUniqueChar(string):
  map = {}

  for char in string:
    if char in map:
      map[char] = map[char] + 1
    else:
      map[char] = 0
  
  for char in map.keys():
    if map[char] == 0:
      return char
  return 


print(findUniqueChar("ffeaabbcce"))

