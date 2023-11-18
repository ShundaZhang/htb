from pwn import *

ip, port = '206.189.24.162',32136
io = remote(ip, port)

io.recvuntil('Hello Cryptographer, please enter the coefficients of the quadratic equation to proceed, hint: ')
buf = io.recvline()

print(buf)
