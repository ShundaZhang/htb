import netsquid as ns
from random import seed, randint
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

O = "Origin"

ns.sim_reset()


def eea(r0, r1):
    if r0 == 0:
        return (r1, 0, 1)
    else:
        g, s, t = eea(r1 % r0, r0)
        return (g, t - (r1 // r0) * s, s)


def add(P, Q, a, m):
    if (P == O):
        return Q
    elif (Q == O):
        return P
    elif ((P[0] == Q[0]) and (P[1] == m - Q[1])):
        return O
    else:
        if (P[0] == Q[0] and P[1] == Q[1]):
            S = ((3 * (pow(P[0], 2)) + a) * eea(2 * P[1], m)[1]) % m
        else:
            S = ((Q[1] - P[1]) * eea((Q[0] - P[0]) % m, m)[1]) % m
        x3 = (pow(S, 2) - P[0] - Q[0]) % m
        y3 = (S * (P[0] - x3) - P[1]) % m
        Q[0], Q[1] = x3, y3
        return [x3, y3]


def multiply(s, P, E):
    s = list(int(k) for k in "{0:b}".format(s))
    a, p = E["a"], E["p"]
    del s[0]
    T = P.copy()
    for i in range(len(s)):
        T = add(T, T, a, p)
        if (s[i] == 1):
            T = add(P, T, a, p)
    return T


def parseUserPoint(user_point):
    return [int(c) for c in user_point.split(",")]


def parseUserBasis(user_basis):
    if len(user_basis) != 256:
        raise Exception("Input must be of length 256")
    basis = []
    for b in user_basis:
        if b == "Z":
            base = ns.Z
        elif b == "X":
            base = ns.X
        else:
            raise Exception(
                "Incorrect base, must be Standard (Z) of Hadamard (X)")
        basis.append(base)
    return basis


def measure(q, obs):
    res, _ = ns.qubits.measure(q, obs)
    return res


def randomBasis():
    r = randint(0, 1)
    return ns.Z if r else ns.X


def bitsToHash(bits):
    bit_string = ''.join([str(i) for i in bits])
    blocks = bytes(
        [int(bit_string[i:i + 8], 2) for i in range(0, len(bit_string), 8)])
    return sha256(blocks).digest()


def bitsToHex(bits):
    bit_string = ''.join([str(i) for i in bits])
    blocks = bytes(
        [int(bit_string[i:i + 8], 2) for i in range(0, len(bit_string), 8)])
    return blocks.hex()


def generateKeys(basis, private_key):
    seed(private_key)
    q_server_key = []
    q_user_key = []

    for i in range(256):
        qubits = ns.qubits.create_qubits(2)
        q1, q2 = qubits[0], qubits[1]
        ns.qubits.operate(q1, ns.X)
        ns.qubits.operate(q1, ns.H)
        ns.qubits.operate(q2, ns.X)
        ns.qubits.combine_qubits([q1, q2])
        ns.qubits.operate([q1, q2], ns.CX)
        q_server_key.append(measure(q1, randomBasis()))
        q_user_key.append(measure(q2, basis[i]))

    q_server_key = bitsToHash(q_server_key)
    q_user_key = bitsToHex(q_user_key)
    return q_server_key, q_user_key


def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, 16))
    return ciphertext
