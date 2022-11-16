from Crypto.Util.number import isPrime


def generate_basis(n):
    basis = [True] * n

    for i in range(3, int(n**0.5) + 1, 2):
        if basis[i]:
            basis[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if basis[i]]


def millerRabin(n, b):
    basis = generate_basis(300)
    #print basis
    '''
    print '[',
    for i in range(300):
    	if isPrime(i):
		print str(i)+',',
    print ']'
    '''

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for b in basis:
        x = pow(b, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def _isPrime(p):
    if p < 1:
        return False
    if not millerRabin(p, 300):
        return False

    return True

'''
p = int(p)

if _isPrime(p) and not isPrime(p):
	print "HTB{fake_flag!}"
else:
	print "Fail!"
'''

#Google Carmichael Number
#https://en.wikipedia.org/wiki/Carmichael_number#Overview
'''
Arnault gives a 397-digit Carmichael number N that is a strong pseudoprime to all prime bases less than 307:
N=p*(313*(p-1)+1)*(353*(p-1)+1)
where
p=29674495668685510550154174642905332730771991799853043350995075531276838753171770199594238596428121188033664754218345562493168782883
'''

p = 29674495668685510550154174642905332730771991799853043350995075531276838753171770199594238596428121188033664754218345562493168782883
N = p*(313*(p-1)+1)*(353*(p-1)+1)

print N

#2887148238050771212671429597130393991977609459279722700926516024197432303799152733116328983144639225941977803110929349655578418949441740933805615113979999421542416933972905423711002751042080134966731755152859226962916775325475044445856101949404200039904432116776619949629539250452698719329070373564032273701278453899126120309244841494728976885406024976768122077071687938121709811322297802059565867
#HTB{c42m1ch431_15_f457_8u7_50m371m35_f457_15_n07_7h3_8357}
