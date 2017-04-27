import sympy
from tqdm import tqdm

count = 0
for i in tqdm(range(2, 1000001)):
  if i in sympy.factorint(i):
    num = str(i)
    junkan = True
    for j in range(len(num)):
      num = num[-1] + num[0:len(num)-1]
      if not int(num) in sympy.factorint(int(num)):
        junkan = False
    if junkan:
      count += 1

print("Answer:" + str(count))

