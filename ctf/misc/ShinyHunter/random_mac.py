import random
import gmpy2

def get_mac():
	mac = [random.randint(0x00, 0xff) for _ in range(6)]
	return ":".join("{:02x}".format(x) for x in mac)

def lcg(seed, a=1664525, c=1013904223, m=2**32):
	return (a * seed + c) % m

device_mac = get_mac()

s = int(device_mac.replace(":", ""), 16)
print(s)
a=1664525
c=1013904223
m=2**32
#y=1685
y = 4294964760

#a*(x+s)+c % m == y
#x = (((y-c)%m * a^-1) %m - s)%m 

x = ((y-c)%m * gmpy2.invert(a,m) - s)%m
print(x)
