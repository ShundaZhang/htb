from pwn import *

#context.log_level = 'debug'

c = 0x8ce7a727c4a70470aa3d6b872f82ef26c8ff5c7820d5790aa53e9dbd1d9f328c8847b268813c9c1bca54c3a892c9a848e95f37bb3c467971af3a29a2ea706dde662caa595728ff094b6c3c66bdddc6733f428c5b80ef81c0dbfa7f4419f08cc6ce7cde30df2004ff8037baf3647cf1813c577ca1303fb92f319418e3ed4f36dc49d33e7d92471a53ae2c029cdfa2b9034a6cb8f3b468f9154a6755aff13d923bd7e6d49d2e8db3b34b6135675d1a11236e7c8641716c54fe91dc26677200232baae8a9d5293109d73336f239d9a8905c7a1b81aec57d3df55f3302c0cddbcd742ea302c1157fa7b1138b36acd82cd73142b4fbf26099153616cd0d244dea2e1c

ip, port = '161.35.36.167', 31765
io = remote(ip, port)

def detect(x):
	io.recvuntil('Option:')
	io.sendline('2')
	io.recvuntil('Plaintext:')
	io.sendline(str(x))
	buf = io.recvline().strip()
	if 'Thanks for the message!' in buf:
		return True
	else:
		return False

low = c
high = c*2
mid = 0

while low <= high:
	mid = (high + low) // 2

	if detect(mid-1) and detect(mid):
		low = mid + 1
		print mid
		print 'Up'

	elif not detect(mid-1) and not detect(mid):
		high = mid - 1
		print mid
		print 'Down'

	elif detect(mid-1) and not detect(mid):
		print mid
		print 'Hit!!!'
		break
else:
	print 'Not Found!'

