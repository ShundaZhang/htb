

# This file was *autogenerated* from the file dec.sage
from sage.all_cmdline import *   # import sage library

_sage_const_35 = Integer(35); _sage_const_98 = Integer(98); _sage_const_434252269029337012720086440207 = Integer(434252269029337012720086440207); _sage_const_16378704336066569231287640165 = Integer(16378704336066569231287640165); _sage_const_377857010369614774097663166640 = Integer(377857010369614774097663166640); _sage_const_434252269029337012720086440208 = Integer(434252269029337012720086440208); _sage_const_1 = Integer(1); _sage_const_0x13a94f6bc6e2190b0ebd1e000 = Integer(0x13a94f6bc6e2190b0ebd1e000); _sage_const_0x5beae2bdf5fed7113ad93fa3 = Integer(0x5beae2bdf5fed7113ad93fa3); _sage_const_0xe5c79bc1120dd3414c191719 = Integer(0xe5c79bc1120dd3414c191719); _sage_const_0x150c5b51ec3db41ffd90c86d5 = Integer(0x150c5b51ec3db41ffd90c86d5); _sage_const_0 = Integer(0)#MOV attack
#https://www.hackthebox.com/blog/movs-like-jagger-ca-ctf-2022-crypto-writeup
#https://people.cs.nctu.edu.tw/~rjchen/ECC2009/19_MOVattack.pdf

a = -_sage_const_35 
b = _sage_const_98 
p = _sage_const_434252269029337012720086440207 

Gx = _sage_const_16378704336066569231287640165 
Gy = _sage_const_377857010369614774097663166640 

ec_order = _sage_const_434252269029337012720086440208 

E = EllipticCurve(GF(p), [a, b])
#print(E.order())

'''
The basic idea of this attack is that the discrete logarithm problem can be moved from an elliptic curve defined over Fp (finite field) to the multiplicative group of the finite field Fpk when p is divided by pk-1. If k is small enough (k < 6), the discrete log becomes easier to calculate than on the curve.
'''

#k = 1
#while (p**k - 1) % E.order():
#    k += 1
#print(k)

def movAttack(G, Q):
    k = _sage_const_1 
    while (p**k - _sage_const_1 ) % E.order():
        k += _sage_const_1 

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

Px = _sage_const_0x13a94f6bc6e2190b0ebd1e000 
Py = _sage_const_0x5beae2bdf5fed7113ad93fa3 

Qx = _sage_const_0xe5c79bc1120dd3414c191719 
Qy = _sage_const_0x150c5b51ec3db41ffd90c86d5 

G = E(Gx, Gy)
P = E(Px, Py)
Q = E(Qx, Qy)

nQ = movAttack(G, Q)
secret_point = nQ * P

print(hex(secret_point[_sage_const_0 ]))
print(hex(secret_point[_sage_const_1 ]))

#HTB{sh0w_m3_y0ur_sp@cip_MOVs_Klaus!}

