from pwn import *

ip, port = '157.245.43.189', 31152
io = remote(ip, port)

io.recvuntil('Message for encryption:')
io.sendline('')
buf = io.recvline()
print(buf)
print(buf[1:-1])
