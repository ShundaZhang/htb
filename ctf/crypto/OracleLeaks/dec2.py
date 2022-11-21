from pwn import *
import time
from Crypto.Util.number import bytes_to_long

def int_to_bytes(val):
	plaintext = hex(val)[2:]
	if len(plaintext)%2 == 1:
		plaintext = "0"+plaintext
	return bytes.fromhex(plaintext)
	
		

#p = process(["python3", "chall.py"])
p = remote("134.209.19.24", 30140)

started = p.recvuntil(">")
p.sendline("1")
p.recvuntil("(n,e): (")
nums = p.recvline().decode("utf-8").replace(")","").replace(" ","").replace("'","")
n, e = nums.split(",")
n = int(n, 16)
e = int(e, 16)
#p.interactive()
p.recvuntil(">")
p.sendline("2")
p.recvuntil("Encrypted text:")
text = p.recvline()
text = text.decode("utf-8").strip()
ct = int(text, 16)
#start = time.time()

cached = dict()
queries = 0

#This tests a number and gets the value for its decrypted length
def test_num(x):
	global cached
	global queries
	if x in cached:
		#print("CACHED!")
		return cached[x]
	p.sendline("3")
	to_send = x
		
	p.sendline(int_to_bytes(x).hex())
	p.recvuntil("Length:")
	length = int(p.recvline().decode("utf-8").strip())
	cached[x] = length
	queries += 1
	return length
	
#This searches for a small value that just barely rolls over N
#Note, sometimes it isn't actually the smallest value, for some reason it does less queries this way/
def base_divide(x):
	byte_size = test_num(x)
	maximum = 0
	#print("Queries start of base divide", queries)
	for i in range(int((127-byte_size)*8), 10000):
		test =(pow(int(2**i), e, n) * x) % n
		#print(test, i, 2**i)
		#print()
		maximum = 2 ** i
		if test_num(test) == 128:
			break
	#print(maximum)
	bottom = maximum//2
	top = maximum
	#print("Queries end of find offset", queries)
	#print(bottom, top)
	while top > bottom + 1:
		mid = (top + bottom) // 2
		#print(bottom, top, mid)
		test = (pow(mid, e, n) * x) % n
		if test_num(test) == 128:
			top = mid - 1
		else:
			bottom = mid + 1
	#print(bottom, top, mid)
	answer = 0
	#print("Queries  mid find N range", queries)
	for i in range(top, bottom-2, -1):
		test = (pow(i, e, n) * x) % n
		#print(test_num(test), byte_size)
		test_num(test)
		if test_num(test) == 127:
			answer = i
			break
	#print("Queries  end find N range", queries)
	#print(i)
	lowest = (256**127) // (answer+1)
	highest = ((256**127) // answer) + 1
	#print(hex(lowest))
	#print(hex(highest))
	ndiv_low = n // highest
	ndiv_hi = n // lowest + 1
	
	bottom = ndiv_low
	top = ndiv_hi
	#print("N RANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	#print(bottom, top)
	while top > bottom + 1:
		mid = (top + bottom) // 2
		test = (pow(mid, e, n) * x) % n
		#print(bottom, top, mid, byte_size, test_num(test))
		test_num(test)
		if test_num(test) < 128:
			top = mid - 1
			if test_num(test)<127:
				#print("early exit", queries)
				return mid, test
		else:
			bottom = mid + 1
	#print(bottom, top)
	#print("Queries  end find final", queries)
	answer = 0
	for i in range(bottom, top+3):
		test = (pow(i, e, n) * x) % n
		#print(bottom, top, mid, byte_size, test_num(test))
		test_num(test)
		if test_num(test) <= byte_size:
			answer = i
			#print("Queries  end divide", queries)
			return answer, test

#print(n, e)
#print(text)
pathed = []
multiples = []
for z in range(60):
	mul1, ct = (1, ct)
	pathed.append(ct)
	mul2, ct = base_divide(ct)
	pathed.append(ct)
	multiples.append((mul1, mul2))
	#This performs the reconstruction of the original plaintext after finding a small value to multiply by pt and the high bits of pt
	#print("="*100, test_num(ct))
	test_num(ct)
	if test_num(ct) < 64:
		break
	minimum = n//multiples[-1][1]
	maximum = n//(multiples[-1][1] - 1)
	minimum *= multiples[-1][0]
	maximum *= multiples[-1][0]  
	#print("-"*100) 
	for a, b in reversed(multiples[:-1]):
		minimum = (n + minimum)// b
		maximum = (n + maximum)// b + 1
		minimum *= a
		maximum *= a 
	#print(hex(minimum))
	#print(hex(maximum))
	str = bytes.fromhex("0"+hex(minimum)[2:])
	print(str)
	matched = 0
	for i in range(len(hex(minimum))):
		if hex(minimum)[i] == hex(maximum)[i]:
			matched += 1
		else:
			break
	#print("-"*100, 1050*((time.time() - start)/queries), matched) 
	if minimum +2 > maximum:
		break
#print(trial_reduce(ct))
#HTB{m4ng3r5_4tt4ck_15_c001_4nd_und3rv4lu3d_341m3f}
