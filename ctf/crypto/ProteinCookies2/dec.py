from Crypto.Cipher import AES

print(chr(80+16+len('&isLoggedIn=True')))
#'p'
#user_id=guest&isLoggedIn=False.55bed551f7dfd552a6ae1551b214175e3ae34bd4954bf2b747390e06982273fd
prefix = 'user_id=guest&isLoggedIn=False'
data = b'&isLoggedIn=True'+b'p'*16
print_data = '&isLoggedIn=True'

key = bytes.fromhex('55bed551f7dfd552a6ae1551b214175e3ae34bd4954bf2b747390e06982273fd')

cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(data)

enc = enc[::-1]
enc = enc[::2] + enc[1::2]
enc = enc[::3] + enc[2::3] + enc[1::3]

print(enc.hex())
print(prefix+chr(80)*16+print_data+'.'+enc.hex())

#set to the cookies and get the flag.pdf
#HTB{b3aT1nG_tH3_cUsT0m_h4sH_??!}
