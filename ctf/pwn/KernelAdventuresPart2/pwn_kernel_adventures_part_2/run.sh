#!/bin/sh

qemu-system-x86_64 \
		-kernel ./bzImage \
		-initrd ./dist.cpio.gz \
        -monitor /dev/null \
		-nographic -append "console=ttyS0"
