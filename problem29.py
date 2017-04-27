from tqdm import tqdm

li = []
for a in tqdm(range(2, 101)):
  for b in range(2, 101):
    li.append(a**b)

print("Answer:" + str(len(list(set(li)))))
