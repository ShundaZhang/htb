from collections import namedtuple
from functools import reduce
from operator import mul
from Crypto.Util.number import inverse
import random
Point = namedtuple("Point","x y")
def moddiv(x,y,p):
    return (x * inverse(y,p)) % p
def crt(*args):
    # Takes a bunch of lists in form [value,modulus]
    values = [row[0] for row in args]
    ns = [row[1] for row in args]
    N = reduce(mul,ns)
    _sum = 0
    for i in range(len(args)):
        yi = N // ns[i]
        zi = inverse(yi,ns[i])
        _sum += values[i]*yi*zi
    return _sum % N
def composite_square_root(num,p,q):
    # Only works if num is a quadratic residue mod p and q AND p and q are 3 mod 4
    n = p * q
    root1 = pow(num,(p+1)//4,p)
    root2 = pow(num,(q+1)//4,q)
    ans = crt([root1,p],[root2,q])
    assert pow(ans,2,n) == (num % n)
    return ans
class EllipticCurve:
    INF = Point(0,0)
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
    def add(self,P,Q):
        if P == self.INF:
            return Q
        elif Q == self.INF:
            return P

        if P.x == Q.x and P.y == (-Q.y % self.p):
            return self.INF
        if P != Q:
            Lambda = moddiv(Q.y - P.y, Q.x - P.x, self.p)
        else:
            Lambda = moddiv(3 * P.x**2 + self.a,2 * P.y , self.p)
        Rx = (Lambda**2 - P.x - Q.x) % self.p
        Ry = (Lambda * (P.x - Rx) - P.y) % self.p
        return Point(Rx,Ry)
    def multiply(self,P,n):
        n %= self.p
        if n != abs(n):
            ans = self.multiply(P,abs(n))
            return Point(ans.x, -ans.y % p)
        R = self.INF
        while n > 0:
            if n % 2 == 1:
                R = self.add(R,P)
            P = self.add(P,P)
            n = n // 2
        return R
    def lift_x(self,x,p,q):
        expr = x**3 + self.a*x + self.b
        y = composite_square_root(expr,p,q)
        return Point(x,y)