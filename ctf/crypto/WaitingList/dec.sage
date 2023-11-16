import sys
import csv
import json
import challenge

DEBUG=True
def dbg(line, force=False, end='\n'):
    if DEBUG or force:
        print(line, flush=True, file=sys.stderr, end=end)
        pass
    pass

def prnt(line, force=False):
    dbg(line, force=force)
    print(line, flush=True)
    pass

def inp(lines=1, chars=0, force=False):
    line = ''
    for _ in range(lines):
        line = input()
        dbg(line, force=force)
    if chars > 0:
        dbg(sys.stdin.read(chars), force=force, end='')
    return line

def hash_msg(msg, n):
    from hashlib import sha1
    h = sha1(msg).digest()
    h = int.from_bytes(h, 'big')
    h = bin(h)[2:]
    h = int(h[:len(bin(n)[2:])], 2)
    return h

def inverse(x, n):
    return int(pow(x, -1, n))

def ppow(x, e, n):
    return int(pow(x, e, n))

def sign(dsa, msg):
    from random import randint
    h = hash_msg(msg, dsa.n)
    k = randint(1, dsa.n-1)
    r = pow(dsa.g, k, dsa.n)
    s = (pow(k, -1, dsa.n) * (h + dsa.key * r)) % dsa.n
    lsb = k % (2 ** 7)
    return {"h": hex(h)[2:], "r": hex(r)[2:], "s": hex(s)[2:], "lsb": bin(lsb)[2:] }

def verify_h(dsa, h, r, s):
    c = inverse(s, dsa.n)
    k = (c * (h + dsa.key * r)) % dsa.n
    return r == pow(dsa.g, k, dsa.n)

def verify_m(dsa, m, r, s):
    h = hash_msg(m, dsa.n)
    return verify_h(dsa, h, r, s)


if __name__ == '__main__':
    dsa = challenge.ECDSA()
    msg = b'william;yarmouth;22-11-2021;09:00'
    sig_r = 1
    sig_s = 0
    known_bits = 7

    mm = list()
    hrsa = list()
    # Read provided information
    with open('appointments.txt', 'r') as csvf:
        csvr = csv.reader(csvf)
        header = next(csvr)
        for row in csvr:
            mm.append(row[0].encode('utf8'))
            pass
        pass
    with open('signatures.txt', 'r') as csvf:
        csvr = csv.reader(csvf, delimiter=';')
        header = next(csvr)
        for h, r, s, a in csvr:
            hrsa.append( (int(h,16), int(r,16), int(s,16), int(a,2)) )
            pass
        pass
    
    # Compute coeffs
    bigB = 2**(len(bin(dsa.n)[2:]) - known_bits + 1) # Upper bound for all bi
    AA = list()
    BB = list()
    Fn = GF(dsa.n)
    h0, r0, s0, a0 = [Fn(x) for x in hrsa[0]]
    for i, (hi, ri, si, ai) in enumerate(hrsa):
        if i == 0:
            continue
        hi, ri, si, ai = Fn(hi), Fn(ri), Fn(si), Fn(ai)
        Ai = ri * si^-1 * r0^-1 * s0
        Bi = -1 * Fn(2)^-known_bits * (ai - si^-1 * (hi + r0^-1 * ri * (s0 * a0 - h0)))
        AA.append(Ai.lift())
        BB.append(Bi.lift())
        pass
    dbg(f"[+] Computed {len(AA)} coefficients.\n[+] Constructing lattice...")

    # Construct lattice
    size = len(AA)
    MM = Matrix(ZZ, size + 2)
    for ii in range(size):
        MM[ii, ii] = dsa.n
        MM[-2, ii] = AA[ii]
        MM[-1, ii] = BB[ii]
        pass
    MM[-2,-2] = 1
    MM[-1,-1] = bigB

    # Perform LLL
    dbg("[+] Performing base reduction...")
    MB = MM.LLL()                 # LLL sorts the basis vectors by size
    if Fn(MB[0, -1]) == Fn(bigB): # so we only check the first basis vector
        k0 = Fn(2)**known_bits * MB[0, -2] + a0
        dsa.key = ((s0 * k0 - h0) * r0^-1).lift()
        dbg('[+] Key candidate found!')
        pass
    else:
        dbg('[!] No candidate found :(')
        sys.exit()
    
    # Verify a signature to know that the key candidate is correct
    m1 = mm[1]
    _, r1, s1, a1 = hrsa[1]
    if verify_m(dsa, m1, r1, s1):
        wohoo = True
        dbg(f'[+] Candidate verifies correctly!')
        pass
    else:
        dbg("[!] Key candidate was not the key :(")
        sys.exit()

    # Craft signature for message
    dbg(f"[+] Crafting signature...")
    dic = sign(dsa, msg)

    # Print flag
    dbg(f"[+] Getting flag...\n")
    msg2server = json.dumps({'pt': msg.decode('ascii'), 'r': dic['r'], 's': dic['s']})
    
    prnt(msg2server)
    
    #inp(3, 2)
    #prnt(msg2server)
    #try:
    #    inp(2)
    #    pass
    #except:
    #    pass
    #pass
