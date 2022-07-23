

M = 17101937747109687265202713197737423
A = 2
B = 3
F = FiniteField(M)
E = EllipticCurve(F,[A,B])

P = (3543321030468950376213178213609418, 14807290861072031659976937040569354)
Q = (5140071671361386753880669417781067, 12952516339987872946099866597314047)

P = E.point(P)
Q = E.point(Q)
print(P.order())

#17101937747109687496599931614463506 = 2 * 3 * 7^2 * 1487 * 3761 * 176489 * 439693 * 3113111 * 43054831
primes = [2 , 3 , 49, 1487 , 3761 , 176489 , 439693 , 3113111 , 43054831]

dlogs = []
for fac in primes:
	t = int(P.order()) / int(fac)
	dlog = discrete_log(t*Q, t*P, operation="+")
	dlogs += [dlog]
	print("factor: "+str(fac)+", Discrete Log: "+str(dlog)) #calculates discrete logarithm for each prime order

d = crt(dlogs, primes)
print(d)
