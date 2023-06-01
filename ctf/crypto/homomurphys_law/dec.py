#homomorphic
#!/usr/bin/env python3
#https://7rocky.github.io/en/ctf/htb-challenges/crypto/homomurphys-law/
#https://github.com/7Rocky/HackTheBox-scripts/blob/main/Challenges/Crypto/Homomurphy's%20Law/README.md
#https://en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem

'''
python3 dec.py 206.189.120.154:32373
[+] Opening connection to 206.189.120.154 on port 32373: Done
[+] PIN seed: 114
[+] Sending key index: Done
[+] OBF pin: [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]
[*] Zero key: b'\xc9\xbc\xeeq\x12\x98\xdf\x7f9K\xb4\x046\xc1R\x1b'
[+] AES key: 13ac6164903991ced058cd2d91c36809
[+] Flag: HTB{d4n9320u5_p20p327135_c4n_134d_70_d3c2yp71n9_3v32y7h1n9}
'''

from pwn import log, re, remote, sys
from random import seed, randint, shuffle
from Crypto.Util.number import getRandomRange
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


MBEGIN = "---BEGIN MORPHEUS KEY---"
MEND = "---END MORPHEUS KEY---"

GBEGIN = "----BEGIN GPUBLIC KEY---"
GEND = "---END GPUBLIC KEY---"


class GM():
    def __init__(self, n, x):
        self.n = n
        self.x = x

    def encrypt(self, bits):
        ct = []

        for bit in bits:
            y = getRandomRange(0, self.n)
            tmp = pow(y, 2) * pow(self.x, int(bit)) % self.n
            ct.append(format(tmp, 'x'))

        return ct


class OBF():
    def __init__(self, rseed):
        seed(rseed)
        self.pin = self.gen_pin()

    def gen_pin(self):
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


def h2d(h: str) -> int:
    return int(h, 16)


def aes_decrypt(key: bytes, enc_data: bytes) -> bytes:
    iv, ct = enc_data[:16], enc_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ct)


def main():
    host, port = sys.argv[1].split(':')
    io = remote(host, int(port))

    with open('sensitive_data/custom_note.txt') as f:
        custom_note = f.read()

    note = custom_note.split(f'\n{MBEGIN}')[0]
    e_k_xor_pin = list(map(h2d, re.findall(
        f'{MBEGIN}\n(.*?)\n{MEND}', custom_note, re.DOTALL)[0].split()))
    n, x = map(h2d, re.findall(
        f'{GBEGIN}\n(.*?)\n{GEND}', custom_note, re.DOTALL)[0].split())

    gm = GM(n, x)

    prog = log.progress('PIN seed')
    index_prog = log.progress('Sending key index')

    for s in range(128):
        prog.status(str(s))
        obf = OBF(s)
        io.recvuntil(b'Awaiting for encryption key')

        for i, p in enumerate(gm.encrypt(obf.pin)):
            index_prog.status(str(i))
            io.sendlineafter(b'> ', str(h2d(p)).encode())

        io.sendlineafter(b'AES Encrypt\n\n> ', b'1')
        enc_data = bytes.fromhex(io.recvline().decode().strip())

        if note.encode() in aes_decrypt(b'\0' * 16, enc_data):
            break

    prog.success(str(s))

    zero_key = bytes.fromhex(hex(int(''.join(map(str, obf.pin)), 2))[2:])
    log.success(f'OBF pin: {obf.pin}')
    log.info(f'Zero key: {zero_key}')

    key = []
    prog = log.progress('AES key')

    for j in range(16):
        io.recvuntil(b'Awaiting for encryption key\n\n')

        for i, k in enumerate(e_k_xor_pin):
            index_prog.status(str(i))
            io.sendlineafter(b'> ', str(k if j == i // 8 else k * k).encode())

        io.sendlineafter(b'AES Encrypt\n\n> ', b'1')
        enc_data = bytes.fromhex(io.recvline().decode().strip())

        for k in range(256):
            test_key = zero_key[:j] + bytes([k]) + zero_key[j + 1:]

            if note.encode() in aes_decrypt(test_key, enc_data):
                key.append(k)
                prog.status(bytes(key).hex())
                break

    index_prog.success()
    prog.success(bytes(key).hex())

    with open('sensitive_data/flag.txt.IBKFZ', 'rb') as f:
        flag = aes_decrypt(bytes(key), f.read())
        log.success('Flag: ' + unpad(flag, 16).decode())


if __name__ == '__main__':
    main()
