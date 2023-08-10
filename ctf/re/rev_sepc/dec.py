from pwn import *

#ghidra -> .text -> found ioctl code
s1 = 'fcb0abd06e442ba0c77d8b5239a7ad606e6b976aa1107c1bc9c753c951d070e50a26'.decode('hex')
      
s2 = 'b4e4e9ab09364ac2a514e53566c399145a34f118917d2370fab53dfa3de500d16915f0a68348c6302e4529020aa90f38890dac1c897cf4d3f06b2f21b7d8c0fb'.decode('hex')

print(xor(s1,s2[:len(s1)]))

