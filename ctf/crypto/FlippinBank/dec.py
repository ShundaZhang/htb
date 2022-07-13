from pwn import *

a = 'c7816fbc60f78b554fe87b857d428289732e5c87fef805b985525301c66cef37c86c40b0e3ed207950b5a39cbf330b95'


for i in range(256):
	io = remote('138.68.150.148', 30694)
	
	io.recvuntil('username:')
	io.sendline('admin')
	io.recvuntil('admin\'s password:')
	io.sendline('x0ld3n_b0y')
	io.recvuntil('enter ciphertext:')
	c = a[:30]+hex(i)[2:].zfill(2)+a[32:]
	io.sendline(c)
	buf = io.recvall()
	print buf
	if 'Logged in successfully!' in buf:
		break
	else:
		print i
	
	io.close()

'''
149
[+] Opening connection to 138.68.150.148 on port 30694: Done
[+] Receiving all data: Done (64B)
[*] Closed connection to 138.68.150.148 port 30694
 Logged in successfully!
Your flag is: HTB{b1t_fl1pp1ng_1s_c00l}
'''
