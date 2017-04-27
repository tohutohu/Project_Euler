from sympy import ntheory
import numpy as np
from tqdm import tqdm

sum = 0
for a in tqdm(range(1, 10000)):
  b = np.sum(ntheory.divisors(a)) - a
  if a == np.sum(ntheory.divisors(b)) - b and a != b:
    print(a)
    sum += a

print("Answer:" + str(sum))
