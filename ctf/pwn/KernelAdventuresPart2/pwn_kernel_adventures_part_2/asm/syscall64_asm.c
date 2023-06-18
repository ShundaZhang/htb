//gcc -o syscall64_asm syscall64_asm.c -nostdlib -nostartfiles -Os -s -static
//#include <stdio.h>
//#include <stdlib.h>

int main() {
    char *message = "Hello, World!\n";
    unsigned long length = 14;
    unsigned long syscall_number = 1; // __NR_write
    unsigned long fd = 1; // stdout
    unsigned long ret;

    asm volatile (
        "syscall"
        : "=a" (ret)
        : "a" (syscall_number), "D" (fd), "S" (message), "d" (length)
        : "rcx", "r11", "memory"
    );

    //if (ret < 0) {
    //    perror("write");
    //    exit(1);
    //}

    return 0;
}

