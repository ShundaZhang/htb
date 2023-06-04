from pwn import *

context.log_level = 'debug'

message = 'Property: '

ip, port = sys.argv[1].split(':')
io = remote(ip, int(port))

io.recvuntil(message)
io.sendline('00'*6)
buf = io.recvline().strip()
c1 = buf.decode('hex')

io.recvuntil(message)
b1 = message+'\x00'*6
b2 = b1+xor(c1, b1)
io.sendline('\x00'*6+xor(c1, b1))
buf = io.recvline().strip()
c2 = buf.decode('hex')

io.recvuntil(message)
io.sendline('\x00'*6+xor(c1,b1)+xor(c2,b2))
flag = io.recvline()

print flag
