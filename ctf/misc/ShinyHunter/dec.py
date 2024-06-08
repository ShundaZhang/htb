from pwn import *

ip, port = '94.237.52.198', 51000


def lucky_try(ip, port, choice, index):
	found = 0
	io = remote(ip, port)
	io.recvuntil('Enter your name: ')
	io.sendline('X')
	io.recvuntil('Choose your starter Poketmon (1, 2, or 3): ')
	io.sendline(str(choice))
	buf = io.recvall()
	if 'HTB{' in buf:
		print(buf)
		found = 1
	else:
		print(f'{index} + {choice}: Not Found!')
	
	io.close()
	if found == 1:
		return True
	else:
		return False

i = 0
while True:
	if lucky_try(ip, port, 1, i) or lucky_try(ip, port, 2, i) or lucky_try(ip, port, 3, i):
		break
	i += 1
