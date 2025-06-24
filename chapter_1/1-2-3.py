n = 1
while True:
  left = 100 * n ** 2
  right = 2 ** n
  print(f"\nn = {n}, 100n² = {left}, 2^n = {right}")
  if left < right:
    print(f"\n✅ The smallest n such that 100n² < 2^n is: {n}")
    break
  n += 1