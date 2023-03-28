for i in `seq 999`; do
	pwds0=$(python dec.py)
	pwds=$(echo $pwds0|tr '[:upper:]' '[:lower:]')
	echo $pwds
	unzip -P $pwds flag*.zip
	rm -f flag*.zip

	if [ -d flag ]; then
		mv flag/* . -f
    		rm -rf flag
	fi
done

'''
$ python dec.py
7920
$ unzip -P 7920 flag_0.zip

'''

#HTB{D0_y0u_L1k3_m0r53??}
