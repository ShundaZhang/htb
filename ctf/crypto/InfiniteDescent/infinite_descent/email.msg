From:	CayceP <cayce.pollard@>
Sent:	11 August 2017 18:15
To:	Deschain, Roland
Subject:	Progress update

Hi Rolly,

Just a quick update. We've addressed your issues with the numpy PSNG by ditching it and created a mersenne twister from scratch.
This will be used as the pre-secret from the RSA exchange for bootstrapping the AES comms.

We have some problems with the RSA generator that we're ironing out. Security have some questions around the
way primes are chosen but I think they're just getting in the way. To prove it's working just fine I've sent your
private key through secure comms and your public key is below with the message; we've also used this to encrypt a pre-shared
secret. Can you decrypt with your private key and check the pre-shared key works with the twister?

Have a good weekend,

CayceP


-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgFbDk+zYy1tbjwPpsTWbYjIfBtZk
walARbJxLg6QhyalsGnBx064VFIH9XIKzPK/Dt1RzMO68gy7zLOiyipPtYb2n0M6
WcdDGgw9J9+xx4HjXZCHx4h4zQhfQeOYymeSPewXJOe+GT31ymz6/Q1Ulyq/jWnD
XZogxfbXi6bIwuN7AgMBAAE=
-----END PUBLIC KEY-----


-----BEGIN MESSAGE-----
41296290787170212566581926747559000694979534392034439796933335542554551981322424774631715454669002723657175134418412556653226439790475349107756702973735895193117931356004359775501074138668004417061809481535231402802835349794859992556874148430578703014721700812262863679987426564893631600671862958451813895661
-----END MESSAGE-----

