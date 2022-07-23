'''
sage dec.sage
17101937747109687496599931614463506
factor: 2, Discrete Log: 1
factor: 3, Discrete Log: 1
factor: 49, Discrete Log: 33
factor: 1487, Discrete Log: 284
factor: 3761, Discrete Log: 2449
factor: 176489, Discrete Log: 65565
factor: 439693, Discrete Log: 286441
factor: 3113111, Discrete Log: 1090561
factor: 43054831, Discrete Log: 33296397
9247030231

'''

#9247030231 = 73 * 7699 * 16453

from ecdsa import ellipticcurve as ecc
from Crypto.Util.number import isPrime

def rotate(seed):
	x, y, z = seed
	x = (171 * x) % 30269
	y = (172 * y) % 30307
	z = (170 * z) % 30323
	seed = x, y, z
	return seed

def goToNextStation(seed):
	while True:
		seed = rotate(seed)
		x, y, z = seed
		if(isPrime(x) and isPrime(y) and isPrime(z)):
			d = x * y * z
			new_point = d * G
			return int(new_point.x()), int(new_point.y())

p = 17101937747109687265202713197737423
Gx = 3543321030468950376213178213609418
Gy = 14807290861072031659976937040569354
ec_order = 17101937747109687496599931614463506
E = ecc.CurveFp(p, 2, 3)
G = ecc.Point(E, Gx, Gy, ec_order)

seed = (73, 7699, 16453)
print goToNextStation(seed)

'''
Enter the x coordinate: 10796485262811059255140200629092500
Enter the y coordinate: 3612498440033028050630345044141525
You found your lover. Here is your flag: HTB{PRNGs,math,ECC_and_crypto_>_love._Love_is_pain}
'''
