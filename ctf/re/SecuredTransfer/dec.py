data = '17275a3d9163b2798392813bf5e6826657bd11426076c910a38b68c2bcbbd3a5'.decode('hex')

with open('flag.enc', 'wb') as f:
	f.write(data)

iv = 'someinitialvalue'
print iv.encode('hex')

#cipher = EVP_aes_256_cbc()

k = [(0x38, ord('s')), (0x2f,0x65), (0x37,0x75), (0x36,0x70), (0x26,0x66), (0x25,0x6f), (0x24,0x72), (0x21,99), (0x2e,0x74), (0x2d,0x6b), (0x1d,0x74), (0x1b,0x6f), (0x32,0x65), (0x31,99), (0x33,0x73), (0x20,0x72), (0x2b,0x79), (0x2a,0x75), (0x29,0x73), (0x1c,0x69), (0x28,0x65), (0x27,100), (0x23,0x65), (0x1f,0x79), (0x30,0x72), (0x34,0x72), (0x1e,0x70), (0x19,0x21), (0x1a,0x6e), (0x2c,0x65), (0x35,0x65), (0x22,0x6e)]

k1 = sorted(k)

key = ''
for i in range(len(k1)):
	key += chr(k1[i][1])	

print key[::-1].encode('hex')

#openssl aes-256-cbc -d -in flag.enc -K 73757065727365637265746b657975736564666f72656e6372797074696f6e21 -iv 736f6d65696e697469616c76616c7565
#HTB{3ncRyPt3d_F1LE_tr4nSf3r}