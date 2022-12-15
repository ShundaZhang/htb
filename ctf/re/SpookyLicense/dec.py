'''
      if ((((((((pcVar1[0x1d] == (char)((pcVar1[5] - pcVar1[3]) + 'F')) &&
               ((char)(pcVar1[2] + pcVar1[0x16]) == (char)(pcVar1[0xd] + '{'))) &&
              ((char)(pcVar1[0xc] + pcVar1[4]) == (char)(pcVar1[5] + '\x1c'))) &&
             ((((char)(pcVar1[0x19] * pcVar1[0x17]) == (char)(*pcVar1 + pcVar1[0x11] + '\x17') &&
               ((char)(pcVar1[0x1b] * pcVar1[1]) == (char)(pcVar1[5] + pcVar1[0x16] + -0x15))) &&
              (((char)(pcVar1[9] * pcVar1[0xd]) == (char)(pcVar1[0x1c] * pcVar1[3] + -9) &&
               ((pcVar1[9] == 'p' &&
                ((char)(pcVar1[0x13] + pcVar1[0x15]) == (char)(pcVar1[6] + -0x80))))))))) &&
            (pcVar1[0x10] == (char)((pcVar1[0xf] - pcVar1[0xb]) + '0'))) &&
           (((((((char)(pcVar1[7] * pcVar1[0x1b]) == (char)(pcVar1[1] * pcVar1[0xd] + '-') &&
                (pcVar1[0xd] == (char)(pcVar1[0x12] + pcVar1[0xd] + -0x65))) &&
               ((char)(pcVar1[0x14] - pcVar1[8]) == (char)(pcVar1[9] + '|'))) &&
              ((pcVar1[0x1f] == (char)((pcVar1[8] - pcVar1[0x1f]) + -0x79) &&
               ((char)(pcVar1[0x14] * pcVar1[0x1f]) == (char)(pcVar1[0x14] + '\x04'))))) &&
             ((char)(pcVar1[0x18] - pcVar1[0x11]) == (char)(pcVar1[0x15] + pcVar1[8] + -0x17))) &&
            ((((char)(pcVar1[7] + pcVar1[5]) == (char)(pcVar1[5] + pcVar1[0x1d] + ',') &&
              ((char)(pcVar1[0xc] * pcVar1[10]) == (char)((pcVar1[1] - pcVar1[0xb]) + -0x24))) &&
             ((((char)(pcVar1[0x1f] * *pcVar1) == (char)(pcVar1[0x1a] + -0x1b) &&
               ((((char)(pcVar1[1] + pcVar1[0x14]) == (char)(pcVar1[10] + -0x7d) &&
                 (pcVar1[0x12] == (char)(pcVar1[0x1b] + pcVar1[0xe] + '\x02'))) &&
                ((char)(pcVar1[0x1e] * pcVar1[0xb]) == (char)(pcVar1[0x15] + 'D'))))) &&
              ((((char)(pcVar1[5] * pcVar1[0x13]) == (char)(pcVar1[1] + -0x2c) &&
                ((char)(pcVar1[0xd] - pcVar1[0x1a]) == (char)(pcVar1[0x15] + -0x7f))) &&
               (pcVar1[0x17] == (char)((pcVar1[0x1d] - *pcVar1) + 'X'))))))))))) &&
          (((pcVar1[0x13] == (char)(pcVar1[8] * pcVar1[0xd] + -0x17) &&
            ((char)(pcVar1[6] + pcVar1[0x16]) == (char)(pcVar1[3] + 'S'))) &&
           ((pcVar1[0xc] == (char)(pcVar1[0x1a] + pcVar1[7] + -0x72) &&
            (((pcVar1[0x10] == (char)((pcVar1[0x12] - pcVar1[5]) + '3') &&
              ((char)(pcVar1[0x1e] - pcVar1[8]) == (char)(pcVar1[0x1d] + -0x4d))) &&
             ((char)(pcVar1[0x14] - pcVar1[0xb]) == (char)(pcVar1[3] + -0x4c))))))))) &&
         (((char)(pcVar1[0x10] - pcVar1[7]) == (char)(pcVar1[0x11] + 'f') &&
          ((char)(pcVar1[1] + pcVar1[0x15]) == (char)(pcVar1[0xb] + pcVar1[0x12] + '+')))))
'''

from z3 import *

pcVar1 = [ BitVec('pcVar1_%s' % i, 8) for i in range(32) ]

s = Solver()

for i in range(32):
	s.add(pcVar1[i] >= 0x20)
	s.add(pcVar1[i] < 0x7f)

s.add( pcVar1[0x1d] == (pcVar1[5] - pcVar1[3] + ord('F'))%256 )
s.add( (pcVar1[2] + pcVar1[0x16])%256 == (pcVar1[0xd] + ord('{'))%256 )
s.add( (pcVar1[0xc] + pcVar1[4])%256 == (pcVar1[5] + ord('\x1c'))%256 )
s.add( (pcVar1[0x19] * pcVar1[0x17])%256 == (pcVar1[0] + pcVar1[0x11] + ord('\x17'))%256 )
s.add( (pcVar1[0x1b] * pcVar1[1])%256 == (pcVar1[5] + pcVar1[0x16] + -0x15)%256 )
s.add( (pcVar1[9] * pcVar1[0xd])%256 == (pcVar1[0x1c] * pcVar1[3] + -9)%256 )
s.add( pcVar1[9] == ord('p') )
s.add( (pcVar1[0x13] + pcVar1[0x15])%256 == (pcVar1[6] + -0x80)%256 )
s.add( pcVar1[0x10] == (pcVar1[0xf] - pcVar1[0xb] + ord('0'))%256 )
s.add( (pcVar1[7] * pcVar1[0x1b])%256 == (pcVar1[1] * pcVar1[0xd] + ord('-'))%256 )
s.add( pcVar1[0xd] == (pcVar1[0x12] + pcVar1[0xd] + -0x65)%256 )
s.add( (pcVar1[0x14] - pcVar1[8])%256 == (pcVar1[9] + ord('|'))%256 )
s.add( pcVar1[0x1f] == (pcVar1[8] - pcVar1[0x1f] + -0x79)%256 )
s.add( (pcVar1[0x14] * pcVar1[0x1f])%256 == (pcVar1[0x14] + ord('\x04'))%256 )
s.add( (pcVar1[0x18] - pcVar1[0x11])%256 == (pcVar1[0x15] + pcVar1[8] + -0x17)%256 )
s.add( (pcVar1[7] + pcVar1[5])%256 == (pcVar1[5] + pcVar1[0x1d] + ord(','))%256 )
s.add( (pcVar1[0xc] * pcVar1[10])%256 == (pcVar1[1] - pcVar1[0xb] + -0x24)%256 )
s.add( (pcVar1[0x1f] * pcVar1[0])%256 == (pcVar1[0x1a] + -0x1b)%256 )
s.add( (pcVar1[1] + pcVar1[0x14])%256 == (pcVar1[10] + -0x7d)%256 )
s.add( pcVar1[0x12] == (pcVar1[0x1b] + pcVar1[0xe] + ord('\x02'))%256 )
s.add( (pcVar1[0x1e] * pcVar1[0xb])%256 == (pcVar1[0x15] + ord('D'))%256 )
s.add( (pcVar1[5] * pcVar1[0x13])%256 == (pcVar1[1] + -0x2c)%256 )
s.add( (pcVar1[0xd] - pcVar1[0x1a])%256 == (pcVar1[0x15] + -0x7f)%256 )
s.add( pcVar1[0x17] == (pcVar1[0x1d] - pcVar1[0] + ord('X'))%256 )
s.add( pcVar1[0x13] == (pcVar1[8] * pcVar1[0xd] + -0x17)%256 )
s.add( (pcVar1[6] + pcVar1[0x16])%256 == (pcVar1[3] + ord('S'))%256 )
s.add( pcVar1[0xc] == (pcVar1[0x1a] + pcVar1[7] + -0x72)%256 )
s.add( pcVar1[0x10] == (pcVar1[0x12] - pcVar1[5] + ord('3'))%256 )
s.add( (pcVar1[0x1e] - pcVar1[8])%256 == (pcVar1[0x1d] + -0x4d)%256 )
s.add( (pcVar1[0x14] - pcVar1[0xb])%256 == (pcVar1[3] + -0x4c)%256 )
s.add( (pcVar1[0x10] - pcVar1[7])%256 == (pcVar1[0x11] + ord('f'))%256 )
s.add( (pcVar1[1] + pcVar1[0x15])%256 == (pcVar1[0xb] + pcVar1[0x12] + ord('+'))%256)

print s.check()
print s.model()

#[pcVar1_12 = 48, pcVar1_11 = 48, pcVar1_10 = 48, pcVar1_29 = 51, pcVar1_23 = 67, pcVar1_4 = 84, pcVar1_5 = 104, pcVar1_7 = 95, pcVar1_26 = 67, pcVar1_30 = 89, pcVar1_6 = 101, pcVar1_14 = 48, pcVar1_25 = 110, pcVar1_13 = 48, pcVar1_17 = 107, pcVar1_1 = 84, pcVar1_27 = 51, pcVar1_28 = 75, pcVar1_16 = 48, pcVar1_15 = 48, pcVar1_19 = 121, pcVar1_3 = 123, pcVar1_24 = 51, pcVar1_2 = 66, pcVar1_0 = 72, pcVar1_8 = 115, pcVar1_21 = 108, pcVar1_22 = 105, pcVar1_31 = 125, pcVar1_20 = 95, pcVar1_18 = 101, pcVar1_9 = 112]

flag = [72, 84, 66, 123, 84, 104, 101, 95, 115, 112, 48, 48, 48, 48, 48, 48, 48, 107, 101, 121, 95, 108, 105, 67, 51, 110, 67, 51, 75, 51, 89, 125]
print ''.join(chr(i) for i in flag)
#HTB{The_sp0000000key_liC3nC3K3Y}
