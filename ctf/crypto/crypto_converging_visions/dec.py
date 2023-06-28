#https://chovid99.github.io/posts/cyber-apocalypse-2023-crypto/#converging-visions
#https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/smart_attack.py

#Use python to speed up (save memory in cloud), get p and run sage in local machine...

from pwn import *

context.log_level = 'debug'

ip, port = '159.65.52.96', 32060
io = remote(ip, port)

high = 2**256
low = 2**255

while high - low >= 0:
	print(f'high, low = {high, low}')
	print(f'diff = {high - low}')
	if high - low == 0 :
		break
	mid = (high + low)//2
	io.sendlineafter(b'> ', b'1')
	io.sendlineafter(b'x : ', str(mid).encode())
	out = io.recvline()
	if b'greater' in out:
		high = mid
	else:
		low = mid + 1
p = high

print(f'recovered p = {p}')
#98807859381918657537428263421507671098277046895420042063839316200156326157051

