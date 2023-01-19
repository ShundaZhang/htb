#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char buf[128] = {0};
	read(0, buf, 32);
	buf[10] = 0;
	open(buf, 0);
	read(3, buf, 32);
	puts(buf);
}
