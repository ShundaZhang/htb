def movAttack(G, Q):
    k = 1
    while (p**k - 1) % E.order():
        k += 1

    Ee = EllipticCurve(GF(p**k, 'y'), [a, b])

    R = Ee.random_point()
    m = R.order()
    d = gcd(m, G.order())
    B = (m // d) * R

    assert G.order() / B.order() in ZZ
    assert G.order() == B.order()

    Ge = Ee(G)
    Qe = Ee(Q)

    n = G.order()
    alpha = Ge.weil_pairing(B, n)
    beta = Qe.weil_pairing(B, n)

    print('Computing log...')
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

nQ = movAttack(G, Q)

print(nQ)

