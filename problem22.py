import glob
import re

files = glob.glob("./*.txt")

result = 0
for file in files:
  for line in open(file, "r"):
    names = re.findall("[a-zA-Z]+", line)
    names.sort()
    count = 0
    for name in names:
      count += 1
      for c in name:
        result += (ord(c)-64) * count

print("Answer:" + str(result))
