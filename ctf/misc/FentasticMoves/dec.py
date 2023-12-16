from pwn import *

ip, port = "167.99.85.216", 30300
io = remote(ip, port)

print(io.recvall())
