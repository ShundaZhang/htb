'''
Partial dp dq
Factoring with Only a Third of the Secret CRT-Exponents
https://eprint.iacr.org/2022/271.pdf

Low dp dq
https://hackmd.io/pTtY4gtrQYuiex-cov2hJg

High dp dq
https://hackmd.io/@Giapppp/rJrKDLm8a?utm_source=preview-mode&utm_medium=rec
https://github.com/hackthebox/uni-ctf-2023/tree/main/uni-ctf-2023/crypto/%5BMedium%5D%20Mayday%20Mayday
https://7rocky.github.io/en/ctf/other/htb-unictf/mayday-mayday/

'''


# This file was *autogenerated* from the file dec.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_2048 = Integer(2048); _sage_const_512 = Integer(512); _sage_const_0x8415befe8ed2f11bc9980dca665d9f011ca1993cac84cbfa19b5b467ad66719eb5dca91f802d3cedd78395b3f94b7f937af8bd0789601b7b68f62e833d1304f2e49058e024a2fc60611017466dcc07c67121604f04d700a15a2e6d2bd146a433b004905c76e543bf1ad3cc26536592bb27081e77c39728535c8d44294dcf28d2199bc1f96ccebe018d12cc8660804f88555887208d4685465ffaa6433e8c0c6bbed3d8ce3f10e1b15962811246292dd9f52728f94a520449db79c9f1cf056d0600dbeb32f6206f9e80ad76570433f4c58fc46c33aa5f1dd7082fdbd2b92981f290d2fca9c135b2cd3d12e794da78f10f8548df11858e2c79af9218e97f09c1a1 = Integer(0x8415befe8ed2f11bc9980dca665d9f011ca1993cac84cbfa19b5b467ad66719eb5dca91f802d3cedd78395b3f94b7f937af8bd0789601b7b68f62e833d1304f2e49058e024a2fc60611017466dcc07c67121604f04d700a15a2e6d2bd146a433b004905c76e543bf1ad3cc26536592bb27081e77c39728535c8d44294dcf28d2199bc1f96ccebe018d12cc8660804f88555887208d4685465ffaa6433e8c0c6bbed3d8ce3f10e1b15962811246292dd9f52728f94a520449db79c9f1cf056d0600dbeb32f6206f9e80ad76570433f4c58fc46c33aa5f1dd7082fdbd2b92981f290d2fca9c135b2cd3d12e794da78f10f8548df11858e2c79af9218e97f09c1a1); _sage_const_0x447a951fc908492e818cad6d6f0ab1b0212b57f952575e391bec5ad43 = Integer(0x447a951fc908492e818cad6d6f0ab1b0212b57f952575e391bec5ad43); _sage_const_0xc8c6f6c4408d9d34b18948d976313329f4e09e722df217fe8dbd0684dbe52bccdcf4de9e6697d788601d753221886b1bc689e68e9745d1297a39cdd2de9bdcdf = Integer(0xc8c6f6c4408d9d34b18948d976313329f4e09e722df217fe8dbd0684dbe52bccdcf4de9e6697d788601d753221886b1bc689e68e9745d1297a39cdd2de9bdcdf); _sage_const_0x230ba63327b3480c4cf80369f10af726baacf61e631b07178d5aa62dc4b9017b30bf28c5ada9486817d71f0587dd23eea5162ff60880eb0cf7f866c695e1b369 = Integer(0x230ba63327b3480c4cf80369f10af726baacf61e631b07178d5aa62dc4b9017b30bf28c5ada9486817d71f0587dd23eea5162ff60880eb0cf7f866c695e1b369); _sage_const_0x23e6597702fba920abcbd5502b4102c0d88c9cac2186231444f4f23bf3e721031bb45cff4fa7dc325c9fc6d7fd51a216afa2161478e8e6610c350c9d5568506c8c94d0385cc77565b402db266e73e301473c0aa5149e920b66e3c81391b488812ef42a451d3003d1ba9d18befbdc38adfb5ca8f67a098ffb86e6aaa1230be7bc54fbade19f2f6d273f62ce07d92aa0356b979f108135c8fb33c77bd6b4eb07cce383f82ae3693feb1ebe3370974db1ae05919661558ce637c922caceb295a5c7717f5fdfd353d6b3b05113194fea4573b7a205ae0c2b034997d1bbbf1eee029499d7116b75413558d09a57b74315b45a9f17b2099dd647da1d63ccb5cb92cb2e = Integer(0x23e6597702fba920abcbd5502b4102c0d88c9cac2186231444f4f23bf3e721031bb45cff4fa7dc325c9fc6d7fd51a216afa2161478e8e6610c350c9d5568506c8c94d0385cc77565b402db266e73e301473c0aa5149e920b66e3c81391b488812ef42a451d3003d1ba9d18befbdc38adfb5ca8f67a098ffb86e6aaa1230be7bc54fbade19f2f6d273f62ce07d92aa0356b979f108135c8fb33c77bd6b4eb07cce383f82ae3693feb1ebe3370974db1ae05919661558ce637c922caceb295a5c7717f5fdfd353d6b3b05113194fea4573b7a205ae0c2b034997d1bbbf1eee029499d7116b75413558d09a57b74315b45a9f17b2099dd647da1d63ccb5cb92cb2e); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_0p5 = RealNumber('0.5')
def calculate_product_kl(dp_msb, dq_msb, N, e, i):
    return ceil(((_sage_const_2 **(_sage_const_2 *i) * e**_sage_const_2  * dp_msb * dq_msb) / N))

bits = _sage_const_2048 
known = _sage_const_512 
N = _sage_const_0x8415befe8ed2f11bc9980dca665d9f011ca1993cac84cbfa19b5b467ad66719eb5dca91f802d3cedd78395b3f94b7f937af8bd0789601b7b68f62e833d1304f2e49058e024a2fc60611017466dcc07c67121604f04d700a15a2e6d2bd146a433b004905c76e543bf1ad3cc26536592bb27081e77c39728535c8d44294dcf28d2199bc1f96ccebe018d12cc8660804f88555887208d4685465ffaa6433e8c0c6bbed3d8ce3f10e1b15962811246292dd9f52728f94a520449db79c9f1cf056d0600dbeb32f6206f9e80ad76570433f4c58fc46c33aa5f1dd7082fdbd2b92981f290d2fca9c135b2cd3d12e794da78f10f8548df11858e2c79af9218e97f09c1a1 
e = _sage_const_0x447a951fc908492e818cad6d6f0ab1b0212b57f952575e391bec5ad43 
dp_msb = _sage_const_0xc8c6f6c4408d9d34b18948d976313329f4e09e722df217fe8dbd0684dbe52bccdcf4de9e6697d788601d753221886b1bc689e68e9745d1297a39cdd2de9bdcdf 
dq_msb = _sage_const_0x230ba63327b3480c4cf80369f10af726baacf61e631b07178d5aa62dc4b9017b30bf28c5ada9486817d71f0587dd23eea5162ff60880eb0cf7f866c695e1b369 
i = bits//_sage_const_2  - known

c = _sage_const_0x23e6597702fba920abcbd5502b4102c0d88c9cac2186231444f4f23bf3e721031bb45cff4fa7dc325c9fc6d7fd51a216afa2161478e8e6610c350c9d5568506c8c94d0385cc77565b402db266e73e301473c0aa5149e920b66e3c81391b488812ef42a451d3003d1ba9d18befbdc38adfb5ca8f67a098ffb86e6aaa1230be7bc54fbade19f2f6d273f62ce07d92aa0356b979f108135c8fb33c77bd6b4eb07cce383f82ae3693feb1ebe3370974db1ae05919661558ce637c922caceb295a5c7717f5fdfd353d6b3b05113194fea4573b7a205ae0c2b034997d1bbbf1eee029499d7116b75413558d09a57b74315b45a9f17b2099dd647da1d63ccb5cb92cb2e 

A = calculate_product_kl(dp_msb, dq_msb, N, e, i)

def recover_k_and_l(A, N, e):
    k_plus_l = (_sage_const_1 -A*(N-_sage_const_1 )) % e

    k, l = var('k,l', domain=ZZ)
		
    # check both possibilities
    for s in [k_plus_l, k_plus_l + e]:
        try:
            sol = solve([k*l == A, k+l == s], k, l, solution_dict=True)[_sage_const_0 ]
            k, l = int(sol[k]), int(sol[l])
            break
        except:
            pass

    assert A == k*l

    return k, l

def factor(dp_msb, N, e, k, l, i):
    # we found k,l but probably in the wrong order
    # try both
    for kt, _ in [[k, l], [l, k]]:
        try:
            x = PolynomialRing(Zmod(kt*N), 'x').gens()[_sage_const_0 ]
            F = x + (e*dp_msb*_sage_const_2 **i + kt - _sage_const_1 ) * pow(e, -_sage_const_1 , kt*N)
            dp_lsb = int(F.small_roots(X=_sage_const_2 **i, beta=_sage_const_0p5 )[_sage_const_0 ])
            dp = (dp_msb << i) + dp_lsb
            
            p = (e*dp+kt-_sage_const_1 ) // kt
            q = N // p
            
            assert N == p * q
    
            return p, q
        except:
            pass

def decrypt(n, e, p, q, c):
    phi = (p-_sage_const_1 )*(q-_sage_const_1 )
    d = pow(e, -_sage_const_1 , phi)
    m = pow(c, d, n)
    return m

from Crypto.Util.number import long_to_bytes as l2b

def pwn():
    bits = _sage_const_2048 
    known = _sage_const_512 
    i = bits//_sage_const_2  - known
    A = calculate_product_kl(dp_msb, dq_msb, N, e, i)
    k, l = recover_k_and_l(A, N, e)
    p, q = factor(dp_msb, N, e, k, l, i)
    flag = decrypt(N, e, p, q, c)
    print(l2b(flag))
 
pwn()

