'''
openssl rsa -text -noout -pubin -in key1.pem
RSA Public-Key: (2048 bit)
Modulus:
    00:c6:ac:b8:df:48:6e:66:71:d4:a5:56:48:03:e1:
    c3:21:4a:8e:27:4d:e0:ac:00:43:ec:28:c8:58:9f:
    37:7c:7e:8d:30:8b:c3:e3:02:85:03:84:34:4b:a7:
    98:88:85:62:0a:41:8e:6a:d9:55:57:82:84:fc:04:
    f2:89:f1:26:b3:8a:01:81:62:51:ce:f9:a1:4f:d4:
    c2:49:d9:6b:69:08:7f:a9:1b:2e:1a:db:dc:80:cb:
    96:ff:0c:cb:61:29:d8:f6:73:7d:a8:50:c4:51:f2:
    ed:3f:6c:b6:1c:36:89:1d:c9:24:d0:ab:28:f2:6a:
    df:0e:d3:57:ce:84:8d:02:ff:e0:09:12:71:4c:cf:
    63:72:c1:f4:10:80:e8:67:47:a0:30:3e:b5:cd:f6:
    ce:91:2f:11:44:fd:4f:55:74:3c:79:68:75:a1:4f:
    df:f8:f8:b6:62:15:0c:56:be:58:b0:92:39:77:1d:
    c4:4d:96:90:79:c4:ad:8f:d9:93:bc:63:0b:78:55:
    d2:e0:2e:8b:e1:68:24:dc:d5:ab:38:13:23:1c:17:
    31:11:0a:8b:d0:28:d7:a1:df:ab:89:2e:75:29:45:
    57:ba:fc:71:ae:af:5e:48:db:02:67:a6:db:63:d3:
    50:f9:95:06:8e:e1:ca:d6:d3:2d:f1:1a:49:bd:24:
    ba:97
Exponent: 65537 (0x10001)
openssl rsa -text -noout -pubin -in key2.pem
RSA Public-Key: (2048 bit)
Modulus:
    00:c6:ac:b8:df:48:6e:66:71:d4:a5:56:48:03:e1:
    c3:21:4a:8e:27:4d:e0:ac:00:43:ec:28:c8:58:9f:
    37:7c:7e:8d:30:8b:c3:e3:02:85:03:84:34:4b:a7:
    98:88:85:62:0a:41:8e:6a:d9:55:57:82:84:fc:04:
    f2:89:f1:26:b3:8a:01:81:62:51:ce:f9:a1:4f:d4:
    c2:49:d9:6b:69:08:7f:a9:1b:2e:1a:db:dc:80:cb:
    96:ff:0c:cb:61:29:d8:f6:73:7d:a8:50:c4:51:f2:
    ed:3f:6c:b6:1c:36:89:1d:c9:24:d0:ab:28:f2:6a:
    df:0e:d3:57:ce:84:8d:02:ff:e0:09:12:71:4c:cf:
    63:72:c1:f4:10:80:e8:67:47:a0:30:3e:b5:cd:f6:
    ce:91:2f:11:44:fd:4f:55:74:3c:79:68:75:a1:4f:
    df:f8:f8:b6:62:15:0c:56:be:58:b0:92:39:77:1d:
    c4:4d:96:90:79:c4:ad:8f:d9:93:bc:63:0b:78:55:
    d2:e0:2e:8b:e1:68:24:dc:d5:ab:38:13:23:1c:17:
    31:11:0a:8b:d0:28:d7:a1:df:ab:89:2e:75:29:45:
    57:ba:fc:71:ae:af:5e:48:db:02:67:a6:db:63:d3:
    50:f9:95:06:8e:e1:ca:d6:d3:2d:f1:1a:49:bd:24:
    ba:97
Exponent: 343223 (0x53cb7)

echo RBVdQw7Pllwb42GDYyRa6ByVOfzRrZHmxBkUPD393zxOcrNRZgfub1mqcrAgX4PAsvAOWptJSHbrHctFm6rJLzhBi/rAsKGboWqPAWYIu49Rt7Sc/5+LE2dvy5zriAKclchv9d+uUJ4/kU/vcpg2qlfTnyor6naBsZQvRze0VCMkPvqWPuE6iL6YEAjZmLWmb+bqO+unTLF4YtM1MkKTtiOEy+Bbd4LxlXIO1KSFVOoGjyLW2pVIgKzotB1/9BwJMKJV14/+MUEiP40ehH0U2zr8BeueeXp6NIZwS/9svmvmVi06Np74EbL+aeB4meaXH22fJU0eyL2FppeyvbVaYQ==|base64 -d|xxd
00000000: 4415 5d43 0ecf 965c 1be3 6183 6324 5ae8  D.]C...\..a.c$Z.
00000010: 1c95 39fc d1ad 91e6 c419 143c 3dfd df3c  ..9........<=..<
00000020: 4e72 b351 6607 ee6f 59aa 72b0 205f 83c0  Nr.Qf..oY.r. _..
00000030: b2f0 0e5a 9b49 4876 eb1d cb45 9baa c92f  ...Z.IHv...E.../
00000040: 3841 8bfa c0b0 a19b a16a 8f01 6608 bb8f  8A.......j..f...
00000050: 51b7 b49c ff9f 8b13 676f cb9c eb88 029c  Q.......go......
00000060: 95c8 6ff5 dfae 509e 3f91 4fef 7298 36aa  ..o...P.?.O.r.6.
00000070: 57d3 9f2a 2bea 7681 b194 2f47 37b4 5423  W..*+.v.../G7.T#
00000080: 243e fa96 3ee1 3a88 be98 1008 d998 b5a6  $>..>.:.........
00000090: 6fe6 ea3b eba7 4cb1 7862 d335 3242 93b6  o..;..L.xb.52B..
000000a0: 2384 cbe0 5b77 82f1 9572 0ed4 a485 54ea  #...[w...r....T.
000000b0: 068f 22d6 da95 4880 ace8 b41d 7ff4 1c09  .."...H.........
000000c0: 30a2 55d7 8ffe 3141 223f 8d1e 847d 14db  0.U...1A"?...}..
000000d0: 3afc 05eb 9e79 7a7a 3486 704b ff6c be6b  :....yzz4.pK.l.k
000000e0: e656 2d3a 369e f811 b2fe 69e0 7899 e697  .V-:6.....i.x...
000000f0: 1f6d 9f25 4d1e c8bd 85a6 97b2 bdb5 5a61  .m.%M.........Za

echo TSHSOfFBkK/sSE4vWxy00EAnZXrIsBI/Y6mGv466baOsST+qyYXHdPsI33Kr6ovucDjgDw/VvQtsAuGhthLbLVdldt9OWDhK5lbM6e0CuhKSoJntnvCz7GtZvjgPM7JDHQkAU7Pcyall9UEqL+W6ZCkiSQnK+j6QB7ynwCsW1wAmnCM68fY2HaBvd8RP2+rPgWv9grcEBkXf7ewA+sxSw7hahMaW0LYhsMYUggrcKqhofGgl+4UR5pdSiFg4YKUSgdSw1Ic/tug9vfHuLSiiuhrtP38yVzazqOZPXGxG4tQ6btc1helH0cLfw1SCdua1ejyan9l1GLXsAyGOKSFdKw==|base64 -d|xxd
00000000: 4d21 d239 f141 90af ec48 4e2f 5b1c b4d0  M!.9.A...HN/[...
00000010: 4027 657a c8b0 123f 63a9 86bf 8eba 6da3  @'ez...?c.....m.
00000020: ac49 3faa c985 c774 fb08 df72 abea 8bee  .I?....t...r....
00000030: 7038 e00f 0fd5 bd0b 6c02 e1a1 b612 db2d  p8......l......-
00000040: 5765 76df 4e58 384a e656 cce9 ed02 ba12  Wev.NX8J.V......
00000050: 92a0 99ed 9ef0 b3ec 6b59 be38 0f33 b243  ........kY.8.3.C
00000060: 1d09 0053 b3dc c9a9 65f5 412a 2fe5 ba64  ...S....e.A*/..d
00000070: 2922 4909 cafa 3e90 07bc a7c0 2b16 d700  )"I...>.....+...
00000080: 269c 233a f1f6 361d a06f 77c4 4fdb eacf  &.#:..6..ow.O...
00000090: 816b fd82 b704 0645 dfed ec00 facc 52c3  .k.....E......R.
000000a0: b85a 84c6 96d0 b621 b0c6 1482 0adc 2aa8  .Z.....!......*.
000000b0: 687c 6825 fb85 11e6 9752 8858 3860 a512  h|h%.....R.X8`..
000000c0: 81d4 b0d4 873f b6e8 3dbd f1ee 2d28 a2ba  .....?..=...-(..
000000d0: 1aed 3f7f 3257 36b3 a8e6 4f5c 6c46 e2d4  ..?.2W6...O\lF..
000000e0: 3a6e d735 85e9 47d1 c2df c354 8276 e6b5  :n.5..G....T.v..
000000f0: 7a3c 9a9f d975 18b5 ec03 218e 2921 5d2b  z<...u....!.)!]+

'''

import gmpy2

n = 0x00c6acb8df486e6671d4a5564803e1c3214a8e274de0ac0043ec28c8589f377c7e8d308bc3e302850384344ba7988885620a418e6ad955578284fc04f289f126b38a01816251cef9a14fd4c249d96b69087fa91b2e1adbdc80cb96ff0ccb6129d8f6737da850c451f2ed3f6cb61c36891dc924d0ab28f26adf0ed357ce848d02ffe00912714ccf6372c1f41080e86747a0303eb5cdf6ce912f1144fd4f55743c796875a14fdff8f8b662150c56be58b09239771dc44d969079c4ad8fd993bc630b7855d2e02e8be16824dcd5ab3813231c1731110a8bd028d7a1dfab892e75294557bafc71aeaf5e48db0267a6db63d350f995068ee1cad6d32df11a49bd24ba97

e1 = 65537
e2 = 343223

c1 = 0x44155d430ecf965c1be3618363245ae81c9539fcd1ad91e6c419143c3dfddf3c4e72b3516607ee6f59aa72b0205f83c0b2f00e5a9b494876eb1dcb459baac92f38418bfac0b0a19ba16a8f016608bb8f51b7b49cff9f8b13676fcb9ceb88029c95c86ff5dfae509e3f914fef729836aa57d39f2a2bea7681b1942f4737b45423243efa963ee13a88be981008d998b5a66fe6ea3beba74cb17862d335324293b62384cbe05b7782f195720ed4a48554ea068f22d6da954880ace8b41d7ff41c0930a255d78ffe3141223f8d1e847d14db3afc05eb9e797a7a3486704bff6cbe6be6562d3a369ef811b2fe69e07899e6971f6d9f254d1ec8bd85a697b2bdb55a61

c2 = 0x4d21d239f14190afec484e2f5b1cb4d04027657ac8b0123f63a986bf8eba6da3ac493faac985c774fb08df72abea8bee7038e00f0fd5bd0b6c02e1a1b612db2d576576df4e58384ae656cce9ed02ba1292a099ed9ef0b3ec6b59be380f33b2431d090053b3dcc9a965f5412a2fe5ba6429224909cafa3e9007bca7c02b16d700269c233af1f6361da06f77c44fdbeacf816bfd82b7040645dfedec00facc52c3b85a84c696d0b621b0c614820adc2aa8687c6825fb8511e6975288583860a51281d4b0d4873fb6e83dbdf1ee2d28a2ba1aed3f7f325736b3a8e64f5c6c46e2d43a6ed73585e947d1c2dfc3548276e6b57a3c9a9fd97518b5ec03218e29215d2b

#print gmpy2.gcdext(e1,e2)
z,x,y = gmpy2.gcdext(e1,e2)

#print z
#print x
#print y

#m = c1^x*c2^y mod n

m = (pow(c1,x,n)*pow(c2,y,n))%n

print hex(m)[2:].decode('hex')
