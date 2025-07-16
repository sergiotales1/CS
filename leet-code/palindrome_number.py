def palindromeNumber(x):
  if x < 0:
    return False
  
  original_number = x
  digits = []

  while x > 0:
     digit = x % 10

     digits.append(digit)

     x //= 10

  reconstructed_number = 0

  for digit in digits:
    reconstructed_number = reconstructed_number * 10 + digit

  if(original_number == reconstructed_number):
     return True
  return False

def mv(x):
  s = str(x)
  print(s[::-1])
  return s[::-1] == s


print(mv(123))
print(palindromeNumber(121))
