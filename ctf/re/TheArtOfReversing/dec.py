'''
.net code, dnSpy to de-complie

0123456789abc -> 21450c3b6798a

cathhtkeepaln-wymddd
'''

x = '21450c3b6798a'
p = 'cathhtkeepaln'
pk = [0]*13
px = list(x)
for i in range(len(px)):
	pk[int(px[i],16)] = p[i]

print ''.join(pk)

def ToR(number):
	if (number < 0 or number > 3999):
		return "";
	if (number < 1):
		return "";
	if (number >= 1000):
		return "M" + ToR(number - 1000);
	if (number >= 900):
		return "CM" + ToR(number - 900);
	if (number >= 500):
		return "D" + ToR(number - 500);
	if (number >= 400):
		return "CD" + ToR(number - 400);
	if (number >= 100):
		return "C" + ToR(number - 100);
	if (number >= 90):
		return "XC" + ToR(number - 90);
	if (number >= 50):
		return "L" + ToR(number - 50);
	if (number >= 40):
		return "XL" + ToR(number - 40);
	if (number >= 10):
		return "X" + ToR(number - 10);
	if (number >= 9):
		return "IX" + ToR(number - 9);
	if (number >= 5):
		return "V" + ToR(number - 5);
	if (number >= 4):
		return "IV" + ToR(number - 4);
	if (number >= 1):
		return "I" + ToR(number - 1);
	return "";

for i in range(16, 3651, 1):
	if ''.join(list(map(lambda x:chr(ord(x)+1), ToR(i)[::-1]))).lower() == 'wymddd':
		print i
		break

#HTB{hacktheplanet356}
