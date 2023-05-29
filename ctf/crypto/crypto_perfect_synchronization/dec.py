#!/usr/bin/python3

import hashlib

with open('output.txt', 'r') as f:
	lines = f.readlines()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
i = 0
d = {}

result = []

for line in lines:
	line = line.strip()
	#print(line)
	#s = hashlib.md5(line.encode())
	s = line
	if i < len(alphabet):
		if not s in d:
			d[s] = alphabet[i]
			i = i + 1
		result.append(d[s])

print(''.join(str(x) for x in result))

'''
https://quipqiup.com/

ABCDECFGHIJFJKHLMLIMLINJLCOIPFIQRCIAJGQIQRJQIMFIJFHISMTCFI
frequency analysis is based on the fact that in any given

ABCDECFGH=frequency
I=SPACE
JFJKHLML=analysis
ML=is
NJLCO=based
PF=on
QRC=the
AJGQ=fact
QRJQ=that
MF=in
JFH=any
SMTCF=given
'''
