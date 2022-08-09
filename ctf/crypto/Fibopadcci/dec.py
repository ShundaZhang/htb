from pwn import *

fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 121, 98, 219, 61]

def bitflip(c,buf,index,padding,io):
	for i in range(256):
		b = hex(i)[2:].zfill(2)
		x = buf[:32-2*index]+b+padding
		io.sendline('1')
		io.recvuntil('Enter your ciphertext in hex:')
		io.sendline(c)
		io.recvuntil('Enter the B used during encryption in hex:')
		io.sendline(x)
		rbuf = io.recvuntil('Your option:')
		if 'Message successfully sent!' in rbuf:
			print('=================================')
			print('index: ',index)
			print('Hit!: ', b)
			print('keybits: ', hex(i^fib[0])[2:].zfill(2))
			return hex(i^fib[0])[2:].zfill(2)
		else:
			print(index,i)

#ip,port = '206.189.21.202',31254
ip,port = '127.0.0.1',1337
io = remote(ip, port)

io.recvuntil('Your option:')

io.sendline('0')

buf = io.recvuntil('Your option:')
buf = buf.split('\n')

c = buf[0].split(' ')[2]
a = buf[1].split(' ')[1]
a2 = 'HTB{th3_s3crt_A}'

#block1
#iv = buf[2].split(' ')[1]
#c1 = c[:32]
#c1 = xor(c1.decode('hex'),a.decode('hex'),a2).encode('hex')

#block2
#iv = c[:32]
#c1 = c[32:64]
#p1 = 'HTB{cU5t0m_p4dd1'
#c1 = xor(c1.decode('hex'),p1,a2).encode('hex')

#block3
iv = c[32:64]
c1 = c[64:96]
p2 = 'Ng_w0nT_s4v3_y0u'
c1 = xor(c1.decode('hex'),p2,a2).encode('hex')

#print(buf)
#print(iv)

padding = ''
keystream = ''
buf0 = '0'*32
for index in range(1,17,1):
	keyx = bitflip(c1, buf0, index, padding, io)
	keystream = keyx + keystream
	padding = ''
	if( index < 16 ):
		for j in range(index):
			padding += hex(int(keystream[2*j:2*j+2],16)^(fib[j+1]))[2:].zfill(2)
	print('-----------------------------------')
	print('keystream: ',keystream)
	print('padding: ',padding)

#xor(keystream,iv)

print('**************************************')
print(iv)
print(keystream)

flag = ''
for i in range(16):
	flag += chr(int(keystream[2*i:2*i+2],16)^int(iv[2*i:2*i+2],16))
print(flag)

'''
**************************************
eb133da0d88ee2c02a5be2206cd6eff0
a3477fdbbbdbd7b41a36bd5058b28bc1
HTB{cU5t0m_p4dd1
**************************************
2ebbbe548d2712c5092b1d94f2b8ca8b
60dce123bd49469a7a1f6ba7adc1fafe
Ng_w0nT_s4v3_y0u
**************************************
5a94285b1e64cce05c4f73f2bbf05e92
05e0606a6d3b98d1317c2cc893d11eef
_tH1s_T1m3_:(!@}

HTB{cU5t0m_p4dd1Ng_w0nT_s4v3_y0u_tH1s_T1m3_:(!@}
'''
