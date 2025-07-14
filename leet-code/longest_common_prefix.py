def longestCommonPrefix(strs):
  sortedStrs = sorted(strs) # sort alphabetically
  first = sortedStrs[0] # get first item
  last = sortedStrs[sortedStrs.__len__() - 1] # get last item
  result = "" # initialize result
  for i, n in enumerate(first):
    if first[i] != last[i]:
      break
    result = result + first[i]

  return result


def longestCommonPrefixImproved(strs):
  pref = strs[0]
  pref_len = len(pref)

  for s in strs[1:]:
    while pref != s[0:pref_len]:
      pref_len -= 1
      if pref_len == 0:
        return ""
      pref = pref[0: pref_len]
  return pref

def mv(strs):
  pref = strs[0]
  pref_len = len(pref)

  for s in strs[1:]:
    while pref != s[0:pref_len]:
      pref_len -= 1
      if pref_len == 0:
        return ""
      pref = s[0:pref_len]
  return pref




strs = ["hey", "he", "hello"]
strs = ["food", "fool", "family"]
print(mv(strs))
# print(longestCommonPrefixImproved(strs))




sortedArray = longestCommonPrefix(strs)

# print(sortedArray)