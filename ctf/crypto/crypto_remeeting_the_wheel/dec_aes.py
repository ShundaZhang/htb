from Crypto.Util.number import getPrime, long_to_bytes as l2b
from Crypto.Cipher import AES
from hashlib import sha256

enc_flag = bytes.fromhex('ce8f36aa844ab00319bcd4f86460a10d77492c060b2c2a91615f4cd1f2d0702e76b68f1ec0f11d15704ba52c5dacc60018d5ed87368464acd030ce6230efdbff7b18cba72ccaa9455a6fe6021b908dd1')

key1 = 1401735
key2 = 1997695
k = key1*key2

key = sha256(str(k).encode()).digest()

cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(enc_flag))

#b'HTB{b3tt3r_m33t_1n_r34l_l1f3_t0_t3ll_th3_s3cr3t_th4n_us3_unp4dd3d_R54!}\t\t\t\t\t\t\t\t\t'
