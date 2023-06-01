from Crypto.Cipher import AES as PYAES
from Crypto.Util.number import getRandomRange
from Crypto.Util.Padding import pad
from Crypto import Random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from random import seed, randint, shuffle
from gmpy2 import legendre

from secret import aes_key, p, q, rseed


class AESP():

    def __init__(self):
        self.key = aes_key
        self.iv = Random.new().read(16)

    def encrypt(self, msg):
        cipher = PYAES.new(self.key, PYAES.MODE_CBC, self.iv)
        return self.iv + cipher.encrypt(pad(msg, 16))

    def decrypt(self, ct):
        cipher = PYAES.new(self.key, PYAES.MODE_CBC, ct[:16])
        return cipher.decrypt(ct[16:])

    def setKey(self, key):
        self.key = key


class AESC():

    def __init__(self):
        self.key = aes_key
        self.iv = Random.new().read(16)

    def encrypt(self, msg):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(pad(msg, 16)) + encryptor.finalize()
        return self.iv + ct

    def decrypt(self, ct):
        cipher = PYAES.new(self.key, PYAES.MODE_CBC, ct[:16])
        return cipher.decrypt(ct[16:])

    def setKey(self, key):
        self.key = key


class GM():

    def __init__(self):
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.x = self.jacobi_symbol()

    def jacobi_symbol(self):
        tmp = getRandomRange(0, self.n)
        while legendre(tmp, self.p) != -1 or legendre(tmp, self.q) != -1:
            tmp = getRandomRange(0, self.n)

        return tmp

    def encrypt(self, bits):
        ct = []

        for bit in bits:
            y = getRandomRange(0, self.n)
            tmp = pow(y, 2) * pow(self.x, int(bit)) % self.n

            ct.append(format(tmp, 'x'))

        return ct

    def decrypt(self, ct):
        m = 0
        for c in ct:
            m <<= 1
            if legendre(c % self.p, self.p) != 1 or legendre(
                    c % self.q, self.q) != 1:
                m += 1
        h = '%x' % m
        return bytes.fromhex(h.zfill(32))


class OBF():

    def __init__(self):
        self.seed = rseed % 2**7
        seed(self.seed)
        self.pin = self.genPin()

    def genPin(self):
        pin = []
        initial = [[randint(1, 256) for _ in range(128)] for _ in range(8)]
        initial = self.transpose(initial)
        for i in range(128):
            tmp = initial[i]
            shuffle(tmp)
            pin.append(tmp[0])
        return ([i % 2 for i in pin])

    def transpose(self, bits):
        return [row for row in map(list, zip(*bits))]

    def xor(self, bits, key):
        return [a ^ b for a, b in zip(bits, key)]

    def bytesToBits(self, bytes):
        bits = bin(int(bytes.hex(), 16))[2:].zfill(len(bytes) * 8)
        bits = [int(i) for i in bits]
        return bits

    def bitsToBytes(self, bits):
        bits = "".join([str(i) for i in bits])
        bits = [int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)]
        return bytes(bits)

    def obfuscate(self, bytes):
        bits = self.bytesToBits(bytes)
        bits = self.xor(bits, self.pin)
        return bits

    def deobfuscate(self, bytes):
        return self.bitsToBytes(self.obfuscate(bytes))
