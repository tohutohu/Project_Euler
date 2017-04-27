from tqdm import tqdm

result = 0
for i in tqdm(range(2, 1000000)):
  po = 0
  for c in str(i):
    po += int(c) ** 5

  if po == i:
    result += i

print("Answer:" + str(result))
