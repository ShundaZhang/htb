#apt-get install volatility
#refere to https://blog.khairulazam.net/2020/10/15/hackthebox-eu-reminiscent-forensics-40-points/
#flounder-pc-memdump.elf is too big, so didn't put in this repo

#volatility -f flounder-pc-memdump.elf imageinfo
#volatility -f flounder-pc-memdump.elf --profile=Win7SP1x64 pstree
#volatility -f flounder-pc-memdump.elf --profile=Win7SP1x64 filescan | grep -i resume
#volatility -f flounder-pc-memdump.elf --profile=Win7SP1x64 dumpfiles -n -i -r \\.lnk --dump-dir=output
#strings the files under folder output, and got base64 code, decode twice, then got the flag
#HTB{$_j0G_y0uR_M3m0rY_$}
