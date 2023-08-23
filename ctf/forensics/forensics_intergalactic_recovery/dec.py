from pwn import *

'''
-rw-r--r--  1 szhan21 szhan21 5242880 4月   8  2022 06f98d35.img
-rw-r--r--  1 szhan21 szhan21    3790 4月   8  2022 0c584923.img
-rw-r--r--  1 szhan21 szhan21 5242880 4月   8  2022 fef0d1cd.img
'''
f1 = read('06f98d35.img') #disk1
f2 = read('0c584923.img') #disk2 corrupted
f3 = read('fef0d1cd.img') #disk3

f4 = xor(f1,f3)
write('disk2.img',f4)

'''
sudo apt-get install mdadm

sudo umount /dev/loop0
sudo losetup /dev/loop0 06f98d35.img
sudo umount /dev/loop1
sudo losetup /dev/loop1 disk2.img
sudo umount /dev/loop2
sudo losetup /dev/loop2 fef0d1cd.img

sudo mdadm --create --level=5 --raid-devices=3  /dev/md0 /dev/loop0 /dev/loop1 /dev/loop2
sudo umount /mnt/0
sudo mdadm --stop /dev/md0
sudo mdadm --create --level=5 --raid-devices=3  /dev/md1 /dev/loop2 /dev/loop1 /dev/loop0
file /mnt/0/imw_1337.pdf
/mnt/0/imw_1337.pdf: PDF document, version 1.7


HTB{f33ls_g00d_t0_b3_1nterg4l4ct1c_m0st_w4nt3d}
'''
