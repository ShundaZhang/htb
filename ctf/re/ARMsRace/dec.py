'''
ARM
'''

from pwn import *
from capstone import *
import binascii
import re

def extract_register_name(string):
    # Define the regular expression pattern to match the register name
    pattern = r"Register (r[0-9]+):"
    match = re.search(pattern, string)
    if match:
        return match.group(1)  # Return the matched register name
    else:
        return None  # Return None if no match is found

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
buf = io.recvuntil(": ").decode()
register_name = extract_register_name(buf)
print(register_name)
assembly, addr = hex_to_arm(hex_string)
print(assembly)


