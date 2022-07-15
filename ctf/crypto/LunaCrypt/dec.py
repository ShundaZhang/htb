import math

strchr = lambda x: chr(x)
strbyt = lambda x, y=0: ord(x[y])
bitlst = lambda x, y: x << y
bitrst = lambda x, y: x >> y
bitext = lambda x, y, z=1: bitrst(x, y) & int(math.pow(2, z) - 1)
bitxor = lambda x, y: x ^ y
bitbor = lambda x, y: x | y
btest  = lambda x, y: (x & y) != 0

FL_NEGATE = bitlst(1, 1)
FL_UNUSED3 = bitlst(1, 2)
FL_XORBY6B = bitlst(1, 3)
FL_XORBY3E = bitlst(1, 4)
FL_UNUSED2 = bitlst(1, 5)
FL_SWAPBYTES = bitlst(1, 6)
FL_UNUSED1 = bitlst(1, 7)

def ValidateChar(char):
	if type(char) is str and len(char) == 1:
		char = strbyt(char)
	return char

def CheckFlag(f, flag):
	return btest(f, flag)

def DSwapChar(char):
	char = ValidateChar(char)
	THIS_MSB = bitext(char, 4, 4)
	THIS_LSB = bitext(char, 0, 4)

	return strchr(bitbor(bitxor(THIS_MSB, 0x0B), bitxor(bitlst(THIS_LSB, 4), 0xD0)))

def XorBy6B(char):
	char = ValidateChar(char)

	return strchr(bitxor(char, 0x6B))

def XorBy3E(char):
	char = ValidateChar(char)

	return strchr(bitxor(char, 0x3E))

def NegateChar(char):
	char = ValidateChar(char)

	return strchr(255 - char)

def RecoverFlag(flag):
	flag = ValidateChar(flag)
	return bitxor(flag, 0x4A)

def DecryptCharacter(char, flag):
	char = ValidateChar(char)
	flag = RecoverFlag(flag)
	if CheckFlag(flag, FL_XORBY3E):
		char = XorBy3E(char)
	if CheckFlag(flag, FL_XORBY6B):
		char = XorBy6B(char)
	if CheckFlag(flag, FL_NEGATE):
		char = NegateChar(char)
	if CheckFlag(flag, FL_SWAPBYTES):
		char = DSwapChar(char)
	
	if type(char) is str and len(char) == 1:
		return char
	else:
		return chr(char)


a = [108,182,82,176,167,158,69,222,39,102,234,14,241,16,10,218,160,108,76,234,225,224,1,12,97,122,114,90,10,90,250,14,155,80,101,186,97,218,115,218,207,76,190,174,196,84,192,144]

c = a[::2]
f = a[1::2]

cx = [chr(i) for i in c]
fx = [chr(i) for i in f]

for i in range(len(cx)):
	print DecryptCharacter(cx[i], fx[i]),

#HTB{Lun4_Lu4_L4t1n_M00n}
