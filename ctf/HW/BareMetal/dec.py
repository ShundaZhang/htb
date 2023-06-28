'''
https://medium.com/@tobias.strg/hack-the-box-bare-metal-cf2771f32d0e

avr-objcopy -I ihex extracted_firmware.hex -O binary firmware_2.bin
'''

import binascii
with open("full_exchange.txt") as file:
    full_str = ''
    bitstream = ''
    for count, line in enumerate(file):
        mod = count % 3
        print(f"[{count}] / {mod}: {line}",end='')
        if(mod is 0):
            bit = '0' if line[0] is 'c' else '1'
            bitstream += bit

    print(f"\ntotal bits = {len(bitstream)}")
    n = int(bitstream, 2)
    x = binascii.unhexlify('%x' % n)
    print(x.decode())

#HTB{817_84n91n9_15_3v32ywh323!@#$%}
