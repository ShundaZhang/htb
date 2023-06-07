from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import os
import random
from secret import FLAG

KEY = os.urandom(16)
IV = os.urandom(16)


class AESWCM:

    def __init__(self, key):
        self.key = key
        self.cipher = AES.new(self.key, AES.MODE_ECB)
        self.BLOCK_SIZE = 16

    def pad(self, pt):
        if len(pt) % self.BLOCK_SIZE != 0:
            pt = pad(pt, self.BLOCK_SIZE)
        return pt

    def blockify(self, message):
        return [
            message[i:i + self.BLOCK_SIZE]
            for i in range(0, len(message), self.BLOCK_SIZE)
        ]

    def xor(self, a, b):
        return bytes([aa ^ bb for aa, bb in zip(a, b)])

    def encrypt(self, pt, iv):
        blocks = self.blockify(pt)
        xor_block = iv

        ct = []
        for block in blocks:
            ct_block = self.cipher.encrypt(self.xor(block, xor_block))
            xor_block = self.xor(block, ct_block)
            ct.append(ct_block)

        return b"".join(ct).hex()

    def decrypt(self, ct, iv):
        ct = bytes.fromhex(ct)
        blocks = self.blockify(ct)
        xor_block = iv

        pt = []
        for block in blocks:
            pt_block = self.xor(self.cipher.decrypt(block), xor_block)
            xor_block = self.xor(block, pt_block)
            pt.append(pt_block)

        return b"".join(pt)

    def tag(self, pt, iv=os.urandom(16)):
        blocks = self.blockify(bytes.fromhex(self.encrypt(pt, iv)))
        random.shuffle(blocks)

        ct = blocks[0]
        for i in range(1, len(blocks)):
            ct = self.xor(blocks[i], ct)

        return ct.hex()


def main():
    aes = AESWCM(KEY)
    tags = []
    properties = []
    print("What properties should your magic wand have?")
    message = "Property: "

    counter = 0
    while counter < 3:
        property = bytes.fromhex(input(message))
        property = aes.pad(message.encode() + property)

        if property not in properties:
            properties.append(property)

            property_tag = aes.tag(property, IV)
            tags.append(property_tag)
            print(property_tag)

            if len(tags) > len(set(tags)):
                print(FLAG)

            counter += 1
        else:
            print("Only different properties are allowed!")
            exit(1)


if __name__ == "__main__":
    main()
