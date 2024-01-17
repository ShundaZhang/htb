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


N = 72741423208033405403492275698762968936514657314823442485453559870105200118330405900858299998747406127848670334407387228444029070060538220448699667905891284937839901536444798774307744865631349770845980738192442639071823803272283670943732769371979418893953521892212745135191661138195973757608889180051128601323
e = 65537
c = 0x4da0230d2b8b46e3a7065f32c46df019739cc002a208cc37767a82c3e94edfc3440fa4b24a32274e35d5ddceaa33505c4f2a57281c3a5d6d4db3a0dbdbb30dbf373241319ce4a7fdd1780b6bafc86e37d283c9f9787c567434e2fc29c988fb05fd411fe4453ea40eb45fc41a423839b485e238dd2530fba284e9b07a0bba6546

bounds = (2^20, 2^20)
roots = tuple(randrange(bound) for bound in bounds)
R = Integers(N)
P.<x, y> = PolynomialRing(R)
monomials = [(x*y)^e, -c]
f = sum(randrange(N)*monomial for monomial in monomials)
f -= f(*roots)
print(small_roots(f, bounds))

