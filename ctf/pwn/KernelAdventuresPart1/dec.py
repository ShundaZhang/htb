import angr
import sys
# Load compiled hashing function
project = angr.Project("./hash")
state = project.factory.entry_state()
# Begin simulation
simmgr = project.factory.simulation_manager(state)
# Find "Found" in output
simmgr.explore(find=lambda state: b"Found" in state.posix.dumps(1))
# Return hex values if found.
if simmgr.found:
	for byte in simmgr.found[0].posix.dumps(0):
		print(hex(byte), end=',')
	print("")

#0x6e,0x63,0x7b,0x89,0x0,0x10,0x4,0x2

'''
# Compress exploit
gzip exploit
# Convert to base64 locally and copy the output from output.txt
cat exploit.gz | base64 > output.txt
# On remote convert base64 to gz file
cd /tmp && echo "base64" | base64 -d > exploit.gz
# Extract exploit
gzip -d expoit.gz
# Run the exploit
chmod +x exploit && ./exploit
'''
