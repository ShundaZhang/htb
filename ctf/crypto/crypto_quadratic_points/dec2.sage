def movAttack(G, Q):
    k = 1
    while (p**k - 1) % E.order():
        k += 1

    Ee = EllipticCurve(GF(p**k, 'y'), [a, b])

    R = Ee.random_point()
    m = R.order()
    d = gcd(m, G.order())
    B = (m // d) * R

    if not (G.order() / B.order() in ZZ):
    	return 0
    if G.order() != B.order():
    	return 0

    Ge = Ee(G)
    Qe = Ee(Q)

    n = G.order()
    alpha = Ge.weil_pairing(B, n)
    beta = Qe.weil_pairing(B, n)

    #print('Computing log...')
    nQ = beta.log(alpha)
    return nQ


a = 100000000000000000 
b = 0 
Gx = 146316399546 
Gy = 17250030801 
Qx = 630879386133 
Qy = 397653533092 
p = 695814196879

E = EllipticCurve(GF(p), [a, b])

G = E(Gx, Gy)
Q = E(Qx, Qy)

QA = []

'''
for _ in range(10**7):
    nQ = movAttack(G, Q)
    if nQ == 0:
        continue
    if nQ not in QA:
        QA.append(nQ)
        print(QA)

factors = [4412475261, 510459163901, 162552065461, 5993871163, 92970645773, 75575290851, 32086903546, 23389226085, 5532047581, 2453223701, 144105791, 458985506, 214079061, 1249683457, 605929373, 913811761, 298046985, 493972141]

print(G)
print(Q)
for i in range(len(factors)):
	Gn = factors[i]*G
	print(Gn)

k = discrete_log(Q, G, G.order(),operation='+')  
print("k:", k)
k = discrete_log(-G, G, G.order(),operation='+')  
print("k:", k)

#k: 510459163901
#k: 695814196879

print(G)
print(Q)
Gn = 510459163901*695814196879*695814196879*695814196879*695814196879*G
print(Gn)
Gn = 695814196879*695814196879*G
print(Gn)
'''


#100000000000000000 23349281323106688 631998598259 137220533053 237545077271 479462837147 670052303779

a = 100000000000000000
b = 23349281323106688
Gx = 631998598259
Gy = 137220533053
Qx = 237545077271
Qy = 479462837147
p = 670052303779

E = EllipticCurve(GF(p), [a, b])

G = E(Gx, Gy)
Q = E(Qx, Qy)

k = discrete_log(Q, G, operation='+')
print("k:", k)
k = discrete_log(-G, G, operation='+')
print("k:", k)

k1 = 24299410991
k2 = 95721551380

print(G)
print(Q)
Gn = k1*k2**2*G
print(Gn)
Gn = k1*k2**4*G
print(Gn)

