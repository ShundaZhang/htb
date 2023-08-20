'''
Run sage dec2.sage first
Then sage dec.sage
Avoid to use any \ in username, json.load/dump will make it shit...


Vitalium Storage Panel Menu:
[0] Get public key of server
[1] Make an account
[2] View coordinates of vitalium stashes
[3] Exit

Enter option > 1
Enter username > PNHMHLUOZLMQEORLOAJDYPNZTSQQJMQYLKJIDZCNLOKTOJKQPFRXR
{"username": "PNHMHLUOZLMQEORLOAJDYPNZTSQQJMQYLKJIDZCNLOKTOJKQPFRXR", "admin": false}
{"r": 17386203443291722512902524271990213200814914585844806909897368828418, "s": 135706694649578728588339859061092209227766165671748264258937295519, "message": "{\"username\": \"PNHMHLUOZLMQEORLOAJDYPNZTSQQJMQYLKJIDZCNLOKTOJKQPFRXR\", \"admin\": false}"}
Vitalium Storage Panel Menu:
[0] Get public key of server
[1] Make an account
[2] View coordinates of vitalium stashes
[3] Exit

Enter option > 2
r > 17386203443291722512902524271990213200814914585844806909897368828418
s > 135706694649578728588339859061092209227766165671748264258937295519
message > {"admin": true, "user": "UPGBRM[KHSYSOR^LNH[SGNNTLXTW[E]SZVOIKPJLOMTRHUOFK"}
r = 17386203443291722512902524271990213200814914585844806909897368828418, v = 17386203443291722512902524271990213200814914585844806909897368828418
Hello admin! Here are the coordinates to your vitalium stash: HTB{th3_l0c4t10n_0f_th3_v1t4l1um_1s_4t___37.187561,-115.885322}

'''


from Crypto.Util.number import *
import json

q = 26189572440233739420990528170531051459310363621928135990243626537967

# b'{"admin": True, "user": "xxxxxxx"}'

for k in range(100):
	
	c = bytes_to_long(b'{"admin": true, "user": "' + b"\x00" * k + b'"}')
	M = Matrix(ZZ, k+2, k+2)
	M[:k+1, :k+1] = Matrix.identity(k+1)
	for i in range(k):
		M[i, -1] = 256 ** (k+1 - i)
		M[-2, i] = -80
	M[-2, -2] = 1
	M[-2, -1] = c
	M[-1, -1] = -q
	M = M.LLL()

	for r in M:
		if r[-1] == 0 and r[-2] == 1:
			try:
				print("Found")
				print(k)
				user = "".join([chr(r[i] + 80) for i in range(k)])
				# check
				message = b'{"admin": true, "user": "' + user.encode() + b'"}'
				print(bytes_to_long(message) % q)
				print(message.decode())
			except:
				pass
