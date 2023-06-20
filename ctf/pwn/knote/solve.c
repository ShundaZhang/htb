#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#include <sys/ioctl.h>
#include <sys/xattr.h>

#define KNOTE_CREATE 0x1337
#define KNOTE_DELETE 0x1338

typedef struct {
        unsigned long idx;
        char* data;
        size_t len;
} req_t;

int fd;

long create(unsigned long idx, char* data, size_t len) {
        req_t req = { .idx = idx, .data = data, .len = len };
        return ioctl(fd, KNOTE_CREATE, &req);
}

long delete(unsigned long idx) {
        req_t req = { .idx = idx };
        return ioctl(fd, KNOTE_DELETE, &req);
}

void open_device()
{
	if( (fd = open("/dev/knote", O_RDONLY))	< 0 )
	{
		printf( "Error open device!\n" );
		exit(-1);
	}
}

int main()
{
	open_device();
	printf( "Create knote structure...\n" );
	create(0, "asdf", 4);

	return 0;
}
