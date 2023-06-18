section .data
    hello db 'Hello, world!',0xA
    len equ $-hello

section .text
    global _start

_start:
    ; Prepare syscall arguments
    mov rax, 1          ; Syscall number for write
    mov rdi, 1          ; File descriptor (1 for stdout)
    mov rsi, hello      ; Buffer address
    mov rdx, len        ; Buffer length

    ; Make the syscall
    syscall

    ; Exit the program
    mov rax, 60         ; Syscall number for exit
    xor rdi, rdi        ; Exit code 0
    syscall

