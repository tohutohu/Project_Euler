import itertools

po = ["0","1","2","3","4","5","6","7","8","9"]

p = list(itertools.permutations(po))

l = []
for t in p:
  l.append(''.join(t))

l.sort()
print(l[1000000-1])
