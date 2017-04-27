prefibo = 2
pre = 1
fibo = 2
result = 2
while fibo < 4000000:
    fibo = pre + prefibo
    pre = prefibo
    prefibo = fibo
    print(fibo)
    if fibo % 2 == 0:
        result = result + fibo

print('Answer:' + str(result))
