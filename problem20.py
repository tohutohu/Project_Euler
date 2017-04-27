import math
from tqdm import tqdm 

result = 0
for c in tqdm(str(math.factorial(100))):
  result += int(c)

print("Answer:" + str(result))
