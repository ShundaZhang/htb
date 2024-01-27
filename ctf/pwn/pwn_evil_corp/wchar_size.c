#include <wchar.h>
#include <stdio.h>

int main()
{
	wchar_t arr[4000];
	printf( "%ld\n", sizeof(wchar_t) );
	printf( "%ld\n", sizeof(arr) );
}
