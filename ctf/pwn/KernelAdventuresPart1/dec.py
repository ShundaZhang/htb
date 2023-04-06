#gunzip rootfs.cpio.gz
#cpio -idmv < rootfs.cpio

from pwn import *

ip, port = 
io = remote(ip, port)
