'''
Wireshark -> Statistics -> Protocol Hierarchy -> Data -> Apply as Filter -> Follow -> TCP Stream

ls -la
total 344
drwxr-xr-x 2 vigil vigil   4096 Jul  9 13:42 .
drwxr-xr-x 6 root  root    4096 Jul  9 13:38 ..
-rwxr-xr-x 1 vigil vigil 339920 Jul  9 13:24 costumers.sql
-rwxr-xr-x 1 vigil vigil    593 Jul  9 13:14 login.sh
pw
pwd
/var/www/html/MarketDump
ls -la
total 344
drwxr-xr-x 2 vigil vigil   4096 Jul  9 13:42 .
drwxr-xr-x 6 root  root    4096 Jul  9 13:38 ..
-rwxr-xr-x 1 vigil vigil 339920 Jul  9 13:24 costumers.sql
-rwxr-xr-x 1 vigil vigil    593 Jul  9 13:14 login.sh
whoami
root
wc -l costumers.sql
10302 costumers.sql
ls -la
total 344
drwxr-xr-x 2 vigil vigil   4096 Jul  9 13:55 .
drwxr-xr-x 6 root  root    4096 Jul  9 13:38 ..
-rwxr-xr-x 1 vigil vigil 333845 Jul  9 13:55 costumers.sql
-rw-r--r-- 1 root  root    1024 Jul  9 13:55 .costumers.sql.swp
-rwxr-xr-x 1 vigil vigil    593 Jul  9 13:14 login.sh
head -n2 costumers.sql
IssuingNetwork,CardNumber
cp costumers.sql /tmp/
cd /tmp
ls
config-err-lU04xV
costumers.sql
mozilla_vigil0
snap.1000_telegram-desktop_0UDXXk
ssh-8jVN4Kyx3X69
systemd-private-9ac4f21175984888b953531b43a88a47-apache2.service-lIsVqD
systemd-private-9ac4f21175984888b953531b43a88a47-bolt.service-Fd1LWs
systemd-private-9ac4f21175984888b953531b43a88a47-colord.service-rdNsnK
systemd-private-9ac4f21175984888b953531b43a88a47-fwupd.service-3d8iRg
systemd-private-9ac4f21175984888b953531b43a88a47-rtkit-daemon.service-pzu6lE
systemd-private-9ac4f21175984888b953531b43a88a47-systemd-resolved.service-ZtjIX4
systemd-private-9ac4f21175984888b953531b43a88a47-systemd-timesyncd.service-0BNKmh
Temp-bf8572b5-6aac-4c1d-aff6-063f56964ecb
python -m SimpleHTTPServer 9998
cat costumers.sql
IssuingNetwork,CardNumber
American Express,NVCijF7n6peM7a7yLYPZrPgHmWUHi97LCAzXxSEUraKme
IssuingNetwork,CardNumber

ls
config-err-lU04xV
costumers.sql
mozilla_vigil0
snap.1000_telegram-desktop_0UDXXk
ssh-8jVN4Kyx3X69
systemd-private-9ac4f21175984888b953531b43a88a47-apache2.service-lIsVqD
systemd-private-9ac4f21175984888b953531b43a88a47-bolt.service-Fd1LWs
systemd-private-9ac4f21175984888b953531b43a88a47-colord.service-rdNsnK
systemd-private-9ac4f21175984888b953531b43a88a47-fwupd.service-3d8iRg
systemd-private-9ac4f21175984888b953531b43a88a47-rtkit-daemon.service-pzu6lE
systemd-private-9ac4f21175984888b953531b43a88a47-systemd-resolved.service-ZtjIX4
systemd-private-9ac4f21175984888b953531b43a88a47-systemd-timesyncd.service-0BNKmh
Temp-bf8572b5-6aac-4c1d-aff6-063f56964ecb
rm -f costumers.sql
ls
config-err-lU04xV
mozilla_vigil0
snap.1000_telegram-desktop_0UDXXk
ssh-8jVN4Kyx3X69
systemd-private-9ac4f21175984888b953531b43a88a47-apache2.service-lIsVqD
systemd-private-9ac4f21175984888b953531b43a88a47-bolt.service-Fd1LWs
systemd-private-9ac4f21175984888b953531b43a88a47-colord.service-rdNsnK
systemd-private-9ac4f21175984888b953531b43a88a47-fwupd.service-3d8iRg
systemd-private-9ac4f21175984888b953531b43a88a47-rtkit-daemon.service-pzu6lE
systemd-private-9ac4f21175984888b953531b43a88a47-systemd-resolved.service-ZtjIX4
systemd-private-9ac4f21175984888b953531b43a88a47-systemd-timesyncd.service-0BNKmh
Temp-bf8572b5-6aac-4c1d-aff6-063f56964ecb
exit

So many "American Express, [0-9]+", but one special record hiden in them...

vim
:g/American Express,[0-9]\+/g

echo NVCijF7n6peM7a7yLYPZrPgHmWUHi97LCAzXxSEUraKme|base58 -d; echo
HTB{DonTRuNAsRoOt!MESsEdUpMarket}

'''
