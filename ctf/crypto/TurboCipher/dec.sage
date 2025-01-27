from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
import gmpy2

context.log_level = 'debug'

ip,port='144.126.228.151',31801

io = remote(ip,port)

io.recvuntil('p = ')
p = int(io.recvline().decode().strip())

io.recvuntil('b = ')
b = int(io.recvline().decode().strip())

io.recvuntil('c = ')
c = int(io.recvline().decode().strip())

io.recvuntil('Please, use nonce = ')
n = int(io.recvline().decode().split(' ')[0])

m = matrix(GF(p), [[0,1], [c,b]])
x0 = 0
x1 = 1
m = m^n

result = m*vector([x0, x1])

io.recvuntil('OTP:')
io.sendline(str(result[0]).encode())

#print(io.recvall())

io.recvuntil('>')
io.sendline(b'1')
cf = int(io.recvline().decode().strip().split(' ')[2])

io.recvuntil('>')
io.sendline(b'2')
io.recvuntil('pt = ')
#pt1 = 2^512-2 #failed, have to choose a more normal number
pt1 = bytes_to_long(b'Z'*64)
io.sendline(long_to_bytes(pt1))
c1 = int(io.recvline().decode().strip().split(' ')[2])

io.recvuntil('>')
io.sendline(b'2')
io.recvuntil('pt = ')
#pt2 = 2^512-4 #failed, have to choose a more normal number
pt2 = bytes_to_long(b'X'*64)
io.sendline(long_to_bytes(pt2))
c2 = int(io.recvline().decode().strip().split(' ')[2])

mx = ((c1-c2)*gmpy2.invert(pt1-pt2, p))%p
flag = ((cf-c1)*gmpy2.invert(mx, p)%p + pt1)%p

print(bytes.fromhex(hex(flag)[2:]))
#b'HTB{C4lcU1u5_m33t5_Cryp70_c4n_y0u_8e1i3ve_17???}'
