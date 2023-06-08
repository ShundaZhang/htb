#!/bin/bash

zipname=37366
for i in `seq 999`; do
        password=`strings $zipname.zip|grep zip -m 1|awk -F. '{print $1}'`
        echo $password
        unzip -P $password $zipname.zip
	zipname=$password
done

#~/ctf/john/run/zip2john 6969.zip > hash.txt
#~/ctf/john/run/john hash.txt --wordlist=/home/szhan21/ctf/john/run/rockyou.txt

#letmeinplease
#unzip 6969.zip with password letmeinplease
#got file DoNotTouch

#strings DoNotTouch |grep HTB

#HTB{z1p_and_unz1p_ma_bruddahs}
