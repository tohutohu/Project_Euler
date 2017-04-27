import sympy
import numpy as np
primes = []

for i in range(2, 2000001):
  if i in sympy.factorint(i):
    primes.append(i)

print("Answer:" + str(np.sum(primes)))
