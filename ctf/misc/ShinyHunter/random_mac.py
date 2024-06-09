import random
import gmpy2

def get_mac():
	mac = [random.randint(0x00, 0xff) for _ in range(6)]
	return ":".join("{:02x}".format(x) for x in mac)

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


device_mac = get_mac()

s = int(device_mac.replace(":", ""), 16)
a=1664525
c=1013904223
m=2**32
#y=1685
y = 4294964760

#a*(x+s)+c % m == y
#x = (((y-c)%m * a^-1) %m - s)%m 

x = ((y-c)%m * gmpy2.invert(a,m) - s)%m
print(f'formatted_time {x}')

print(f'traget seed: {y}')
seed = lcg(x+s)
print(f'recovered seed: {seed}')

#find the first seed meet our goal

for i in range(1000):
	seed = lcg(i+s)
	s1, s2 = is_seed(seed)
	if s1 != -1 and s2 != -1:
		print(f'Found {i}!')
	
