#!/usr/bin/python3

from pwn import *

context.log_level = 'debug'

ip, port = '139.59.174.176', 30781
io = remote(ip, port)

io.recvuntil(']: ')
buf = io.recvline()
print(buf.decode().split(' '))
print(buf.decode().split(' ')[:-2])
