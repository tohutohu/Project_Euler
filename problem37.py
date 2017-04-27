import sympy
from tqdm import tqdm

result = 0
for i in tqdm(range(12, 1000000)):
  if i in sympy.factorint(i):
    po = True
    num = str(i)
    for j in range(1, len(num)):
      if 1 == int(num[j:]) or not int(num[j:]) in sympy.factorint(int(num[j:])) or 1 == int(num[:-1*j]) or not int(num[:-1*j]) in sympy.factorint(int(num[:-1*j])):
        po = False
        break

    if po:
      print(i)
      result += i

print("Answer:" + str(result))
