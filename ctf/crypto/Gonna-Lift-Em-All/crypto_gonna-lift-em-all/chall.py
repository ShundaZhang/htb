from Crypto.Util.number import bytes_to_long, getPrime
import random

FLAG = b'HTB{???????????????????????????????????????????????????}'


def gen_params():
    p = getPrime(1024)
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    return (p, g, h), x


def encrypt(pubkey):
    p, g, h = pubkey
    m = bytes_to_long(FLAG)
    y = random.randint(2, p - 2)
    s = pow(h, y, p)
    return (g * y % p, m * s % p)


def main():
    pubkey, _ = gen_params()
    c1, c2 = encrypt(pubkey)

    with open('out.txt', 'w') as f:
        f.write(
            f'p = {pubkey[0]}\ng = {pubkey[1]}\nh = {pubkey[2]}\n(c1, c2) = ({c1}, {c2})\n'
        )


if __name__ == "__main__":
    main()
