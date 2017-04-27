import sympy

primeCount = 0
i = 2
while True:
  factor = sympy.factorint(i)
  if i in factor:
    primeCount += 1
    print(str(primeCount) + ": " + str(factor))
    if primeCount == 10001:
      break
  i += 1

print("Answer:" + str(i))
