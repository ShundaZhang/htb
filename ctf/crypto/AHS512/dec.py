#!/usr/bin/python3

from hashlib import sha512
from random import randint

class ahs512():

    def __init__(self, message):
        self.message = message
        self.key = self.generateKey()

    def generateKey(self):
        while True:
            key = randint(2, len(self.message) - 1)
            if len(self.message) % key == 0:
                break

        return key

    def transpose(self, message):
        transposed = [0 for _ in message]

        columns = len(message) // self.key

        for i, char in enumerate(message):
            row = i // columns
            col = i % columns
            transposed[col * self.key + row] = char

        return bytes(transposed)

    def rotate(self, message):
        return [((b >> 4) | (b << 3)) & 0xff for b in message]

    def hexdigest(self):
        transposed = self.transpose(self.message)
        rotated = self.rotate(transposed)
        return sha512(bytes(rotated)).hexdigest()


original_message = b"pumpkin_spice_latte!"
#original_digest = ahs512(original_message).hexdigest()
transposed = ahs512(original_message).transpose(original_message)
print(bytes(transposed))
#rotated = ahs512(original_message).rotate(bytes(transposed))
#print(bytes(rotated))
'''
>>> print ord('!')
33
>>> print bin(ord('!'))
0b100001
>>> print chr(32)

>>> "pumpkin_spice_latte ".encode('hex')
'70756d706b696e5f73706963655f6c6174746520'
>>> print bin(ord('!'))
0b100001

Make new bit 7 | bit 0 == orginal bit 7 | bit 0

33 => 160

>>> print int(0b10100000)
160
>>> print hex(int(0b10100000))
0xa0
>>> 70756d706b696e5f73706963655f6c61747465a0

Enter your message: 70756d706b696e5f73706963655f6c61747465a0

HTB{5h4512_8u7_w17h_4_7w157_83f023_c4n_93n32473_c0111510n5}
'''

