#https://7rocky.github.io/en/ctf/htb-challenges/pwn/knote/

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


'''
