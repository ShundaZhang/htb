#RSA_PKCS1v1_5 attacks!!!

#The server side will close connection in 3 minutes! Connection from PRC and US will be closed, as the latency is too high!
#Found HTB is using Digital Ocean London, so by a VPC in London can resolve this issue!!

#https://ctftime.org/writeup/31460
#https://platypwnies.de/writeups/2021/htb-uni-quals/crypto/oracle-leaks/
#https://github.com/mimoo/RSA_PKCS1v1_5_attacks
#https://link.springer.com/content/pdf/10.1007%2FBFb0055716.pdf
#https://link.springer.com/content/pdf/10.1007/3-540-44647-8_14.pdf

#!/usr/bin/python3

import logging
import os
import math
from pwn import *
from Crypto.Util.number import long_to_bytes

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

'''
# setup
def generate_keypair(size_N_in_bits):
    size_prime = 1 << (size_N_in_bits / 2)
    while True:
        p = random_prime(size_prime)
        q = random_prime(size_prime)
        N = p * q
        phi = (p-1)*(q-1)
        e = 17
        if gcd(e, phi) != 1:
            continue
        # will sometimes not work, generate another setup?
        d = inverse_mod(e, phi)
        break
    return e, d, N
'''

# to do ceil() of large divisions
def ceildiv(a, b):
    return -(-a // b)

# helper
def get_byte_length(message):
    res = 0
    if (len(bin(message)) - 2) % 8 != 0:
        res += 1
    res += (len(bin(message)) - 2) // 8
    return res


# pad plaintext [00, 02, randoms, 00, messsage] of len target_length
def padding(message, target_length):
    # 02
    res = 0x02 << 8 * (target_length - 2)
    # random
    random_pad = os.urandom(target_length - 3 - get_byte_length(message))
    for idx, val in enumerate(random_pad):
        if val == 0:
            val = 1
        res += val << (len(random_pad) - idx + get_byte_length(message)) * 8
    # 00
    # message
    res += message

    return res


# a length oracle
def oracle_length(c, N, p):
    #p = pow(c, d, N)
    #return get_byte_length(p)
    p.sendline("3")
    p.sendline(long_to_bytes(c).hex())
    p.recvuntil("Length:")
    length = int(p.recvline().decode("utf-8").strip())
    return length

# our attack with Manger
def Manger(key_size, N, e, c, p, logging):
    # setup 1
    #e = 65537
    #priv = rsa.generate_private_key(
    # public_exponent=e,
    # key_size=key_size,
    # backend=default_backend()
    #)
    #d = priv.private_numbers().d
    #pub = priv.public_key()
    #N = pub.public_numbers().n

    # setup 2
    N_size = ceildiv(key_size, 8)
    #plaintext = 0x6c6f6c  # "lol"
    #ciphertext = pub.encrypt(b"lol", PKCS1v15())
    #padded = padding(plaintext, N_size)
    #logging.info("to find: %d" % padded)
    ciphertext = c
    # setup 3
    B = lower(N_size)
    total_msg = 0

    # setup attack
    N_bit_length = (N_size - 2) * 8

    # attack
    f1 = 2
    leak = 0

    # step 1
    logging.info("step 1.")
    while True:
        c2 = (ciphertext * pow(f1, e, N)) % N
        total_msg += 1
        leak = oracle_length(c2, N, p)
        if leak == N_size:
            logging.info("step 1.3b")
            break
        logging.info("step 1.3a")
        f1 = 2 * f1

    logging.info(str(total_msg) + " messages")

    # Step 2.
    logging.info("Step 2.")
    f2 = (N+B) // B
    f2 = f2 * (f1 // 2)
    while True:
        c2 = (ciphertext * pow(f2, e, N)) % N
        total_msg += 1
        leak = oracle_length(c2, N, p)
        if leak < N_size:
            logging.info("step 2.3b")
            break
        logging.info("step 2.3a")
        f2 = f2 + (f1//2)
    logging.info(str(total_msg) + " messages")
    
    # step 3.
    logging.info("Step 3.")
    m_min = ceildiv(N, f2)
    m_max = (N+B) // f2
    logging.info("\n- m_min: %d\n- m_max: %d\n" % (m_min, m_max))
    m = [m_min, m_max]
    while True:
        # find good f3
        f_tmp = 2*B // (m_max - m_min)
        i = f_tmp * m_min // N
        f3 = ceildiv(i * N, m_min)
        # try the oracle
        c2 = (ciphertext * pow(f3, e, N)) % N
        total_msg += 1
        leak = oracle_length(c2, N, p)
        # branch
        if leak < N_size:
            logging.info("step 3.5b")
            m_max = (i * N + B) // f3
        else:
            logging.info("3.5a")
            m_min = ceildiv(i * N + B, f3)
        logging.info("\n- m_min: %d\n- m_max: %d\n" % (m_min, m_max))
        if m_min == m_max:
            break

    #if m_min != padded:
    #    logging.fatal("algorithm did not work")
    #    exit(1)
    logging.info(str(total_msg) + " messages")
    return total_msg


# for N_size = 2:
# m_max = 11111111 11111111
def upper(num):
    return 2**(num*8) - 1

# for N_size = 2:
# m_min = 1 00000000
def lower(num):
    return 2**((num-1)*8) 

#

ip, port = "134.209.19.24", 30140

if __name__ == "__main__":
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    #p = process(["python3", "chall.py"])
    p = remote(ip, port)
    started = p.recvuntil(">")
    p.sendline("1")
    p.recvuntil("(n,e): (")
    nums = p.recvline().decode("utf-8").replace(")","").replace(" ","").replace("'","")
    n, e = nums.split(",")
    n = int(n, 16)
    e = int(e, 16)
    #p.interactive()
    p.recvuntil(">")
    p.sendline("2")
    p.recvuntil("Encrypted text:")
    text = p.recvline()
    text = text.decode("utf-8").strip()
    ct = int(text, 16)
    Manger(1024, n, e, ct, p, logger)

'''
root@ubuntu-s-1vcpu-1gb-lon1-01:~/htb/ctf/crypto/OracleLeaks# python2
Python 2.7.18 (default, Sep 12 2022, 15:58:04)
[GCC 12.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> ('0'+hex(7142021928104790007219007127486191800406098549214233731419885073119784531054272060561639866217267567068389346952550013180229447536223058905081582877135305958480405524559464339500830216101809393916903720951076992051114120426900760850855647377114035724429375918801957502699546636070570248038913368694941309)[2:-1]).decode('hex')
'\x02\x9a\x89\xf6\xd8O\x94i\x80Z\x9e\x9c:\xa0\xfd)B\x85\x16VM>\xdco\xe5\r\xcf\xdd\x1c\x1f\x05\x04\x9b\tr\xad\x84\xe5\xccO\xd9\xf3\xd2\x9dZ\xad[\x160\x02|\xe0\x9b/\xa7\xb3\xb7\xb8&0\xfd\x0e\xe1h\xb9\x86\xc6\xc8\xa8\x1b\xa7QM\x94\xe8\x18\x00HTB{m4ng3r5_4tt4ck_15_c001_4nd_und3rv4lu3d_341m3f}'
'''
