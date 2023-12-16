from pwn import *

ip, port = "167.99.85.216", 30300
io = remote(ip, port)

buf = io.recvuntil("What's the best move?")
print(buf)
