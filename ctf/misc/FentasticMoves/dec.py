from pwn import *

ip, port = "167.99.85.216", 30300
io = remote(io, port)

print(io.recvall())
