'''
Bypass safeurl check with server side redirect.
safeurl will check ports and hostname, normal ports other than 80/8080/443 will be blocked, all local host ip will be blocked.

There are two access to server, one is safeurl.execute, the second one is requests.get.
So in serverside, just return or redirect to google for the first access from safeurl, and then redirect to 127.0.0.1:1337/secret in the second access from python requests.

python app.py

input http://<vps_ip>/old in the search box

HTB{Expl01t1ng_ssrfs_f0r_fun}
'''
