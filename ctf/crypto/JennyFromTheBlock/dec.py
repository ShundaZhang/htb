from hashlib import sha256

ct = 'd56591f1e1cbcb77c98473266bb8b3938db1ea6e8751604bced6ff262e954b8243e085580d650d757af55475e3a8e7030da53a5080a7c6a117e2537c4c8dcdfa9af11f91d12619caf796a4d12d0cbb085ca62b1dca39465a03ed967c10e944dd4f7bce176d1c81cefed8ec1316add4a1aead3a21199bdb4d84986f00bba5bfc6b899f065811c2b244d384ed93483ea3adc633fc267a072a3952657f1d8ec88a8335fe6a26589af63671bc00c4c8f2bb580d318cf8350dcc9257044ee4ffaffbe8391ac11c6bd224ea0a2cca4b4378b58e3c687ea7f80d1db46dfb4d842e1fd797c651646ea6651c53db8edd315a6204695bc35bc26e80b05284660b03068d9b0'.decode('hex')

block0 = 'Command executed: cat secret.txt'
#print len(block0) #32
#print len(ct)

def decrypt_block(eblock, block):
	pt = ''
	for i in range(32):
		pt += chr((ord(eblock[i]) - ord(block[i]) + 256) %256)
	return pt

px = ''
eblock0 = ct[:32]
h = sha256(eblock0+block0).digest()
for ic in range(1, len(ct)/32, 1):
	cx0 = ct[ic*len(block0):(ic+1)*len(block0)]
	px0 = decrypt_block(cx0, h)
	h = sha256(cx0+px0).digest()
	px += px0

print px

#HTB{th1s_b451c_b107k_c1ph3r_1s_n0t_s@fe}
