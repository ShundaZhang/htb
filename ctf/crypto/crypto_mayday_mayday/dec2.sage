#https://hackmd.io/@Giapppp/rJrKDLm8a?utm_source=preview-mode&utm_medium=rec

from Crypto.Util.number import *

N = 0x8415befe8ed2f11bc9980dca665d9f011ca1993cac84cbfa19b5b467ad66719eb5dca91f802d3cedd78395b3f94b7f937af8bd0789601b7b68f62e833d1304f2e49058e024a2fc60611017466dcc07c67121604f04d700a15a2e6d2bd146a433b004905c76e543bf1ad3cc26536592bb27081e77c39728535c8d44294dcf28d2199bc1f96ccebe018d12cc8660804f88555887208d4685465ffaa6433e8c0c6bbed3d8ce3f10e1b15962811246292dd9f52728f94a520449db79c9f1cf056d0600dbeb32f6206f9e80ad76570433f4c58fc46c33aa5f1dd7082fdbd2b92981f290d2fca9c135b2cd3d12e794da78f10f8548df11858e2c79af9218e97f09c1a1
e = 0x447a951fc908492e818cad6d6f0ab1b0212b57f952575e391bec5ad43
c = 0x23e6597702fba920abcbd5502b4102c0d88c9cac2186231444f4f23bf3e721031bb45cff4fa7dc325c9fc6d7fd51a216afa2161478e8e6610c350c9d5568506c8c94d0385cc77565b402db266e73e301473c0aa5149e920b66e3c81391b488812ef42a451d3003d1ba9d18befbdc38adfb5ca8f67a098ffb86e6aaa1230be7bc54fbade19f2f6d273f62ce07d92aa0356b979f108135c8fb33c77bd6b4eb07cce383f82ae3693feb1ebe3370974db1ae05919661558ce637c922caceb295a5c7717f5fdfd353d6b3b05113194fea4573b7a205ae0c2b034997d1bbbf1eee029499d7116b75413558d09a57b74315b45a9f17b2099dd647da1d63ccb5cb92cb2e
dp = 0xc8c6f6c4408d9d34b18948d976313329f4e09e722df217fe8dbd0684dbe52bccdcf4de9e6697d788601d753221886b1bc689e68e9745d1297a39cdd2de9bdcdf
dq = 0x230ba63327b3480c4cf80369f10af726baacf61e631b07178d5aa62dc4b9017b30bf28c5ada9486817d71f0587dd23eea5162ff60880eb0cf7f866c695e1b369

A = (2**1024*e**2*dp*dq)//N + 1

x = PolynomialRing(Zmod(e), 'x').gen()
f = x^2 - (1 - A*(N - 1))*x + A
k, l = [int(c[0]) for c in f.roots()]

x = PolynomialRing(Zmod(k*N), 'x').gen()
a = ((e*dp*2^512 + k - 1) * pow(e, -1, k * N)) % (k * N)
g = x + a
dp_low = int(g.small_roots(X=2**512, beta=0.5)[0])

kp = int(g(dp_low))
p = gcd(kp, N)
q = N // p
assert p * q == N
d = pow(e, -1, (p - 1)*(q - 1))
m = pow(c, d, N)
from Crypto.Util.number import *
print(long_to_bytes(int(m)))
