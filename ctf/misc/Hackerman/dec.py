'''
stegoveritas hackerman.jpg

5634275d694f8665957746c9619132f0
it should be a hash
goto somd5.net and extract it

almost

steghide extract -sf hackerman.jpg
Enter passphrase: almost
wrote extracted data to "hackerman.txt".

cat hackerman.txt
SFRCezN2MWxfYzBycH0=

echo SFRCezN2MWxfYzBycH0=|base64 -d
HTB{3v1l_c0rp}
'''
