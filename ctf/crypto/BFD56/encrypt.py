from secret import pt,key,block_length
import random

alph = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def strmask(msg,mask):
    mask = (mask * ((len(msg)//len(mask)) + 1))
    return "".join([alph[(alph.index(i) + alph.index(j)) % 25] for i,j in zip(msg, mask)])

def strunmask(msg,mask):
    mask = (mask * ((len(msg)//len(mask)) + 1))
    return "".join([alph[(alph.index(i) - alph.index(j)) % 25] for i,j in zip(msg, mask)])

def encrypt_block(pt, indices, characters):
    res = [-1] * len(pt) * 2
    for i,c in enumerate(pt):
        res[i],res[i+len(pt)] = indices[c][0],indices[c][1]
    ret = ""
    for i in range(0,len(res),2):
        ret += characters[str(res[i]) + str(res[i+1])]
    return ret

def encrypt(plaintext, key, block_length):
    iv = "".join([random.sample(list(alph), 1)[0] for i in range(block_length)])
    
    indices = {}
    characters = {}
    for i,c in enumerate(key):
        indices[c] = str(i//5) +  str(i%5)
        characters[str(i//5) +  str(i%5)] = c

    plaintext_blocks = [plaintext[i : i + block_length] for i in range(0, len(plaintext), block_length)]

    ciphertext = ""
    cmask = iv
    for block in plaintext_blocks:
        block_enc = encrypt_block(strmask(block,cmask),indices,characters)
        ciphertext += block_enc
        cmask = block_enc

    return iv,ciphertext

with open('ciphertext.txt', 'w') as f:
    f.write(str(encrypt(pt,key,block_length)))
