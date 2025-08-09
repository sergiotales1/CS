# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):
  romanMap = {"I": 1, "V": 5, "X": 10, "L": 50 ,"C" : 100, "D":500, "M":1000}
  total = 0
  for i, c in enumerate(s):
    if i == len(s) - 1:
      total += romanMap[c] 
      continue

    if romanMap[c] < romanMap[s[i + 1]]: 
      total -= romanMap[c]
    else:
      total += romanMap[c]
  return total

print("value: MCMXCIV ",romanToInt("MCMXCIV")) # 1994
# romanToInt("III")
print("value: LIV ",romanToInt("LIV")) # 54