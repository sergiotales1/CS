# https://leetcode.com/problems/valid-word/?envType=daily-question&envId=2025-07-15
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

vowels = ["a", "e", "i", "o", "u"]

def validWord(str):
  if len(str) < 3:
    return False
  
  lowerCase = str.lower()

  hasConsonant = False
  hasVowel = False
  for letter in lowerCase:
    if letter in alphabet:
      if letter in vowels:
        hasVowel = True
      else:
        hasConsonant = True
    else:
      if not letter in numbers:
        return False
  return hasConsonant & hasVowel


print(validWord("234Adas"))