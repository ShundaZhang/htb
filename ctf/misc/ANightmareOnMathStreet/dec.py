#!/usr/bin/python3

from pwn import *

context.log_level = 'debug'

ip, port = '139.59.174.176', 30781
io = remote(ip, port)

io.recvuntil(']: ')
buf = io.recvline()
print(buf.decode())
print(buf.decode()[:-5])
s = buf.decode()[:-5]
s = s.replace('(', '( ')
s = s.replace(')', ' )')
print(s)
