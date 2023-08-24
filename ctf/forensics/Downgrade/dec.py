'''
https://medium.com/codex/hack-the-boo-downgrade-34590cb026d5

nc 157.245.37.125 31533

+-----------+---------------------------------------------------------+
|   Title   |                       Description                       |
+-----------+---------------------------------------------------------+
| Downgrade |         During recent auditing, we noticed that         |
|           |     network authentication is not forced upon remote    |
|           |       connections to our Windows 2012 server. That      |
|           |           led us to investigate our system for          |
|           |  suspicious logins further. Provided the server's event |
|           |       logs, can you find any suspicious successful      |
|           |                          login?                         |
+-----------+---------------------------------------------------------+

Which event log contains information about logon and logoff events? (for example: Setup)
> Security
[+] Correct!

What is the event id for logs for a successful logon to a local computer? (for example: 1337)
> 4624
[+] Correct!

Which is the default Active Directory authentication protocol? (for example: http)
> Kerberos
[+] Correct!

Looking at all the logon events, what is the AuthPackage that stands out as different from all the rest? (for example: http)
> ntlm
[+] Correct!

What is the timestamp of the suspicious login (yyyy-MM-ddTHH:mm:ss) UTC? (for example, 2021-10-10T08:23:12)
> 2022-09-28T13:10:57
[+] Correct!

[+] Here is the flag: HTB{34sy_t0_d0_4nd_34asy_t0_d3t3ct}
'''
