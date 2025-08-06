# https://leetcode.com/problems/length-of-last-word/description/

def i(s):
  split = s.split()
  lastWordLength = len(split[len(split) - 1])

  print(lastWordLength)
  return

i("   fly me   to   the moon  ")