import numpy as np

result = np.power(np.sum(range(1, 101)), 2) - np.sum(np.power(range(1, 101), 2))
print(result)
