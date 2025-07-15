# https://leetcode.com/problems/valid-word/?envType=daily-question&envId=2025-07-15
validDigits = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

vowels = ["a", "e", "i", "o", "u"]

def validWord(str):
  if len(str) < 3:
    return False
  
  lowerCase = str.lower()
  
  if not any(letter in lowerCase for letter in vowels):
    return False

  for letter in lowerCase:
    if not (letter in validDigits):
      print(letter)
      return False

  print(len(str))
  return



validWord("234Adas")