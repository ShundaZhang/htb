#https://joshuanatan.medium.com/hack-bfc7c6528463

#grep support.php in pcap, found 4 streams
#modify support.php to print_support.php to print out the intermediate output
#php -S 0.0.0.0:8000

#Postman POST http://10.239.166.119:8000/print_support.php
#QKxO/n6DAwXuGEoc5X9/H3HkMXv1Ih75Fx1NdSPRNDPUmHTy -> uid=33(www-data) gid=33(www-data) groups=33(www-data)

#QKzo43k49AMoNoVOfAMh+6h3euEZJvkTlblqP34rlZqPhxDgKLYMz7NpqfQ9IR9FOXy0OfVbUgo/PF3MxrMw/JOdJebwjE2y6VAxUFnyA4H4dHQNgV49YatbqT0it9IXYf5kzoE4+kfGnZ/dTAsyCesTC0i5V+gJQw6bYm/nU3U/lrYGyl+dgvIOURfl0fvGm0hmr0RZKQ== -> 
'''
total 24K
drwxr-xr-x 2 developer developer 4.0K May 21 20:37 .
drwxr-xr-x 3 root root 4.0K May 20 21:28 ..
-rw-r--r-- 1 developer developer 220 May 20 21:28 .bash_logout
-rw-r--r-- 1 developer developer 3.5K May 20 21:28 .bashrc
-rw-r--r-- 1 developer developer 675 May 20 21:28 .profile
-rw-r--r-- 1 developer developer 1.6K May 21 20:37 pwdb.kdbx
'''

#QKy2/Pr9e+Z3eUh4//sZexUyZR8mN/g= -> /home/developer

#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 ->
#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

#store to pass.txt
#base64 -d pass.txt > pwdb.kdbx

#~/ctf/john/run/keepass2john pwdb.kdbx > pwdb.hash

'''
~/ctf/john/run/john pwdb.hash --wordlist=/home/szhan21/ctf/john/run/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 6000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES, 1=TwoFish, 2=ChaCha]) is 0 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
chainsaw         (pwdb)
1g 0:00:00:36 DONE (2023-04-05 18:00) 0.02727g/s 585.1p/s 585.1c/s 585.1C/s chivas13..biggie1
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
'''

#Use KeePass to open the pwdb.kdbx with password "chainsaw", then copy the password **** under Title Falg to Notepad.
#HTB{pr0tect_y0_shellZ}
