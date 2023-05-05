'''
s
edufw
edufw
edufw
tg
h
ev
a
'r
st
'''

import itertools

edufw = "edufw"
tg = "tg"
ev = "ev"
r = "'r"
st = "st"

for combo in itertools.product(edufw, repeat=3):
    for t in tg:
        for e in ev:
            for a in r:
                for s in st:
                    s1 = "s" + "".join(combo) + t + "h" + e + "a" + a + s
                    print(s1)

