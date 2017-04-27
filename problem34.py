import math
from tqdm import tqdm

result = 0
for i in tqdm(range(3, 1000000)):
  po = 0
  for c in str(i):
    po += math.factorial(int(c))

  if po == i:
    result += i

print("Answer:" + str(result))
