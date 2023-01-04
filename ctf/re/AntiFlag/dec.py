'''
https://www.youtube.com/watch?v=L-P5mfkyzeo

binary patching with ghidra + pwntools

1. Show the unreachable code block: Edit -> Tool Options -> Decompiler -> Analysis -> Uncheck Eliminate unreachable code
2. wget https://raw.githubusercontent.com/schlafwandler/ghidra_SavePatch/master/SavePatch.py and move to C:\...\ghidra_10.1.5_PUBLIC_20220726\ghidra_10.1.5_PUBLIC\Ghidra\Features\Python\ghidra_scripts
3. Patch Instruction (Ctrl+Shift+G)    
	00101510 74  13           JZ         LAB_00101525
	to
	00101510 75  13           JNZ        LAB_00101525
4. Select the modifed JNZ line and Display Script Manager, find SavePatch.py and run
5. Save to a patched binary and run it, get the flag

HTB{y0u_trac3_m3_g00d!!!}
'''
