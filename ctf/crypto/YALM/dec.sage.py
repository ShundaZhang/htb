

# This file was *autogenerated* from the file dec.sage
from sage.all_cmdline import *   # import sage library

_sage_const_21749248918759683544337447272671509713087570396847392696977994631698960045317596819865693333334493624370502448636831584145988028711233567234243060258534971464669149620614565032099403467041715388472573566028628032216786420721029298628718338901002634257184379911607586178908031583767930607042050327867387826322057745659825383472535093247656847914770054940932586227870658228788851350227826766531278231302804798812982333973499725242482126946725617567342220811180425286455535934049795118021253184879329685587581988120903375604417828886611483991738931048802648869100685999118954373198032024067740799452410209559772440413103 = Integer(21749248918759683544337447272671509713087570396847392696977994631698960045317596819865693333334493624370502448636831584145988028711233567234243060258534971464669149620614565032099403467041715388472573566028628032216786420721029298628718338901002634257184379911607586178908031583767930607042050327867387826322057745659825383472535093247656847914770054940932586227870658228788851350227826766531278231302804798812982333973499725242482126946725617567342220811180425286455535934049795118021253184879329685587581988120903375604417828886611483991738931048802648869100685999118954373198032024067740799452410209559772440413103); _sage_const_0x8ce7a727c4a70470aa3d6b872f82ef26c8ff5c7820d5790aa53e9dbd1d9f328c8847b268813c9c1bca54c3a892c9a848e95f37bb3c467971af3a29a2ea706dde662caa595728ff094b6c3c66bdddc6733f428c5b80ef81c0dbfa7f4419f08cc6ce7cde30df2004ff8037baf3647cf1813c577ca1303fb92f319418e3ed4f36dc49d33e7d92471a53ae2c029cdfa2b9034a6cb8f3b468f9154a6755aff13d923bd7e6d49d2e8db3b34b6135675d1a11236e7c8641716c54fe91dc26677200232baae8a9d5293109d73336f239d9a8905c7a1b81aec57d3df55f3302c0cddbcd742ea302c1157fa7b1138b36acd82cd73142b4fbf26099153616cd0d244dea2e1c = Integer(0x8ce7a727c4a70470aa3d6b872f82ef26c8ff5c7820d5790aa53e9dbd1d9f328c8847b268813c9c1bca54c3a892c9a848e95f37bb3c467971af3a29a2ea706dde662caa595728ff094b6c3c66bdddc6733f428c5b80ef81c0dbfa7f4419f08cc6ce7cde30df2004ff8037baf3647cf1813c577ca1303fb92f319418e3ed4f36dc49d33e7d92471a53ae2c029cdfa2b9034a6cb8f3b468f9154a6755aff13d923bd7e6d49d2e8db3b34b6135675d1a11236e7c8641716c54fe91dc26677200232baae8a9d5293109d73336f239d9a8905c7a1b81aec57d3df55f3302c0cddbcd742ea302c1157fa7b1138b36acd82cd73142b4fbf26099153616cd0d244dea2e1c); _sage_const_16 = Integer(16); _sage_const_10 = Integer(10); _sage_const_50 = Integer(50); _sage_const_8 = Integer(8); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2)
n = _sage_const_21749248918759683544337447272671509713087570396847392696977994631698960045317596819865693333334493624370502448636831584145988028711233567234243060258534971464669149620614565032099403467041715388472573566028628032216786420721029298628718338901002634257184379911607586178908031583767930607042050327867387826322057745659825383472535093247656847914770054940932586227870658228788851350227826766531278231302804798812982333973499725242482126946725617567342220811180425286455535934049795118021253184879329685587581988120903375604417828886611483991738931048802648869100685999118954373198032024067740799452410209559772440413103 

c = _sage_const_0x8ce7a727c4a70470aa3d6b872f82ef26c8ff5c7820d5790aa53e9dbd1d9f328c8847b268813c9c1bca54c3a892c9a848e95f37bb3c467971af3a29a2ea706dde662caa595728ff094b6c3c66bdddc6733f428c5b80ef81c0dbfa7f4419f08cc6ce7cde30df2004ff8037baf3647cf1813c577ca1303fb92f319418e3ed4f36dc49d33e7d92471a53ae2c029cdfa2b9034a6cb8f3b468f9154a6755aff13d923bd7e6d49d2e8db3b34b6135675d1a11236e7c8641716c54fe91dc26677200232baae8a9d5293109d73336f239d9a8905c7a1b81aec57d3df55f3302c0cddbcd742ea302c1157fa7b1138b36acd82cd73142b4fbf26099153616cd0d244dea2e1c 

message = 'Hey! This is my secret... it is secure because RSA is extremely strong and very hard to break... Here you go: HTB{'

hm0 = int(message.encode().hex(), _sage_const_16 )
R = PolynomialRing(Zmod(n), names=('x',)); (x,) = R._first_ngens(1)

for r in range(_sage_const_10 , _sage_const_50 ):
	hm = hm0<<(_sage_const_8 *r)
	m = hm + x
	#root = (m^3 - c).small_roots(X=2^(8*r),beta=0.1)
	root = (m**_sage_const_3  - c).small_roots()
	print(root)
	if root:
		M = m(root[_sage_const_0 ])
		print(bytes.fromhex(hex(int(M))[_sage_const_2 :]))

#HTB{c4n_LLL_br34k_RSA??!}

'''
Can also refer to:
#https://drive.google.com/file/d/1e8mXpAWQEYb73VynQ7Oq-k5eDuDLGnr5/view
#https://latticehacks.cr.yp.to/rsa.html
'''
