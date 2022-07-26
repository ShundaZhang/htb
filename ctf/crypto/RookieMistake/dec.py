#Cipolla
#https://rosettacode.org/wiki/Cipolla%27s_algorithm#Python

#Converts n to base b as a list of integers between 0 and b-1
#Most-significant digit on the left
def convertToBase(n, b):
	if(n < 2):
		return [n];
	temp = n;
	ans = [];
	while(temp != 0):
		ans = [temp % b]+ ans;
		temp /= b;
	return ans;
 
#Takes integer n and odd prime p
#Returns both square roots of n modulo p as a pair (a,b)
#Returns () if no root
def cipolla(n,p):
	n %= p
	if(n == 0 or n == 1):
		return (n,-n%p)
	phi = p - 1
	if(pow(n, phi/2, p) != 1):
		return ()
	if(p%4 == 3):
		ans = pow(n,(p+1)/4,p)
		return (ans,-ans%p)
	aa = 0
	for i in xrange(1,p):
		temp = pow((i*i-n)%p,phi/2,p)
		if(temp == phi):
			aa = i
			break;
	exponent = convertToBase((p+1)/2,2)
	def cipollaMult((a,b),(c,d),w,p):
		return ((a*c+b*d*w)%p,(a*d+b*c)%p)
	x1 = (aa,1)
	x2 = cipollaMult(x1,x1,aa*aa-n,p)
	for i in xrange(1,len(exponent)):
		if(exponent[i] == 0):
			x2 = cipollaMult(x2,x1,aa*aa-n,p)
			x1 = cipollaMult(x1,x1,aa*aa-n,p)
		else:
			x1 = cipollaMult(x1,x2,aa*aa-n,p)
			x2 = cipollaMult(x2,x2,aa*aa-n,p)
	return (x1[0],-x1[0]%p)

'''
print "Roots of 2 mod 7: " +str(cipolla(2,7))
print "Roots of 8218 mod 10007: " +str(cipolla(8218,10007))
print "Roots of 56 mod 101: " +str(cipolla(56,101))
print "Roots of 1 mod 11: " +str(cipolla(1,11))
print "Roots of 8219 mod 10007: " +str(cipolla(8219,10007))
'''
#RSA if n is prime, n = p*1, phi = p-1 = n-1
#but no result for e^-1 in p-1, because e and p-1 are all evens
#(p-1)/2 is producted by several primes
#e/2 and (p-1)/2 should be OK to get invert

#(f^2)^e/2 mod p = c1, e -> e/2, phi = p - 1 -> (p-1)/2
#f^2 mod p = m
#use cipolla to caculate f
import gmpy2

p = 0x16498bf7cc48a7465416e0f9ec8034f4030991e73aff9524ef74cc574228e36e6e1944c7686f69f0d1186a69b7aa77d7e954edc8a6932f006786f4648ecc8d4f4d3f6c03d9a1ee9fe61b28b6dd2791a63be581b8811a8ac90a387241ea68b7d36b4a274f64c7a721ad55cfcef23cd14c72542f576e4b507c11c4fa198e80021d484691b
e = 0x69420
c1 = 0xa82b37d57b6476fa98f6ee7c278d934bd96c49aa1c5399552d25211230d76cb16ade049572bf631e3849903638d41c884957b9592d0aa072b2bdc3105fe0e3253284f85286ec613966f9cde77ae06e2053dc2254e44ca673b4c76879eff84e5fc32af976c1bfafe147a277d72aad674db749ed8f34d2ebe8189cf12afc9baa17764e4b

d = gmpy2.invert(e/2, (p-1)/2)
m = pow(c1, d, p)
for mx in cipolla(m, p):
	print hex(mx)[2:]

print '4854427b7768795f6431645f7930755f6d3373735f33763372797468316e675f75705f3174735f6e30745f746834745f68347264a67bcb9c2c629c4e5149d2717d6683ecdf079959fdd2307c8aa040b5cee4fe509946c34a5eee981ac48fdeda63048a418f7a41908893436f550eb184f4659023a831cc8e3f'.decode('hex')[:-69]

#HTB{why_d1d_y0u_m3ss_3v3ryth1ng_up_1ts_n0t_th4t_h4rd

#sage dec.sage
print hex(2804476603085107565027707255749331066295103785426224861629602201861680712499854130377652576076102338557402972269310646835886484491716329948655731491481860234974607399319663254766286986177485599417063421968583069450861571804348897620247729058365086491428960261457881020586798485365714478651540371063176262146817288318452782818035727600844973213824528482080917545525357109160391608446961425726431705862033416482182497028540360742130961638707993186618482030415914893938295007102503532179843459346182484919123109958806129275887177866427746552590289190952679504543771881453032958846129549284558335743189694513183)[2:-1].decode('hex')[:-200]
#_ju5t_us3_pr0p3r_p4r4m3t3rs_f0r_4ny_crypt0syst3m...}

#HTB{why_d1d_y0u_m3ss_3v3ryth1ng_up_1ts_n0t_th4t_h4rd_ju5t_us3_pr0p3r_p4r4m3t3rs_f0r_4ny_crypt0syst3m...}
