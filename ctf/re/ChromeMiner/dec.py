#https://ctftime.org/writeup/34612

'''
download .exe, dnSpy
Found several urls:

https://priyacareers.htb/c2VjcmV0/archive.zip?k=ZGlzY3VyZG5pdHJ1
https://perfectdemos.htb/c2VjcmV0/archive.zip?k=ZGlzY3VyZG5pdHJ1
https://bussiness-z.htb/c2VjcmV0/archive.zip?k=ZGlzY3VyZG5pdHJ1
https://cablingpoint.htb/c2VjcmV0/archive.zip?k=ZGlzY3VyZG5pdHJ1
https://corporatebusinessmachines.htb/c2VjcmV0/archive.zip?k=ZGlzY3VyZG5pdHJ1

Try, and should get the zip, including Chrome extension, unzip it by 7zip or online
Get backgroud.js, print out and found some info -- AES CBC encrypted flag
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_aes_cbc(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

key = b'_NOT_THE_SECRET_'
iv = b'_NOT_THE_SECRET_'
c = bytes.fromhex('E242E64261D21969F65BEDF954900A995209099FB6C3C682C0D9C4B275B1C212BC188E0882B6BE72C749211241187FA8')
print(decrypt_aes_cbc(key,iv,c))

#HTB{__mY_vRy_owN_CHR0me_M1N3R__}
