from pwn import *

'''
Added 11 chars (22 hex digital), blocks number changed from 3 to 4.

Flag len == 25 (12+11+25 == 48)

+--------+   +-----------+   +------------+   +---------+   +-----------+
| 12 + 4 | + | 16 oracle | + | 9 + 7 flag | + | 16 flag | + | X}\x0e*14 |
+--------+   +-----------+   +------------+   +---------+   +-----------+
+--------+   +-----------+   +------------+   +---------+   +-----------+
| 12 + 4 | + | 16 oracle | + | 10+ 6 flag | + | 16 flag | + | XX}\x0d*13|
+--------+   +-----------+   +------------+   +---------+   +-----------+
......

'''

ip, port = "206.189.117.48",31247
io = remote(ip, port)

flag = 'r0k3n_0r@c1e!!!}'
#oracle0 = ('}'+'\x0e'*14).encode('hex')
oracle0 = 'r0k3n_0r@c1e!!!'.encode('hex')
#for i in range(24):
for i in range(15,24,1):
	io.recvuntil('>')
	io.sendline('00'*4+'00'+oracle0+(9+i)*'00')
	oracle_target = io.recvline().strip()[4*32:5*32]
	for x in range(256):
		io.recvuntil('>')
		io.sendline('00'*4+chr(x).encode('hex')+oracle0+(9+i)*'00')
		oracle = io.recvline().strip()[32:64]
		if oracle == oracle_target:
			flag = chr(x)+flag
			print flag
			if i < 14:
				oracle0 = chr(x).encode('hex') + oracle0[:2*(i+1)] + chr(14-(i+1)).encode('hex')*(14-(i+1))
			else:
				oracle0 = chr(x).encode('hex') + oracle0[:-2]
			break
		#else:
		#	print i,x

print flag
#HTB{7h3_br0k3n_0r@c1e!!!}
