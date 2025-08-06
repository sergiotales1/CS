# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
def i(haystack, needle):
  # loop through haystack
  # searching a subarray == needle
  # len(haystack)
  # haystack[i : len(needle)]
  if len(haystack) < len(needle):
    return -1
  
  for i in range(len(haystack) - len(needle) + 1):
    if haystack[i : i + len(needle)] == needle: # i = 0 | 0 : 2
      return i
  return -1
  



haystack = "sadbutsad" # i = 0
needle = "sad"
# haystack = "dress"
# needle = "ss"
# i <= 3
# i = 0 | dr e [0 : 2]
# i = 1 | re s
# i = 2 | es s
# i = 3 | ss _
print(i(haystack, needle))