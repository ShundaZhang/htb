#https://chovid99.github.io/posts/cyber-apocalypse-2023-crypto/#converging-visions
#https://github.com/jvdsn/crypto-attacks/blob/master/attacks/ecc/smart_attack.py

from pwn import *

context.log_level = 'debug'

ip, port = '68.183.37.122', 30347
io = remote(ip, port)

high = 2**256
low = 2**255

'''
while high - low >= 0:
	print(f'high, low = {high, low}')
	print(f'diff = {high - low}')
	if high - low == 0 :
		break
	mid = (high + low)//2
	io.sendlineafter(b'> ', b'1')
	io.sendlineafter(b'x: ', str(mid).encode())
	out = io.recvline()
	if b'greater' in out:
		high = mid
	else:
		low = mid + 1
p = high

print(f'recovered p = {p}')
'''
#91720173941422125335466921700213991383508377854521057423162397714341988797837

p = 91720173941422125335466921700213991383508377854521057423162397714341988797837

#1. Setup Point
#2. Receive new point
#3. Find true point
#> 1
x1, y1 = 2222, 51905877010927770223814226825586016366266471294683356118822223333358631959312
#> 2
x2, y2 = 29262882672682253155666407326094365722244738499849724283747970668840315937134, 97054301871949590985143840761189236394278080647872583473067783758707938985526

a = (y1**2 - y2**2 - x1**3 + x2**3)*pow(x1-x2, -1, p)%p
b = (y1**2 - x1**3 - a*x1)%p

E = EllipticCurve(GF(p), [a, b])
print(f'E.order() = {E.order()}')
print(f'p = {p}')

# Lifts a point to the p-adic numbers.
def _lift(E, P, gf):
	x, y = map(ZZ, P.xy())
	for point_ in E.lift_x(x, all=True):
		_, y_ = map(gf, point_.xy())
		if y == y_:
			return point_


def attack(G, P):
	"""
	Solves the discrete logarithm problem using Smart's attack.
	More information: Smart N. P., "The discrete logarithm problem on elliptic curves of trace one"
	:param G: the base point
	:param P: the point multiplication result
	:return: l such that l * G == P
	"""
	E = G.curve()
	gf = E.base_ring()
	p = gf.order()
	assert E.trace_of_frobenius() == 1, f"Curve should have trace of Frobenius = 1."

	E = EllipticCurve(Qp(p), [int(a) + p * ZZ.random_element(1, p) for a in E.a_invariants()])
	G = p * _lift(E, G, gf)
	P = p * _lift(E, P, gf)
	Gx, Gy = G.xy()
	Px, Py = P.xy()
	return int(gf((Px / Py) / (Gx / Gy)))

def setup_point(x):
	io.sendlineafter(b'> ', b'1')
	io.sendlineafter(b'x: ', str(x).encode())
	_, x1, y1 = eval(io.recvline().strip())
	return x1, y1

def next_point():
	io.sendlineafter(b'> ', b'2')
	io.recvline()
	_, x, y = eval(io.recvline().strip())
	return x, y

x1, y1 = setup_point(x1)
x2, y2 = next_point()

G = E(x1, y1)
P = E(x2, y2)
enc_seed = attack(G, P)

m = p * 6089788258325039501929073418355467714844813056959443481824909430411674443639248386564763122373451773381582660411059922334086996696436657009055324008041039
#m is too big, we just try p
print(f'recovered enc_seed: {enc_seed}') # enc_seed = seed^2 mod p

inc = int.from_bytes(b"Coordinates lost in space", "big")

Z = IntegerModRing(p)
seeds_1 = Z(enc_seed).nth_root(2, all=True) # There will be two roots

#1. have to choose one of the roots, 50% lucky, try several times
#2. why can just mod p but not mod m??
next_seed = (a * pow(seeds_1[1], 3) + b * seeds_1[1] + inc)%p 

setup_point(x1)

prediction_point = G*int(next_seed)
print(f'prediction: {prediction_point}')
io.sendlineafter(b'> ', b'3')
io.sendlineafter(b'x: ', str(prediction_point[0]).encode())
io.sendlineafter(b'y: ', str(prediction_point[1]).encode())
print(io.recvall())
#HTB{0Racl3_AS_a_f3A7Ur3_0n_W3aK_CURV3_aND_PRN9??_7H3_s3cur17Y_0F_0uR_CRyP70Sys73M_w1LL_c0LLAp53!!!}
