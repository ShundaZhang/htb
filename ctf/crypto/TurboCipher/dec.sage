from pwn import *

context.log_level = 'debug'

ip,port='144.126.228.151',31590

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

print(io.recvall())
