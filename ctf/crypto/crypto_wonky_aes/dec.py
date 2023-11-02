'''
https://github.com/arusson/dfa-aes
https://github.com/arusson/dfa-aes/blob/main/src/dfa9.c

Modify daf-aes a little, bypass the decrypt check, just print out the possible keys, usually 1 key or 2 keys.

Connect to server, get enought ciphertext/faulttext pairs in log.txt
Find 8 pairs (in the order of 1st/2nd/3rd/4th byte changed) and into round9_8pairs.txt (keep the first line as plaintext/ciphertext as any value, we have bypassed it)

./bin/dfa -9 -i round9_8pairs.txt
Number of candidates for positions  0, 13, 10,  7: 1
                                    4,  1, 14, 11: 1
                                    8,  5,  2, 15: 1
                                   12,  9,  6,  3: 1
Number of Master Key candidates: 1
Progress: 1/1
17863ac678c4dcf2c6cd86cb1dad2a0d
The master key is 17863ac678c4dcf2c6cd86cb1dad2a0d

'''

from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

key = bytes.fromhex('17863ac678c4dcf2c6cd86cb1dad2a0d')
encrypted = bytes.fromhex('d5ce3817e81b2cf698c26828d0784d3ddbb5fef2989cbf27c68e7cfd527d2b4f')
cipher = AES.new(key, AES.MODE_ECB)
message = cipher.decrypt(encrypted)
print(message)


#HTB{d1d_y0u_kn0w_ab0ut_PQ_DF4?!}
