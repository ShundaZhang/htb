'''
szhan21@szhan21-NUC:~/ctf/htb/ctf/re/BehindtheScenes$ gdb ./behindthescenes
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 193 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
GEF for linux ready, type `gef' to start, `gef config' to configure
89 commands loaded for GDB 8.1.1 using Python engine 3.6
[*] 3 commands could not be loaded, run `gef missing` to know why.
Reading symbols from ./behindthescenes...(no debugging symbols found)...done.
gef➤  disassemble main
Dump of assembler code for function main:
   0x0000000000001261 <+0>:     endbr64
   0x0000000000001265 <+4>:     push   rbp
   0x0000000000001266 <+5>:     mov    rbp,rsp
   0x0000000000001269 <+8>:     sub    rsp,0xb0
   0x0000000000001270 <+15>:    mov    DWORD PTR [rbp-0xa4],edi
   0x0000000000001276 <+21>:    mov    QWORD PTR [rbp-0xb0],rsi
   0x000000000000127d <+28>:    mov    rax,QWORD PTR fs:0x28
   0x0000000000001286 <+37>:    mov    QWORD PTR [rbp-0x8],rax
   0x000000000000128a <+41>:    xor    eax,eax
   0x000000000000128c <+43>:    lea    rax,[rbp-0xa0]
   0x0000000000001293 <+50>:    mov    edx,0x98
   0x0000000000001298 <+55>:    mov    esi,0x0
   0x000000000000129d <+60>:    mov    rdi,rax
   0x00000000000012a0 <+63>:    call   0x1120 <memset@plt>
   0x00000000000012a5 <+68>:    lea    rax,[rbp-0xa0]
   0x00000000000012ac <+75>:    add    rax,0x8
   0x00000000000012b0 <+79>:    mov    rdi,rax
   0x00000000000012b3 <+82>:    call   0x1130 <sigemptyset@plt>
   0x00000000000012b8 <+87>:    lea    rax,[rip+0xffffffffffffff6a]        # 0x1229 <segill_sigaction>
   0x00000000000012bf <+94>:    mov    QWORD PTR [rbp-0xa0],rax
   0x00000000000012c6 <+101>:   mov    DWORD PTR [rbp-0x18],0x4
   0x00000000000012cd <+108>:   lea    rax,[rbp-0xa0]
   0x00000000000012d4 <+115>:   mov    edx,0x0
   0x00000000000012d9 <+120>:   mov    rsi,rax
   0x00000000000012dc <+123>:   mov    edi,0x4
   0x00000000000012e1 <+128>:   call   0x10e0 <sigaction@plt>
   0x00000000000012e6 <+133>:   ud2
   0x00000000000012e8 <+135>:   cmp    DWORD PTR [rbp-0xa4],0x2
   0x00000000000012ef <+142>:   je     0x130b <main+170>
   0x00000000000012f1 <+144>:   ud2
   0x00000000000012f3 <+146>:   lea    rdi,[rip+0xd0a]        # 0x2004
   0x00000000000012fa <+153>:   call   0x10d0 <puts@plt>
   0x00000000000012ff <+158>:   ud2
   0x0000000000001301 <+160>:   mov    eax,0x1
   0x0000000000001306 <+165>:   jmp    0x1439 <main+472>
   0x000000000000130b <+170>:   ud2
   0x000000000000130d <+172>:   mov    rax,QWORD PTR [rbp-0xb0]
   0x0000000000001314 <+179>:   add    rax,0x8
   0x0000000000001318 <+183>:   mov    rax,QWORD PTR [rax]
   0x000000000000131b <+186>:   mov    rdi,rax
   0x000000000000131e <+189>:   call   0x10f0 <strlen@plt>
   0x0000000000001323 <+194>:   cmp    rax,0xc
   0x0000000000001327 <+198>:   jne    0x1432 <main+465>
   0x000000000000132d <+204>:   ud2
   0x000000000000132f <+206>:   mov    rax,QWORD PTR [rbp-0xb0]
   0x0000000000001336 <+213>:   add    rax,0x8
   0x000000000000133a <+217>:   mov    rax,QWORD PTR [rax]
   0x000000000000133d <+220>:   mov    edx,0x3
   0x0000000000001342 <+225>:   lea    rsi,[rip+0xcd2]        # 0x201b
   0x0000000000001349 <+232>:   mov    rdi,rax
   0x000000000000134c <+235>:   call   0x10c0 <strncmp@plt>
   0x0000000000001351 <+240>:   test   eax,eax
   0x0000000000001353 <+242>:   jne    0x1429 <main+456>
   0x0000000000001359 <+248>:   ud2
   0x000000000000135b <+250>:   mov    rax,QWORD PTR [rbp-0xb0]
   0x0000000000001362 <+257>:   add    rax,0x8
   0x0000000000001366 <+261>:   mov    rax,QWORD PTR [rax]
   0x0000000000001369 <+264>:   add    rax,0x3
   0x000000000000136d <+268>:   mov    edx,0x3
   0x0000000000001372 <+273>:   lea    rsi,[rip+0xca6]        # 0x201f
   0x0000000000001379 <+280>:   mov    rdi,rax
   0x000000000000137c <+283>:   call   0x10c0 <strncmp@plt>
   0x0000000000001381 <+288>:   test   eax,eax
   0x0000000000001383 <+290>:   jne    0x1420 <main+447>
   0x0000000000001389 <+296>:   ud2
   0x000000000000138b <+298>:   mov    rax,QWORD PTR [rbp-0xb0]
   0x0000000000001392 <+305>:   add    rax,0x8
   0x0000000000001396 <+309>:   mov    rax,QWORD PTR [rax]
   0x0000000000001399 <+312>:   add    rax,0x6
   0x000000000000139d <+316>:   mov    edx,0x3
   0x00000000000013a2 <+321>:   lea    rsi,[rip+0xc7a]        # 0x2023
   0x00000000000013a9 <+328>:   mov    rdi,rax
   0x00000000000013ac <+331>:   call   0x10c0 <strncmp@plt>
   0x00000000000013b1 <+336>:   test   eax,eax
   0x00000000000013b3 <+338>:   jne    0x1417 <main+438>
   0x00000000000013b5 <+340>:   ud2
   0x00000000000013b7 <+342>:   mov    rax,QWORD PTR [rbp-0xb0]
   0x00000000000013be <+349>:   add    rax,0x8
   0x00000000000013c2 <+353>:   mov    rax,QWORD PTR [rax]
   0x00000000000013c5 <+356>:   add    rax,0x9
   0x00000000000013c9 <+360>:   mov    edx,0x3
   0x00000000000013ce <+365>:   lea    rsi,[rip+0xc52]        # 0x2027
   0x00000000000013d5 <+372>:   mov    rdi,rax
   0x00000000000013d8 <+375>:   call   0x10c0 <strncmp@plt>
   0x00000000000013dd <+380>:   test   eax,eax
   0x00000000000013df <+382>:   jne    0x140e <main+429>
   0x00000000000013e1 <+384>:   ud2
   0x00000000000013e3 <+386>:   mov    rax,QWORD PTR [rbp-0xb0]
   0x00000000000013ea <+393>:   add    rax,0x8
   0x00000000000013ee <+397>:   mov    rax,QWORD PTR [rax]
   0x00000000000013f1 <+400>:   mov    rsi,rax
   0x00000000000013f4 <+403>:   lea    rdi,[rip+0xc30]        # 0x202b
   0x00000000000013fb <+410>:   mov    eax,0x0
   0x0000000000001400 <+415>:   call   0x1110 <printf@plt>
   0x0000000000001405 <+420>:   ud2
   0x0000000000001407 <+422>:   mov    eax,0x0
   0x000000000000140c <+427>:   jmp    0x1439 <main+472>
   0x000000000000140e <+429>:   ud2
   0x0000000000001410 <+431>:   mov    eax,0x0
   0x0000000000001415 <+436>:   jmp    0x1439 <main+472>
   0x0000000000001417 <+438>:   ud2
   0x0000000000001419 <+440>:   mov    eax,0x0
   0x000000000000141e <+445>:   jmp    0x1439 <main+472>
   0x0000000000001420 <+447>:   ud2
   0x0000000000001422 <+449>:   mov    eax,0x0
   0x0000000000001427 <+454>:   jmp    0x1439 <main+472>
   0x0000000000001429 <+456>:   ud2
   0x000000000000142b <+458>:   mov    eax,0x0
   0x0000000000001430 <+463>:   jmp    0x1439 <main+472>
   0x0000000000001432 <+465>:   ud2
   0x0000000000001434 <+467>:   mov    eax,0x0
   0x0000000000001439 <+472>:   mov    rcx,QWORD PTR [rbp-0x8]
   0x000000000000143d <+476>:   xor    rcx,QWORD PTR fs:0x28
   0x0000000000001446 <+485>:   je     0x144d <main+492>
   0x0000000000001448 <+487>:   call   0x1100 <__stack_chk_fail@plt>
   0x000000000000144d <+492>:   leave
   0x000000000000144e <+493>:   ret
End of assembler dump.

From ghidra:

                             //
                             // .rodata
                             // SHT_PROGBITS  [0x2000 - 0x2035]
                             // ram:00102000-ram:00102035
                             //
                             _IO_stdin_used                                  XREF[3]:     Entry Point(*), 00100130(*),
                                                                                          _elfSectionHeaders::00000490(*)
        00102000 01 00 02 00     undefined4 00020001h
        00102004 2e 2f 63        ds         "./challenge <password>"
                 68 61 6c
                 6c 65 6e
        0010201b 49              ??         49h    I
        0010201c 74              ??         74h    t
        0010201d 7a              ??         7Ah    z
        0010201e 00              ??         00h
        0010201f 5f              ??         5Fh    _
        00102020 30              ??         30h    0
        00102021 6e              ??         6Eh    n
        00102022 00              ??         00h
        00102023 4c              ??         4Ch    L
        00102024 79              ??         79h    y
        00102025 5f              ??         5Fh    _
        00102026 00              ??         00h
        00102027 55              ??         55h    U
        00102028 44              ??         44h    D
        00102029 32              ??         32h    2
        0010202a 00              ??         00h
        0010202b 3e              ??         3Eh    >
        0010202c 20              ??         20h
        0010202d 48              ??         48h    H
        0010202e 54              ??         54h    T
        0010202f 42              ??         42h    B
        00102030 7b              ??         7Bh    {
        00102031 25              ??         25h    %
        00102032 73              ??         73h    s
        00102033 7d              ??         7Dh    }
        00102034 0a              ??         0Ah
        00102035 00              ??         00h

The password is Itz_0nLy_UD2

szhan21@szhan21-NUC:~/ctf/htb/ctf/re/BehindtheScenes$ ./behindthescenes Itz_0nLy_UD2
> HTB{Itz_0nLy_UD2}

'''
