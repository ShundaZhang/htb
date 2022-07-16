#!/usr/bin/env python3
from secret import flag, p, q
from Crypto.Util.number import bytes_to_long
from random import randint


def partition_message(m, N):
    m1 = randint(1, N)
    parts = []
    remainder = 0
    while sum(parts) < m:
        if sum(parts) + m1 < m:
            parts.append(m1)
        else:
            remainder = m - sum(parts)
            parts.append(m1 + remainder)
    return (parts, remainder)


def encode(message, N):
    m = bytes_to_long(message)
    parts, remainder = partition_message(m, N)
    ciphers = [pow(c, 2, N) for c in parts]
    return (ciphers, remainder)


N = p * q
ciphers, remainder = encode(flag, N)

with open("output.txt", "w") as f:
    out = f'{N}\n{remainder}\n{ciphers}'
    f.write(out)
