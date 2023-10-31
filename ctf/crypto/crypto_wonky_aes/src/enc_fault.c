#include "aes.h"
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

typedef uint8_t state_t[4][4];
int urand_fd;

void GetRand(uint8_t *buf, int len) {
	read(urand_fd, buf, len);
}

bool ShouldEnc() {
	char inp[3];
	inp[0] = '\0';
	while (inp[0] != 'y' &&
		   inp[0] != 'Y' &&
		   inp[0] != 'n' &&
		   inp[0] != 'N') {
		printf("Encrypt once? (y/n): ");
		if (scanf("%1s", inp) != 1) {
			return false;
		}
		getchar();
	}
	return inp[0] == 'Y' || inp[0] == 'y';
}

int main() {
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stderr, 0, 2, 0);
    
	urand_fd = open("/dev/urandom", O_RDONLY);
	if (urand_fd < 0) {
		puts("Error: Contact admin");
		return -1;
	}

	uint8_t Round[AES_keyExpSize];
	uint8_t plain[AES_KEYLEN], buf[AES_KEYLEN], Key[AES_KEYLEN];
	
	GetRand(Key, AES_KEYLEN);

	KeyExpansion(Round, Key);

	bool end = false;
	uint8_t fault;
	uint8_t fault_pos;

	while (!end) {
		end = !ShouldEnc();
		if (!end) {
			GetRand(plain, AES_KEYLEN);
			memcpy(buf, plain, sizeof(plain));
			Cipher((state_t*)buf, Round);
			
			puts("");
			printf("Correct encryption: ");
			for (int i = 0; i < AES_KEYLEN; i++) {
				printf("%02x", buf[i]);
			}
			puts("");
			puts("Bzz...A wild fault has appeared!");
			printf("Faulty encryption:  ");
			memcpy(buf, plain, sizeof(plain));

			GetRand(&fault, 1);
			GetRand(&fault_pos, 1);
			fault_pos %= sizeof(state_t);

			CipherFault((state_t*)buf, Round, true, fault_pos, fault);
			for (int i = 0; i < AES_KEYLEN; i++) {
				printf("%02x", buf[i]);
			}
			puts("\n");
			// printf("%d\n", fault_pos);
		}
	}

	int flag_fd = open("flag.txt", O_RDONLY);
	if (flag_fd < 0) {
		puts("Error: Contact admin");
		return -1;
	}
	uint8_t flag[AES_KEYLEN * 2];
	memset(flag, 0, AES_KEYLEN * 2);
	read(flag_fd, flag, AES_KEYLEN * 2);

	printf("\nFlag encrypted: ");
	for (int part = 0; part < 2; part++) {
		memcpy(buf, &flag[part * AES_KEYLEN], AES_KEYLEN);
		Cipher((state_t*)buf, Round);
		for (int i = 0; i < AES_KEYLEN; i++) {
			printf("%02x", buf[i]);
		}
	}
	puts("");
}