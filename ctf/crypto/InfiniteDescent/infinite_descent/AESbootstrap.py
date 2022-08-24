#!/usr/bin/env python
#**********************************************************************
# filename: AESbootstrap.py
# version: 0.11.7-alpha
# release date: 20170801
# dev: Cayce Pollard
# qa: Jonathan Norrell
# instantiate mersenne each time, feed it every 3 digits of the shared secret
# to establish a shared AES128 key.
#
#**********************************************************************

#textbook mersenne twister from https://en.wikipedia.org/wiki/Mersenne_Twister#Python_implementation (no rolling your own!)

class mersenne(object):

    def __init__(self, seed):
        # Initialize the index to 0
        self.index = 624
        self.mt = [0] * 624
        self.mt[0] = seed  # Initialize the initial state to the seed
        for i in range(1, 624):
            initval = int(0xFFFFFFFF & (1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i))
            # print(initval)
            self.mt[i] = initval


    def extract_number(self):
        if self.index >= 624:
            self.twist()

        y = self.mt[self.index]

        # Right shift by 11 bits
        y = y ^ y >> 11
        # Shift y left by 7 and take the bitwise and of 2636928640
        y = y ^ y << 7 & 2636928640
        # Shift y left by 15 and take the bitwise and of y and 4022730752
        y = y ^ y << 15 & 4022730752
        # Right shift by 18 bits
        y = y ^ y >> 18

        self.index = self.index + 1

        return int(0xFFFFFFFF & y)

    def twist(self):
        for i in range(624):
            # Get the most significant bit and add it to the less significant
            # bits of the next number
            y = int(0xFFFFFFFF & ((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)))
            self.mt[i] = self.mt[(i + 397) % 624] ^ y >> 1

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df
        self.index = 0
        #test


#******************************************************************************
#test tool:
#use this to convert a triplet from the decoded value as seedval
#do this across each of the values to check the candidate against the AESkey.
#******************************************************************************
def gen_and_check(genseed):
    # make an object
    x = mersenne(genseed)
    y = (x.extract_number() & 0xFF) #only interested in LSBs. Use the mask as we don't care about the rest

    return y #candidate for comparison.

list = str(bin(gen_and_check(seedval)))
candidate = list[2::]
candidate = candidate.zfill(8)
