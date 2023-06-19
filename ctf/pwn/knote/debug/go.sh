x86_64-linux-musl-gcc -o solve -static ../solve.c
mv solve rootfs
cd rootfs

find . -print0 | cpio --null -ov --format=newc 2>/dev/null | gzip -9 > ../rootfs.img

cd ..
sh qemu-cmd
