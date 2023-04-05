#!/usr/bin/python3

from pwn import *

context.log_level = 'debug'

ip, port = '139.59.174.176', 30781
io = remote(ip, port)

buf = io.recvuntil(']:')
print(buf.split(' '))
