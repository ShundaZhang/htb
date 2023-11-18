import sys

arguments = sys.argv[1:]  

a = int(arguments[0])
b = int(arguments[1])

Gx = int(arguments[2])
Gy = int(arguments[3])

Gnx = int(arguments[4])
Gny = int(arguments[5])

p = int(arguments[6])


E = EllipticCurve(GF(p), [a, b])
n = E.order()
print("Order:", n)

if p == n:
	print('Found p == n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
	exit(0)

for k in range(1,10):
	if (p**k - 1) % n == 0:
		print('k in MOV:', k)
		print('Found MOV!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		exit(0)

print('Failed...')
exit(-1)
