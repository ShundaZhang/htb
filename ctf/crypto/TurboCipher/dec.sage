from pwn import *

context.log_level = 'debug'

ip,port='144.126.228.151',31590

io = remote(ip,port)

