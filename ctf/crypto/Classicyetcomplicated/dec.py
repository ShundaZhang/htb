#cipher identifier
#https://www.boxentriq.com/code-breaking/cipher-identifier
#https://www.boxentriq.com/code-breaking/vigenere-cipher
#Auto Solve (without key)
#The key is: helloworld

'''
Guess the algorithm is vigenere.
Guess alp is the (duplicated twice).
python
>>> chr((ord('a')-ord('t')+26)%26+ord('a'))
'h'
>>> chr((ord('l')-ord('h')+26)%26+ord('a'))
'e'
>>> chr((ord('p')-ord('e')+26)%26+ord('a'))
'l'
Guess the key is helloworld...
'''
