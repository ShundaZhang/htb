'''
https://tellnotales.xyz/posts/ca2022_htb_writeup/#crypto--find-marhers-secret-68-solves

RC4 FMS attack:
https://en.wikipedia.org/wiki/Fluhrer,_Mantin_and_Shamir_attack

Code refer to:
https://github.com/jvdsn/crypto-attacks/blob/master/attacks/rc4/fms.py

'''

from collections import Counter
from pwn import *

def possible_key_bit(key, c):
	s = [i for i in range(256)]
	j = 0
	for i in range(len(key)):
		j = (j + s[i] + key[i]) % 256
		s[i], s[j] = s[j], s[i]

	return (c[0] - j - s[len(key)]) % 256


def attack(encrypt_oracle, key_len):
	"""
	Recovers the hidden part of an RC4 key using the Fluhrer-Mantin-Shamir attack.
	:param encrypt_oracle: the padding oracle, returns the encryption of a plaintext under a hidden key concatenated with the iv
	:param key_len: the length of the hidden part of the key
	:return: the hidden part of the key
	"""
	key = bytearray([3, 255, 0])
	for a in range(key_len):
		key[0] = a + 3
		possible = Counter()
		for x in range(256):
			key[2] = x
			c = encrypt_oracle(key[:3], b"\x00")
			possible[possible_key_bit(key, c)] += 1
		key.append(possible.most_common(1)[0][0])

	return key[3:]


