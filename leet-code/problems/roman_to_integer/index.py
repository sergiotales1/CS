# https://leetcode.com/problems/roman-to-integer/description/
romanHashMap = {"I" : 1, "V": 5, "X": 10,"L":50, "C": 100, "D":500,"M": 1000}

def romanToInt(s):
  total = 0
  lastSymbol = ""
  for  symbol in s[::-1]:
    if symbol in romanHashMap.keys():
      if(symbol == "I" and (lastSymbol == "V" or lastSymbol == "X")):
        total -= romanHashMap[symbol]
      elif(symbol == "X" and (lastSymbol == "L" or lastSymbol == "C")):
        total -= romanHashMap[symbol]
      elif(symbol == "C" and (lastSymbol == "D" or lastSymbol == "M")):
        total -= romanHashMap[symbol]
      else:
        total += romanHashMap[symbol]
      lastSymbol = symbol
    else:
      return total
  return total

print("value: MCMXCIV ",romanToInt("MCMXCIV"))
# romanToInt("III")
print("value: LIV ",romanToInt("LIV"))