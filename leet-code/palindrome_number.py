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


print(palindromeNumber(121))

def extract_digits_math(number):
    if number < 0:
        # Handle negative numbers by working with the absolute value
        number = abs(number)
    
    digits = []
    
    # Special case for 0
    if number == 0:
        return [0]
        
    while number > 0:
        # Get the last digit
        digit = number % 10
        
        # Add the digit to the list
        digits.append(digit)
        
        # Remove the last digit
        number //= 10
    
    # The digits are in reverse order, so reverse the list
    return digits[::-1]

number = 12345
digits_list = extract_digits_math(number)
print(digits_list)  # Output: [1, 2, 3, 4, 5]

# Accessing individual digits from the list
first_digit = digits_list[0]  # 1
third_digit = digits_list[2]  # 3