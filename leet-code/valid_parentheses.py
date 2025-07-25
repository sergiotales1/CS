# https://leetcode.com/problems/valid-parentheses/description/
def validParentheses(s):
  
  stack = []
  dict = {"]":"[", "}":"{", ")":"("}
  for char in s:
      if char in dict.values():
          stack.append(char)
      elif char in dict.keys():
        if stack == [] or dict[char] != stack.pop():
          return False
      else:
          return False
  return stack == []

def mv(s):
  stack = []
  dict = {"]":"[", ")":"(", "}":"{" }
  for char in s:
    if char in dict.values():
       stack.append(char)
    elif char in dict.keys():
      if stack == [] or dict[char] != stack.pop():
         return False
    else:
       return False
  return stack == []

      
          
print(mv("()"))

print(validParentheses("[([]])"))