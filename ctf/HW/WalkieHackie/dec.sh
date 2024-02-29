#URH (Universal Radio Hacker)
#Open *.complex, found Preamble is alwasy AAAAAAAA, Sync Word is always 73214693, and the middle 2 bytes of Payload are always ff.

#!/bin/bash

target="http://83.136.254.199:44948/transmit"

for ((i=0; i<=255; i++)); do
    x1=$(printf "%02x" $i)
    for ((j=0; j<=255; j++)); do
        x2=$(printf "%02x" $j)
        data="pa=AAAAAAAA&sw=73214693&pl=${x1}ff${x2}"
        curl -X POST -d "$data" -H "Content-Type: application/x-www-form-urlencoded" "$target" 
    done
done

#bash dec.sh > result.txt
#grep HTB result.txt
#HTB{B4s1c_r4d10_fund4s}

