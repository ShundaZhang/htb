; nasm -felf32 jmp.asm && ld -melf_i386 jmp.o -o jmp
section .text
global _start
_start:
sub esp, 0x16
jmp esp
