import math

def log2(x):
	n = 0
	while x > 1:
		x = x / 2
		n += 1
	return n

def hb(binary_value):
	for i, bit in enumerate(bin(binary_value)[:1:-1]):
		if bit == '1':
			return i


with open('out.txt','r') as f:
	buf = f.read()

array = buf.split('\n')
for i in range(len(array)):
	x,y = array[i].strip().split(' ')
	x = int(x)
	y = int(y)

	if bin(x).count('1') == bin(y).count('1'):
		key = x|y
		#print bin(key)[2:].zfill(16)
		fh1 = str(hex(log2(key^x))[2:])+str(hex(log2(key^y))[2:])
		ch1 = fh1.decode('hex')
		fh2 = str(hex(log2(key^y))[2:])+str(hex(log2(key^x))[2:])
		ch2 = fh2.decode('hex')

		print fh1,ch1,fh2,ch2
	else:
		key = x&y
		h = hb(x^y)
		h1 = 2**h
		h2 = h1^x^y
		key1 = key|h1
		key2 = key|h2
		fh1 = str(hex(log2(key1^x))[2:])+str(hex(log2(key1^y))[2:])
		ch1 = fh1.decode('hex')
		fh2 = str(hex(log2(key2^x))[2:])+str(hex(log2(key2^y))[2:])
		ch2 = fh2.decode('hex')

		print fh1,ch1,fh2,ch2
		#print bin(key1)[2:].zfill(16), bin(key2)[2:].zfill(16)

'''
>>> chr(0x22)
'"'
>>> chr(0x33)
'3'
>>> chr(0x44)
'D'
>>> chr(0x55)
'U'
>>> chr(0x66)
'f'
>>> chr(0x77)
'w'

HTB{I_L0v3_VHDL_but_LOve_my_Sw33thear7_m0re} #Wrong
HTB{I_L0v3_VHDL_but_LOve_my_5w33thear7_m0re} #Correct! Ensure login successfully before submitting flag, otherwise will always fail!!
'''
