from Crypto.Util.number import *
from secret import pts,p,q

e = random_prime(2^10) # this will also be a secret , don't complain

N = p*q
pts = [bytes_to_long(i) for i in pts]
cts = [pow(i,e,N) for i in pts]
hint = sum(pts) # bcuz i don't want make chall unsolvable
print(f"{N},{cts},{hint}")