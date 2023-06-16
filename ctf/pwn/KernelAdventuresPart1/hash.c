#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef unsigned int uint;

uint hash(char *param_1)
{
  uint uVar1;
  size_t sVar2;
  uint local_14;
  size_t local_10;
  
  local_10 = 0;
  local_14 = 0;
  sVar2 = strlen(param_1);
  for (; local_10 != sVar2; local_10 = local_10 + 1) {
    uVar1 = (local_14 + (int)param_1[local_10]) * 0x401;
    local_14 = uVar1 ^ uVar1 >> 6 ^ (int)param_1[local_10];
  }
  return local_14;
}

int main()
{
	char buf[8];
	uint ret = 0;

	memset(buf, 0, 8);
	read(0, buf, 8);

	ret = hash(buf);
	if (ret == 0x03319f75)
		printf("Found");
	else
		printf("NO");
}
