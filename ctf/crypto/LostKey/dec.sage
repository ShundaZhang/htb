#https://susanou.github.io/Writeups/posts/lostkey/
#https://zhuanlan.zhihu.com/p/368002164

'''
y^2 + ay = x^3 + bx^2 + cxy + dx + e
y^2 + a1xy + a3y = x^3 + a2x^2 + a4x + a6

l: lambda
l = (3x1^2 + 2a2x1 - a1y1 + a4) / (2y1 + a1x1 + a3)

R = 2P
xr = l^2 + la1 - a2 - 2x1yr = -a1xr - a3 - lxr + lx1 - y1

l = (3xpxq + ixp + j) / (yp + yq + k) mod p
xr = l^2 - xp - xq - m mod p
yr = l(xp - xr) - yp - n mod q

Lambda = (3*(P.x*Q.x) + 417826948860567519876089769167830531934*P.x + 177776968102066079765540960971192211603) * inverse(P.y+Q.y+3045783791, self.p)

R.x = (Lambda**2-P.x-Q.x-208913474430283759938044884583915265967) % self.p

R.y = (Lambda*(P.x-R.x) - P.y - 3045783791) % self.p

'''

i = 417826948860567519876089769167830531934
j = 177776968102066079765540960971192211603
k = 3045783791
m = 208913474430283759938044884583915265967
n = 3045783791

x = 14374457579818477622328740718059855487576640954098578940171165283141210916477
y = 97329024367170116249091206808639646539802948165666798870051500045258465236698
p = 101177610013690114367644862496650410682060315507552683976670417670408764432851

a1 = 0
a2 = i/2
a4 = j
a3 = k
a6 = y^2 + a3*y - x^3 - a2*x^2 - a4*x

E = EllipticCurve(GF(p), [a1, a2, a3, a4, a6])
P = E(x,y)
Q = E.lift_x(32293793010624418281951109498609822259728115103695057808533313831446479788050)
O = E.order()

fact = factor(O)
#print(fact)
fact = list(fact)
#print(fact)
factors = []
for f in fact:
    factors.append(f[0]**f[1])
#print(factors)

factors = factors[:-2]
dl = []
for f in factors:
    Pi = P * (int(O)//f)
    Qi = Q * (int(O)//f)
    
    d_log = discrete_log(Qi, Pi, operation="+")
    print("factor:  ", f, " ECDLP sol: ", d_log)
    dl.append(d_log)
print(dl)

l = crt(dl, factors)
print(l)

def list_product(f, n=1):
    for x in f:
        n = n*x
    return n
mod = list_product(factors)
print(mod)

#n = mod*i + l

for i in range(int(38685626227668133590597631)//mod):
    if (P*(l+mod*i))[0] == Q[0]:
        print(i)
        break

n = (l+mod*i)%p
print(n)
