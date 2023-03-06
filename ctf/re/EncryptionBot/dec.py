import os

#'9W8TLp4k7t0vJW7n3VvMCpWq9WzT3C8pZ9Wz'
enc = 'Lp4k7t0vJW7n3VvMCpWq9WzT3C8pZ9Wz'

fname = 'input.txt'
ans = []

for i in range(0,36,4):
	ans.append(enc[i:i+4])

flag = ['']*9
flag[0] = 'HTB{'
ff = 1
#print ans

for i in range(0x20, 0x7f, 1):
	for j in range(0x20, 0x7f, 1):
		for k in range(0x20, 0x7f, 1):
			s = chr(i)+chr(j)+chr(k)+'A'*24
			with open(fname,'wb') as f:
				f.write(s)
			s1 = os.popen('./chall < '+fname).read().split('\n')[-2][:4]
			if s1 in ans:
				ff += 1 
				x = ans.index(s1)
				flag[x] = s[:3]
				ans.pop(x)
				print ''.join(flag)
				if ff == 9:
					os.system('rm -f '+fname)
					exit(0)

