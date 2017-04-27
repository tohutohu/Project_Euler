
for c in range(1001):
  for b in range(c):
    for a in range(b):
      if a*a + b*b == c*c and 1000 == a + b + c:
        print(str(a) + str(b) + str(c))
        print("Answer:" + str(a*b*c))
