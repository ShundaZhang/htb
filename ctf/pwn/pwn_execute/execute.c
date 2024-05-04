// gcc execute.c -z execstack -o execute

#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void setup() {
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(0x7f);
}

int check(char *a, char *b, int size, int op) {
    for(int i = 0; i < op; i++) {
        for(int j = 0; j < size-1; j++) {
            if(a[i] == b[j])
                return 0;
        }
    }
    
    return 1337;
}

int main(){
    char buf[62];
    char blacklist[] = "\x3b\x54\x62\x69\x6e\x73\x68\xf6\xd2\xc0\x5f\xc9\x66\x6c\x61\x67";

    setup();

    puts("Hey, just because I am hungry doesn't mean I'll execute everything");
    
    int size = read(0, buf, 60);
	   
    if(!check(blacklist, buf, size, strlen(blacklist))) {
        puts("Hehe, told you... won't accept everything");
        exit(1337);
    }

    ( ( void (*) () ) buf) ();
}
