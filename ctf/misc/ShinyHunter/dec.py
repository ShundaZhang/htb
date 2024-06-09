from pwn import *

#ip, port = '94.237.52.198', 51000
ip, port = '178.62.102.205', 1337
#ip, port = '127.0.0.1', 1337

def lcg(seed, a=1664525, c=1013904223, m=2**32):
        return (a * seed + c) % m

def is_seed(seed):
        natures = ["Adamant", "Bashful", "Bold", "Brave", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]
        random.seed(seed)
        tid = random.randint(0,65535)
        sid = random.randint(0,65535)
        for seedi in range(3):
                random.seed(seed+seedi)
                for _ in range(6):
                        random.randint(20,31)
                random.choice(natures)
                pid = random.randint(0,2**32-1)
                if ((tid ^ sid) ^ (pid & 0xFFFF) ^ (pid >> 16)) < 8:
                        print('Found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print(f'seed: {seed} + choice: {seedi}')
                        return seed, seedi
        return -1, -1

def lucky_try(ip, port):
	found = 0
	io = remote(ip, port)
	io.recvuntil('Mac Address: ')
	device_mac = io.recvline().decode().strip()

	s = int(device_mac.replace(":", ""), 16)
	a=1664525
	c=1013904223
	m=2**32

	s1 = -1
	s2 = -1
	x = 0

	for i in range(20,100):
		seed = lcg(i+s)
		s1, s2 = is_seed(seed)
		if s1 != -1 and s2 != -1:
			print(f'Found {i}!')
			x = i
			break
	if s1 == -1 or s2 == -1:
		io.close()
		return False

	choice = s2
	delta = 0

	io.recvuntil('Enter your name: ')
	sleep(x-18+delta)
	io.sendline('X')
	
	#For Debug: get fomatted_time
	#print(io.recvline())
	
	io.recvuntil('Choose your starter Poketmon (1, 2, or 3): ')
	io.sendline(str(choice))
	buf = io.recvall()
	if b'HTB{' in buf:
		print(buf)
		found = 1
	
	io.close()
	if found == 1:
		return True
	else:
		return False

i = 0
while True:
	if lucky_try(ip, port):
		break
	i += 1
