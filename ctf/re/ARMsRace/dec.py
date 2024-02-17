'''
ARM
'''

from pwn import *
from capstone import *
import binascii
import re
import angr

def write_asm_to_file(asm_code, filename):
    with open(filename, "w") as file:
        file.write(asm_code)

def assemble_asm(input_filename, output_filename):
    import subprocess
    # Run arm-linux-gnueabi-as to assemble the assembly code
    subprocess.run(["arm-linux-gnueabi-as", "-o", output_filename, input_filename])

def extract_register_name(string):
    # Define the regular expression pattern to match the register name
    pattern = r"Register (r[0-9]+):"
    match = re.search(pattern, string)
    if match:
        return match.group(1)  # Return the matched register name
    else:
        return None  # Return None if no match is found

def extract_hexadecimal_value(string):
    # Define the regular expression pattern to match the hexadecimal value
    pattern = r"0x[0-9a-fA-F]+"
    match = re.search(pattern, string)
    if match:
        return match.group(0)  # Return the matched hexadecimal value
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

    disassembly += "movw    r1, #0x7ade"
    return disassembly, address

def get_result(output_filename, start_addr, reg):
    # Path to the ARM binary
    binary_path = output_filename

    # Load the binary into Angr
    proj = angr.Project(binary_path, auto_load_libs=False)

    # Create an entry state
    entry_state = proj.factory.entry_state()
    # Create a simulation manager with the entry state
    simgr = proj.factory.simulation_manager(entry_state)

    # Use Angr's symbolic execution engine to execute until the specified address
    simgr = proj.factory.simulation_manager(entry_state)
    # Explore the binary
    simgr.explore(find= 0x400000 + start_addr + 4)

    # Print the state of the program at address 0x1d8
    for state in simgr.found:
        return state.registers.load(reg)

ip, port = "94.237.56.188", 44351
io = remote(ip, port)

io.recvuntil(": ")
hex_string = io.recvline().strip().decode()
#print(hex_string)
buf = io.recvuntil(": ").decode()
register_name = extract_register_name(buf)
#print(register_name)
assembly, addr = hex_to_arm(hex_string)
#print(assembly)

# Write the assembly code to a file
asm_filename = "c1.asm"
write_asm_to_file(assembly, asm_filename)

# Assemble the assembly code using arm-linux-gnueabi-as
output_filename = "c1"
assemble_asm(asm_filename, output_filename)

result = get_result(output_filename, addr, register_name)
print(result)
#hex_ret = extract_hexadecimal_value(result)
#print(hex_ret)
