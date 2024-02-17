'''
ARM
'''

from pwn import *
from capstone import *
import binascii

def hex_to_arm(hex_string):
    # Convert hex string to bytes
    binary_data = binascii.unhexlify(hex_string)

    # Initialize Capstone disassembler
    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)

    # Disassemble the binary data
    disassembly = ""
    for i in md.disasm(binary_data, 0):
        #disassembly += "0x%x:\t%s\t%s\n" % (i.address, i.mnemonic, i.op_str)
        address = i.address
        disassembly += "%s\t%s\n" % (i.mnemonic, i.op_str)

    return disassembly, address


ip, port = "94.237.56.188", 44351
io = remote(ip, port)

io.recvuntil(": ")
hex_string = io.recvline().strip().decode()
print(hex_string)
buf = io.recvuntil(": ")
print(buf)
assembly, addr = hex_to_arm(hex_string)
print(assembly)


