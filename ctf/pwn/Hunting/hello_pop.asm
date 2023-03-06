;nasm -f elf32 hello.asm && ld -m elf_i386 hello.o -o hello

section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point

    push    len                                 ;message length
    pop     edx
    push    msg                                 ;message to write
    pop     ecx
    push    1                                   ;file descriptor (stdout)
    pop     ebx
    push    4                                   ;system call number (sys_write)
    pop     eax
    int     0x80                                ;call kernel
    push    1                                   ;system call number (sys_exit)
    pop     eax
    int     0x80                                ;call kernel

section     .data

msg     db  'Hello, world!',0xa                 ;our dear string
len     equ $ - msg                             ;length of our dear string
