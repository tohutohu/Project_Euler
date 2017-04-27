result = 0
po = 0
for i in range(1, 1000000):
  print("Start:" + str(i))
  count = 1
  n = i
  while n != 1:
    if n % 2 == 0:
      n = n /2
    else:
      n = 3*n + 1
    count += 1
  print("count:" + str(count))
  if result < count:
    result = max([count, result])
    po = i

print("Count:" + str(result))
print("Answer:" + str(po))
