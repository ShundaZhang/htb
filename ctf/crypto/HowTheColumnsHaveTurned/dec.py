key = '148823505998502'

def deriveKey(key):
	derived_key = []

	for i, char in enumerate(key):
		previous_letters = key[:i]
		new_number = 1
		for j, previous_char in enumerate(previous_letters):
			if previous_char > char:
				derived_key[j] += 1
			else:
				new_number += 1
		derived_key.append(new_number)
	return derived_key


print deriveKey(key)


def transpose(array):
    return [row for row in map(list, zip(*array))]


def flatten(array):
    return "".join([i for sub in array for i in sub])


def twistedColumnarEncrypt(pt, key):
    #derived_key = deriveKey(key)
    derived_key = key

    width = len(key)

    blocks = [pt[i:i + width] for i in range(0, len(pt), width)]
    blocks = transpose(blocks)

    ct = [blocks[derived_key.index(i + 1)][::-1] for i in range(width)]
    ct = flatten(ct)
    return ct

#key = [4,1,2,3]
#message = '0123456789abcdef'
#ct = twistedColumnarEncrypt(message, key)
#print ct

'''

4 1 2 3
-------
0 1 2 3
4 5 6 7
8 9 a b
c d e f

d951ea62fb73c840
Columnar, but each block reversed
'''

key = [3, 7, 11, 12, 4, 6, 8, 1, 9, 14, 15, 13, 10, 2, 5]

msgs = ['ETYDEDTYAATOSTTUFTEETHIVHMVOSFNANDHEGIIIOCESTHTCHDHNRNYALSRPDAIRDCEEIFREEEEOETLRTRNLEEUNBEOIPYLTNOVEOAOTN',
'EECNEMOTCYSSSEORIRCETFDUCEDAATAPATWTTSKTTRROCEANHHHAIHOGPTTGROIEETURAFYUIPUEEONOISECNJISAFALRIUAVSAAVPDES',
'GTNOERUTOIAOTIGRESHHBTSEHLORSRSSNTWINTEAUEENTAEEENOICCAFOSHDORLUFHRIALNGOYPNCEIGTAYAPETHCEOUATEFISTFBPSVK',
'SNUTCAGPEEPWLHITEDFNDMPNWSHFORSLEOAIPTAPEOOOAOTGOSESNADRITRAEREOSSNPECUHSNHENSAATETTPSIUIUOOHPNSKTNIRYHFT',
'WFAFDDSGIMMYTADNHRENINONSRSUMNITAHIANSUOEMAAEDAIFLOTFINEAYNEGYSNKROEOGFTCTNLYIIOODLOIRERVTAROTRROUNUTFAUP']

#key = [4,1,2,3]
#msgs = ['d951ea62fb73c840']

ln = len(msgs[0])
lk = len(key)
k = ln/lk
for msg in msgs:
	t = []
	for j in range(k):
		t.append(['']*lk)

	for i in range(0,len(msg),k):
		a  = msg[i:i+k]
		a = a[::-1]
		for j in range(k):
			t[j][key.index(i/k+1)] = a[j]
	f = ''
	for x in t:
		f += ''.join(x)

	print f

'''
THELOCATIONOFTHECONVOYDANTEISDETERMINEDTOBEONTHETHIRDPLANETAFTERVINYRYOUCANUSELIGHTSPEEDAFTERTHEDELIVERYS
THECARGOISSAFEWENEEDTOMOVEFASTCAUSETHERADARSAREPICKINGUPSUSPICIOUSACTIVITYAROUNDTHETRAJECTORYOFTHEPLANETA
BECAREFULSKOLIWHENYOUARRIVEATTHEPALACEOFSCIONSAYTHECODEPHRASETOGETINHTBTHISRNGISNOTSAFEFORGENETINGOUTPUTS
DONTFORGETTOCHANGETHEDARKFUELOFTHESPACESHIPWEDONTWANTANYUNPLEASANTSURPRISESTOHAPPENTHISSERIOUSMISSIONPOPO
IFYOUMESSUPAGAINILLSENDYOUTOTHEANDROIDGRAVEYARDTOSUFFERFROMTHECONSTANTTERMINATIONOFYOURKINDAFINALWARNINGM

HTB{THISRNGISNOTSAFEFORGENETINGOUTPUTS}
'''

