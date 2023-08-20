#https://hackmd.io/@dogdogeatcatcat/rJav0g-93#Interception
#https://www.youtube.com/watch?v=xmnbRIYVsfQ&t=2123s

from pwn import *

from hashlib import sha256
from Crypto.Util.number import isPrime, getPrime, long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from pool import GREET, ANS

e = 0x10001
#context.log_level = 'debug'

#io = process('./server.py')
ip, port = "167.172.62.51", 31909
io = remote(ip, port)

io.recvuntil('We say : ')
buf = io.recvline().strip()
#print(buf)
c1 = bytes_to_long(bytes.fromhex(buf.decode()))

io.recvuntil('>')
io.sendline(b'S')
io.recvuntil('You say : ')
io.sendline(buf)
buf = io.recvline()
#print(buf.decode().split(' ')[4].strip().encode())
c2 = bytes_to_long(bytes.fromhex(buf.decode().split(' ')[4].strip()))

#print(c1, c2)

N = 0
ph = 0
for i in range(len(GREET)):
	if N != 0:
		break
	m1 = bytes_to_long(GREET[i].encode())
	for j in range(len(ANS)):
		m2 = bytes_to_long(ANS[j].encode())
		n = gcd(m1**e - c1, m2**e - c2)
		if n == 1:
			continue
		#print(f'GCD N: {n}, {int(n).bit_length()}')
		io.recvuntil('>')
		io.sendline(b'F')
		io.recvuntil('you know the public key :')
		io.sendline(sha256(str(n).encode()).digest().hex())
		buf = io.recvline()
		#print(buf)
		if b'Get out!' in buf:
			continue
		else:
			print(f'N found! {n}')
			N = n
			ph = int(buf.decode().split(' ')[6].strip())
			break

if N == 0:
	print('Try Again!')
	exit(0)

ln = int(N).bit_length()//2
ll = ln - 643
hp = (ph >> ll) << ll
#print(hp)

R.<x> = PolynomialRing(Zmod(N))
P = hp + x
#x0 = P.small_roots()[0] #too large, need to limit
x0 = P.small_roots(X=2^ll, beta=0.4)[0]
print(x0)

p = P(x0)
print(p)

q = N//int(p)

#print(p, q)

phi = (p-1)*(q-1)
a = 0xdeadbeef
ct = 0x1337
#Fermat’s little theorem
an = pow(a, N, phi)
key = pow(ct, an, N)

io.recvuntil('>')
io.sendline(b'R')
io.recvuntil('Enter decryption key :')
io.sendline(long_to_bytes(int(key))[:16].hex().encode())
print(io.recvall())
