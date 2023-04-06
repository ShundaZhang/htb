python3 decode.py $1 | sed 's/*//g' | sed 's/Enter Password//g' | sed 's/ACCESS GRANDED SYSTEM DISARMED//g' | tr -d ' '
