//gcc -o sh_asm sh_asm.c -nostdlib -nostartfiles -Os -s -static

int main() {
    char *cmd = "/bin/sh";

    asm volatile (
        "mov $0x3b, %%rax\n"   // syscall number for execve
        "mov %0, %%rdi\n"      // command string
        "xor %%rsi, %%rsi\n"   // argv = NULL
        "xor %%rdx, %%rdx\n"   // envp = NULL
        "syscall\n"            // invoke the syscall
        :
        : "g"(cmd)
        : "rax", "rdi", "rsi", "rdx"
    );

    return 0;
}

