from Crypto.Util.number import long_to_bytes
from pwn import *

a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff


def solveDL():
    b = randint(1, p)
    E = EllipticCurve(GF(p), [a, b])
    order = E.order()
    factors = prime_factors(order)

    valid = []
    for factor in factors:
        if factor <= 2**40:
            valid.append(factor)

    prime = valid[-1]

    G = E.gen(0) * int(order / prime)

    # Here we send G to the server
    tmp_point = G.xy()
    tmp_x, tmp_y = str(tmp_point[0]), str(tmp_point[1])
    tmp_point = tmp_x + " " + tmp_y
    message = b"Awaiting public key of the client...\n"
    r.sendlineafter(message, bytes(tmp_point, "Latin"))

    # We get back Q which is G * k
    data = r.recvline()
    print(data)

    if b"Error" in data:
        print("An error on the server occured")
        return None, None

    Q = eval(data[len("Shared secret: "):])
    try:
        Q = E(Q[0], Q[1])
        print("Computing the discrete log problem")
        log = G.discrete_log(Q)
        print(f"DL found: {log}")
        return (log, prime)
    except Exception as e:
        print(e)
        return None, None


def getDLs():
    dlogs = []
    primes = []
    for i in range(1, 16):
        log, prime = solveDL()
        if log != None:
            dlogs.append(log)
            primes.append(prime)
        print(f"counter: {i}")
    return dlogs, primes


def pwn():
    dlogs, primes = getDLs()
    print(f"dlogs: {dlogs}")
    print(f"primes: {primes}")
    super_secret = CRT_list(dlogs, primes)
    print(long_to_bytes(super_secret))

ip, port = '144.126.206.29',31283
r = remote(ip, port)
pwn()
