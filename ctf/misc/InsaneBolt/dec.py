from pwn import *
import sys

context.log_level = 'debug'

ip, port = sys.argv[1].split(':')
io = remote(ip, int(port))

io.recvuntil('>')
io.sendline(b'2')
io.recvline()
buf = io.recvuntil('>').decode().split('\n')[:-2]
print(buf)
