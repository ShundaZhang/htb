import sys
import csv
from collections import defaultdict

columns = defaultdict(list)
with open(sys.argv[1]) as f:
    reader = csv.DictReader(f)
    for row in reader:
        for k, v in row.items():
            columns[k].append(v)

data = map(lambda h: int(h, 16), columns["Data"])
data = list(filter(lambda h: ((h & 0x0f) & 0x01) and ((h & 0x0f) & 0x04) and ((h & 0x0f) & 0x08), data))

data = zip(data[::2], data[1::2])
data = map(lambda pair: chr(pair[0] & 0xf0 | (pair[1] >> 4)), data)
print("".join(data))
