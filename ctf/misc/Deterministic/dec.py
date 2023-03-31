from pwn import *

'''
for i in ['H','T','B','{','l','0','l','_','n','0','p','e','}']:
	print ord(i)

72
84
66
123
108
48
108
95
110
48
112
101
125
'''
#cat flag.txt |sort|uniq >sort.txt

with open('sort.txt', 'r') as f:
	buf = f.readlines()

s = []
v = []
t = []
for line in buf:
	f = line.strip().split(' ')
	s.append(f[0])
	v.append(f[1])
	t.append(f[2])

'''
for start in range(len(s)):
	i = start
	l = 0
	#print '*************************'
	#print s[i], v[i], t[i]
	for _ in range(len(s)):
		if t[i] in s:
			i = s.index(t[i])
			#print s[i], v[i], t[i]
			l += 1
		else:
			#print '==========================='
			print start, s[start], t[i], l
			break
'''

#60 69420 999 393

i = 60
flag = ''
while t[i] in s:
	flag += chr(int(v[i]))
	i = s.index(t[i])

for i in range(256):
	print xor(flag, i)

#python dec.py > log.txt
#HTB{4ut0M4t4_4r3_FuUuN_4nD_N0t_D1fF1cUlt!!}
