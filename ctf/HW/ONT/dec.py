'''
file rootfs
rootfs: Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023

mount rootfs /mnt/image/ -t squashfs -o loop
cd /mnt/image/
grep HTB -r .

./etc/config_default.xml:<Value Name="SUSER_PASSWORD" Value="HTB{N0w_Y0u_C4n_L0g1n}"/>
''
