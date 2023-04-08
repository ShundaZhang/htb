from pwn import *

ip, port = '134.122.104.91', 32475

io = remote(ip, port)
io.close()
