import re
from PIL import Image

m = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....", "I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.", "S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--.."," ": "/", "1" : ".----","2" : "..---","3" : "...--","4" : "....-","5" : ".....","6" : "-....","7" : "--...","8" : "---..", "9" : "----.","0" : "-----",".": ".-.-.-",",": "--..--",":": "---...","?": "..--..","'": ".----.","-": "-....-", "/": "-..-.","@": ".--.-.","=": "-...-"}

rm = dict((v,k) for (k, v) in m.items())

#print m
#print rm

def decode_morse(message):
	msg = message.split(' ')
	decode_msg = ''
	for i in msg:
		if i in rm:
			decode_msg += rm[i]
		else:
			decode_msg += 'ERROR!!!'
	print decode_msg
	#return decode_msg

image = Image.open('pwd.png')
rgb = image.convert('RGB')
w, h = image.size
bs = ''

#c2 is the different color, when touch c2 add 0, when trun back to c1 add 1 as end
for y in range(0, h, 1):
	bs += '\n'
	for x in range(0, w, 1):
		p = rgb.getpixel((x,y))
		if x == 0:
			c1 = p
		elif x > 0 and p != c1:
			c2 = p
		
		if p == c1:
			bs += '1'
		elif p == c2:
			bs += '0'

bs = bs.replace('0001','-')
bs = bs.replace('01','.')
bs = re.sub('1+', ' ', bs)
bs = re.sub('\s+', ' ', bs)

bs = bs.strip()

decode_morse(bs)
