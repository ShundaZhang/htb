#!/usr/bin/python3

from pwn import *
import gmpy2

#context.log_level = 'debug'

#Input message as hex: 00
N = 2**1024

key = [1]*64

#print(sum(key))
ip,port = '167.99.197.168',30589
io = remote(ip,port)

io.recvuntil('>')
io.sendline('2')
io.recvuntil('Input message as hex:')
io.sendline('00')  #any even number should be OK, observe the result, odd -> even is not in key

for _ in range(64):
	buf = io.recvline().strip()
	#print(buf)
	x,y = buf.decode().split(', ')
	x = int(x[1:])
	y = int(y[:-1])
	print(x,y)
