from tqdm import tqdm
result = 1

for i in tqdm(range(21, 41)):
  result *= i

for j in tqdm(range(1, 21)):
  result = result / j

print("Answer:" + str(result))
