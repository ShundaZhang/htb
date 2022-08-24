#!/usr/bin/env python
#**********************************************************************
# filename: fasterprimes.py
# version: 0.06.2-alpha
# release date: 20170806
# dev: Cayce Pollard
# qa: NOT PASSED, open defects.
# finds a specified length prime, then a neighbouring prime for speed. 
# DEFECTS
# ID[243], category A4, owner: CayceP, comment: may have to be run several times to generate valid RSA values
# ID[552], category A9, owner: AppSec, comment: Do neighbouring primes present a security risk?
#**********************************************************************


from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
import sympy


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def getPQ():
    n_length =512 #generates a 1024 bit key.
    while True:
        firstprime = number.getPrime(n_length) #let's get our first number
	lowerp = firstprime - 10
	upperp = firstprime + 10       
	for x in range(lowerp,upperp): #getPrime takes too long so we'll find a nearby prime for q
           if x == firstprime:
             continue
           else:   
             if sympy.isprime(x):
                secondprime = x
                return firstprime, secondprime
                break
        return 1, 1
     
e = 65537

while True:
    p, q = getPQ()  
    if p == 1:
        print("still trying")
    else:
      break


n = p*q #we make our modulus
phi = (p-1)*(q-1) #this one is for making the private key
gcd, d, b = egcd(e, phi) #now we have all our RSA values. 

key_params = (long(n), long(e), long(d))
key = RSA.construct(key_params)
print key.exportKey()
print key.publickey().exportKey()
#keep the pre-shared key below 100 bytes. 
message = #put the message here.
#message = [ord(c) for c in message] #comment out if message is int.
#message = int(''.join(map(str,message)))
print ('message: ', message)
RSAsecret = key.encrypt(int(message),'') #check the encryption works 
print ('RSAsecret: ', RSAsecret) #send this to the recipient
print ('message: ', message) #don't send this you idiot.
print ('Secret check:', key.decrypt(RSAsecret)) #check the message matches the decrypted message/

