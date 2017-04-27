result = 0

for i in range(100, 1000):
  for j in range(100, 1000):
    po = i * j
    if po == int(str(po)[::-1]):
      result = max([po, result])

print("Answer:" + str(result))
