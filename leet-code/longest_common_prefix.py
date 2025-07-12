def longestCommonPrefix(strs):
  for word in strs:
    for letter in word:
      print(letter)

strs = ["oi", "hi"]
longestCommonPrefix(strs)