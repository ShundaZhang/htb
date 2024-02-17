'''
ARM
'''

from capstone import *
import binascii

def hex_to_arm(hex_string):
    # Convert hex string to bytes
    binary_data = binascii.unhexlify(hex_string)

    # Initialize Capstone disassembler
    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)

    for i in md.disasm(binary_data, 0):
        address = "0x%x:\t%s\t%s\n" % (i.address, i.mnemonic, i.op_str)
        print(address)

    # Disassemble the binary data
    disassembly = ""
    for i in md.disasm(binary_data, 0):
        #disassembly += "0x%x:\t%s\t%s\n" % (i.address, i.mnemonic, i.op_str)
        disassembly += "%s\t%s\n" % (i.mnemonic, i.op_str)

    return disassembly

def main():
    hex_string = "370301e3621d04e3a71248e37d2101e3bf2b43e3900100e0900200e0fd170fe33f134ae3c7210ee3ae2c4ce3000060e2bd1106e3171e41e3a52a08e35b264de3010080e00200a0e08f120fe3dd184ee3ee200ae325234ae3010000e0020000e06a1c09e3bf1f49e3da240be3902347e3010020e0020020e0e01c05e3f41749e3812606e36b294ce3010000e0020000e0fd1204e39b1b40e3f5270be3aa2548e3010040e00200c0e0de1a07e3dd1a41e3172600e31e2e41e3010080e1020080e17a1903e3ea174ae3e02e04e3502440e3010040e00200c0e0691b07e3311440e32c2c0ee3782445e3010040e00200c0e0ea1902e3641748e39d2d03e37d2648e3010000e0020000e0611d02e3621a46e3092c0fe3482a40e3900100e0900200e0ad1e05e3941742e33d260ce3d02e47e3010040e00200c0e0351c07e3ab134ce3d72902e3de2143e3010020e0020020e07d1f00e35c124fe3602e07e366244ee3010080e00200a0e0981f00e386124de3c42005e3722949e3010000e0020000e05e1306e3f41245e378270ae3422d4de3010040e00200c0e0841301e35e1c48e39e2604e3732e46e3000060e2551909e368114ae3a1290ce348274fe3010020e0020020e0ac1c00e376194fe355270be34f244be3900100e0900200e0"
    assembly = hex_to_arm(hex_string)
    print(assembly)

if __name__ == "__main__":
    main()

