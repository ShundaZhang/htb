#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char a[32] = {0};

	read(0, a, 32);

	for( int i = 0; i < 32; i++ )
	{
		printf("0x%x\n", a[i]);
	}
}
