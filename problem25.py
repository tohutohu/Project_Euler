pre = 1
fibo = 0
count = 0

while True:
  tmp = fibo
  fibo = fibo + pre
  pre = tmp
  count += 1
  if len(str(fibo)) == 1000:
    break


print("Answer:" + str(count))
