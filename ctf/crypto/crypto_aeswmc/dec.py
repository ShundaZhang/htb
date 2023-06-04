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
b2 = xor(c1, b1)
io.sendline('00'*6+xor(c1, b1).encode('hex'))
buf = io.recvline().strip()
c2 = buf.decode('hex')
c2 = xor(c2, c1)

io.recvuntil(message)
io.sendline('00'*6+xor(c1,b1).encode('hex')+xor(c2,b2).encode('hex'))
flag = io.recvline()

print flag
#HTB{AES_cu570m_m0d35_4nd_hm4cs_423_fun}
