import itertools

def small_roots(f, bounds, m=1, d=None):
	if not d:
		d = f.degree()

	R = f.base_ring()
	N = R.cardinality()
	
	f /= f.coefficients().pop(0)
	f = f.change_ring(ZZ)

	G = Sequence([], f.parent())
	for i in range(m+1):
		base = N^(m-i) * f^i
		for shifts in itertools.product(range(d), repeat=f.nvariables()):
			g = base * prod(map(power, f.variables(), shifts))
			G.append(g)

	B, monomials = G.coefficient_matrix()
	monomials = vector(monomials)

	factors = [monomial(*bounds) for monomial in monomials]
	for i, factor in enumerate(factors):
		B.rescale_col(i, factor)

	B = B.dense_matrix().LLL()

	B = B.change_ring(QQ)
	for i, factor in enumerate(factors):
		B.rescale_col(i, 1/factor)

	H = Sequence([], f.parent().change_ring(QQ))
	for h in filter(None, B*monomials):
		H.append(h)
		I = H.ideal()
		if I.dimension() == -1:
			H.pop()
		elif I.dimension() == 0:
			roots = []
			for root in I.variety(ring=ZZ):
				root = tuple(R(root[var]) for var in f.variables())
				roots.append(root)
			return roots

	return []


'''
This is your lucky point:
{"x": "0x22c317eecf1799f74facf0c5b47aee31479b073d33900b976710f3d523d8ffed9cb3e27c2cb67f06877a9485ff6e7277981d45069330edbca3de929f6ac1f363", "y": "0xc08a052f2c56484ee1be80f5b26bd42d8389c0a24039c5db12c2f88da225b631797695f2aff5d9de8684550f16f7a189a9b61f1cb3337420e148040b55555bbc"}
1. Get path parameters
2. Try to exit the labyrinth
> 1
{"p": "0xda2c5dde59d6534498abb2897cc21fe6910c9a29ca0b1341cecd586e99afc049fe15bf6743756e54766e8c75e1708b6335b6332153d84d3d060958b2a155f44f", "a": "0x67d252d9c16a0a000a07618ba69c6ac490b354b33ee3174d605ddcdc3d6df9e81878", "b": "0x270abb04095c001e68aafb4bf9dc9703397464595b9b544192be4fcf5fd55bd7ea5fc"}
'''

p = 0xda2c5dde59d6534498abb2897cc21fe6910c9a29ca0b1341cecd586e99afc049fe15bf6743756e54766e8c75e1708b6335b6332153d84d3d060958b2a155f44f
a = 0x67d252d9c16a0a000a07618ba69c6ac490b354b33ee3174d605ddcdc3d6df9e81878
b = 0x270abb04095c001e68aafb4bf9dc9703397464595b9b544192be4fcf5fd55bd7ea5fc

x = 0x22c317eecf1799f74facf0c5b47aee31479b073d33900b976710f3d523d8ffed9cb3e27c2cb67f06877a9485ff6e7277981d45069330edbca3de929f6ac1f363
y = 0xc08a052f2c56484ee1be80f5b26bd42d8389c0a24039c5db12c2f88da225b631797695f2aff5d9de8684550f16f7a189a9b61f1cb3337420e148040b55555bbc

'''
f(x) = x^3 - y^2 + (partial_a*2^r + c)*x + (partial_b*2^r + d) mod p
c and d is small, r is bruteforceable
bounds = [2^r, 2^r]
'''

for r in range(512//3, 2*512//3):
	P.<c,d> = PolynomialRing(Zmod(p))
	bound = 2^r
	f = x^3 - y^2 + (a*2^r + c)*x + (b*2^r + d) 
	bounds = (bound, bound)
	sols = small_roots(f, bounds, m = 7, d = 3)
	if (len(sols) > 0 ):
		for sol in sols:
			sol_a = int(sol[0]) + a*2^r
			sol_b = int(sol[1]) + b*2^r
			print(sol_a, sol_b)
		exit()

