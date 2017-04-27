import sympy
import math
from tqdm import tqdm

result = 0
for i in tqdm(range(1, 1000000)):
  junkan = True
  num = str(i)
  for l in range(math.ceil(len(num)/2)):
    if num[l] != num[-1*l - 1]:
      junkan = False
      break

  if junkan:
    num = format(i, "b")
    for j in range(math.ceil(len(num)/2)):
      if num[j] != num[-1*j - 1]:
        junkan = False
        break
  if junkan:
    result += i

print("Answer:" + str(result))

