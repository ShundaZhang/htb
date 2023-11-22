#The challenge updated and need to use LLL to pass the step 1.

import sys

arguments = sys.argv[1:]

#x = float(arguments[0])
#print(x)
x = -0.7039096773343625

M = Matrix(ZZ,3,4)
M[0] = [1, 0, 0, 10**17*x**2]
M[1] = [0, 1, 0, 10**17*x]
M[2] = [0, 0, 1, 10**17]
L = M.LLL()
print(L)

ai, bi, ci = int(L[0][0]), int(L[0][1]), int(L[0][2])

res = ai*x**2 + bi*x + ci
res *= 10**13 # did you think I would be that careless?

if int(res) != 0 or any(i == 0 or abs(i) > 60 for i in [ai, bi, ci]):
	print("Nope!")
	exit()

print("You passed the first test, now onto the second\n")

