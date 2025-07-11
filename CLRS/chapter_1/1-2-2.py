# run: python 1-2-2.py 
import math

for n in range(2, 100):
    if n < 8 * math.log2(n):
        print(f"{n} ✅")
    else:
        print(f"{n} ❌")
        break
