from Crypto.Util.number import *

k1 = 24299410991
k2 = 95721551380


x = k1
y = k2**2

for i in range(10):
	f = x*(y**i)
	print(long_to_bytes(f))
