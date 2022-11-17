'''
Options:

1.Encrypt flag
2.Encrypt plaintext
3.Change mode
4.Exit

> {"option":"3"}
These are the supported modes
{"modes": ["ECB", "CBC", "CFB", "OFB", "CTR"]}
Expecting modes:
{"modes":["CTR"]}
Please interact with the server using json data!
Selected mode is CTR.

Options:

1.Encrypt flag
2.Encrypt plaintext
3.Change mode
4.Exit

> {"option":"1"}

{"response": "encrypted", "ciphertext": "22ade9dbf7f96a62990faa5083df4cf4aff5527d47d25a20259b892abebe3f5689a67b4a4c9d19fa856c903646ff45312bda829f249042300cad63ec3ee3e3e4"}
Please interact with the server using json data!
Selected mode is CTR.

Options:

1.Encrypt flag
2.Encrypt plaintext
3.Change mode
4.Exit

> {"option":"2"}
Enter plaintext:
{"plaintext":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"}

{"response": "encrypted", "ciphertext": "2bb8eae18388744eec20924eafae6986dbeb750c34cc711451ed975fa0941027bf89657b3ce869d5f31ea940588a33470fa9f9d004ee0d6159ee5ebf7aa18ef5"}
Please interact with the server using json data!
Selected mode is CTR.

Options:

1.Encrypt flag
2.Encrypt plaintext
3.Change mode
4.Exit

>
'''
from pwn import *

c1 = '2bb8eae18388744eec20924eafae6986dbeb750c34cc711451ed975fa0941027bf89657b3ce869d5f31ea940588a33470fa9f9d004ee0d6159ee5ebf7aa18ef5'.decode('hex')

p1 = 'A'*48+'\x10'*16
c2 = '22ade9dbf7f96a62990faa5083df4cf4aff5527d47d25a20259b892abebe3f5689a67b4a4c9d19fa856c903646ff45312bda829f249042300cad63ec3ee3e3e4'.decode('hex')
flag = xor(xor(c1,p1),c2)

print flag
