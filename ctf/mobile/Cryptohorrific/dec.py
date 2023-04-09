#https://medium.com/write-ups-hackthebox/cryptohorrific-mobile-writeup-c78f79d6b1b1
#https://0xn1ghtr1ngs.github.io/posts/MobileChallenges-HTB/
from Crypto.Cipher import AES

#from IDA, we noticed the rcx and rsi parameters before calling SecretManager_key_iv_data

key = '!A%D*G-KaPdSgVkY'
iv = 'QfTjWnZq4t7w!z%C' #Apple CCCrypt is using AES 128 ECB?

#from Plist, we got cipher-text

#enc = 'XTq+CWzQS0wYzs2rJ+GNrPLP6qekDbwze6fIeRRwBK2WXHOhba7WR2OGNUFKoAvyW7njTCMlQzlwIRdJvaP2iYQ==' #Error
enc = 'Tq+CWzQS0wYzs2rJ+GNrPLP6qekDbwze6fIeRRwBK2WXHOhba7WR2OGNUFKoAvyW7njTCMlQzlwIRdJvaP2iYQ=='
cipher = AES.new(key, AES.MODE_ECB)
print cipher.decrypt(enc.decode('base64'))
#HTB{%SoC00l_H4ckTh3b0xbyBs3cur31stCh4ll3ng3!!Cr4zY%}
