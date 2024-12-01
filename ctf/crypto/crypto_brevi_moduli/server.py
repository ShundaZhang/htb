from Crypto.Util.number import isPrime, getPrime, bytes_to_long
from Crypto.PublicKey import RSA

rounds = 5
e = 65537

for i in range(rounds):
    print('*'*10, f'Round {i+1}/{rounds}', '*'*10)

    pumpkin1 = getPrime(110)
    pumpkin2 = getPrime(110)
    n = pumpkin1 * pumpkin2
    large_pumpkin = RSA.construct((n, e)).exportKey()
    print(f'\n🎃Can you crack this pumpkin🎃?\n{large_pumpkin.decode()}\n')

    assert isPrime(_pmp1 := int(input('enter your first pumpkin = '))), exit()
    assert isPrime(_pmp2 := int(input('enter your second pumpkin = '))), exit()

    if n != _pmp1 * _pmp2:
        print('wrong! bye...')
        exit()

    print()

print(open('flag.txt').read())