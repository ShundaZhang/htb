from random import randint
from secrets import flag, r

pubkey = Matrix(ZZ, [
    [47, -77, -85],
    [-49, 78, 50],
    [57, -78, 99]
])

for c in flag:
    v = vector([ord(c), randint(0, 100), randint(0, 100)]) * pubkey + r
    print(v)
