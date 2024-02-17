.global _start

.section .text

_start:
    MOV R0, #10       @ Load 10 into register R0
    MOV R1, #15       @ Load 15 into register R1
    ADD R2, R0, R1    @ Add the contents of R0 and R1, store result in R2
    
    MOV R7, #1        @ Syscall number for exit
    MOV R0, #0        @ Return value for exit syscall
    SWI 0             @ Invoke syscall

