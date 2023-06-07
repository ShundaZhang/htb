'''
~/ctf/john/run/pdf2john.pl 0ld\ is\ g0ld.pdf > hash.txt

~/ctf/john/run/john hash.txt --wordlist=/home/szhan21/ctf/john/run/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
Cost 1 (revision) is 4 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
jumanji69        (0ld is g0ld.pdf)
1g 0:00:06:54 DONE (2023-06-07 15:36) 0.002410g/s 16442p/s 16442c/s 16442C/s jumart..jumane
Use the "--show --format=PDF" options to display all of the cracked passwords reliably
Session completed.

OR use pdfcrack

pdfcrack -f 0ld\ is\ g0ld.pdf -w /home/szhan21/ctf/john/run/rockyou.txt

PDF version 1.6
Security Handler: Standard
V: 2
R: 3
P: -1060
Length: 128
Encrypted Metadata: True
FileID: 5c8f37d2a45eb64e9dbbf71ca3e86861
U: 9cba5cfb1c536f1384bba7458aae3f8100000000000000000000000000000000
O: 702cc7ced92b595274b7918dcb6dc74bedef6ef851b4b4b5b8c88732ba4dac0c
Average Speed: 44234.6 w/s. Current Word: 'leo082270'
Average Speed: 44175.9 w/s. Current Word: 'goman1'
Average Speed: 44173.9 w/s. Current Word: 'y.a.s.m.e.e.n.90'
Average Speed: 44087.8 w/s. Current Word: 'stephz24'
Average Speed: 44076.2 w/s. Current Word: 'radha06'
Average Speed: 44079.7 w/s. Current Word: 'muñoz21'
Average Speed: 44071.8 w/s. Current Word: 'lindabebe05'
found user-password: 'jumanji69'

.-. .---- .--. ... .- -- ..- ...-- .-.. -- ----- .-. ... ...--

R1PSAMU3LM0RS3

'''
