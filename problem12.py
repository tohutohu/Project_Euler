import sympy

i = 0
po = 0
while True:
  i += 1
  po += i
  if sympy.divisor_count(po) > 500:
    break

print("Answer:" + str(po))
