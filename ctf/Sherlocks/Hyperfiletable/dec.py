'''
https://www.cnblogs.com/IFS-/p/17917728.html

analyzeMFT.py：https://github.com/dkovar/analyzeMFT
MFTExplorer：https://ericzimmerman.github.io/#!index.md

Observe the results from the tools, not too hard...

The last question:

python3 analyzeMFT.py -f ~/ctf/htb/ctf/Sherlocks/Hyperfiletable/mft.raw -o mft.txt
grep "/Users/" mft.txt|grep Active | grep -v Folder|wc -l

3478
Very close to ***1
3471
'''
