# https://gist.github.com/nakov/60d62bdf4067ea72b7832ce9f71ae079
def mod_sqrt(a, p):
    def legendre_symbol(a, p):
        ls = pow(a, (p-1)//2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p+1)//4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while not s % 2:
        s >>= 1
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s+1)//2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r-m-1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

class EllipticCurve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def get_point(self, x):
        # equivalent to E.lift_x(x)
        return Point(self, x, -mod_sqrt(x**3 + self.a*x + self.b, self.p) % self.p)
    
class Point:
    def __init__(self, E, x, y):
        self.E = E
        self.x = x
        self.y = y
    
    def __add__(self, Q):
        P = self
        x1, y1 = P.x, P.y
        x2, y2 = Q.x, Q.y

        if (x1, y1) == (0, 0):
            return Q
        elif (x2, y2) == (0, 0):
            return P
        
        if x1 == x2 and y1 == -y2:
            return (0, 0)
        
        if (x1, y1) != (x2, y2):
            lam = (y2 - y1) * pow(x2 - x1, -1, self.E.p) % self.E.p
        else:
            lam = (3*x1**2 + self.E.a) * pow(2*y1, -1, self.E.p) % self.E.p
        
        x3 = lam**2 - x1 - x2
        y3 = lam*(x1 - x3) - y1
        return Point(self.E, x3 % self.E.p, y3 % self.E.p)

    def __mul__(self, n):
        P = self
        Q = P
        R = Point(self.E, 0, 0)
        while n:
            if n & 1:
                R += Q
            Q = Q + Q
            n >>= 1
        return R

    def __str__(self):
        return f'({self.x}, {self.y})'