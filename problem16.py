import numpy as np

result = 0
print(2**1000)
for c in str(2**1000):
  print(c)
  result += int(c)

print("Answer:" + str(result))
