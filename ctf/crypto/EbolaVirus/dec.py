'''
#key tream xor -- Failed...

from pwn import *
from itertools import permutations

with open('key.txt','r') as f:
        buf = f.readlines()
xk = buf[0]

with open('encrypted.bin','r') as f:
	buf = f.readlines()
ct = buf[0]

dna = ['G','A','T','C']

pdna = list(permutations(dna))

for kp in pdna:
        kb = ''
        for i in range(len(xk)):
                c = xk[i]
                if c == kp[0]:
                        kb += '00'
                elif c == kp[1]:
                        kb += '01'
                elif c == kp[2]:
                        kb += '10'
                else:
                        kb += '11'
        key = ''
        for i in range(0,len(kb),8):
                key += chr(int(kb[i:i+8],2))
        #print key
	#print xor(ct,key)
'''

#substitution: '\t' -> ' '

#!/usr/bin/python3

pset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
cset = []
pindex = 0
chmap = {}

with open('encrypted.bin', 'rb') as file:
    content = file.read()

ptext = ''
for h in content:
	if h == ord('\t'):
		chmap[h] = ' '
		ptext += ' '
	else:
		if h not in cset:
			cset.append(h)
			chmap[h] = pset[pindex]
			pindex += 1
		ptext += chmap[h]

print(ptext)

'''
abc defgh ijklm nhlmcm ho hnlpcq mckjflm jggocmm rbjnb jm fspco shphg js lopkchpctu defgh ijklm tjmchmc vdwxy sjkmp hzzchkct jo ABCD jo E mjFlgphocflm flpekchGmq foc jo rbhp jm ofrq HIhkhq Jflpb Jlthoq hot pbc fpbck jo KhFelGlq xcFfnkhpjn Lczlegjn fs MfoNfu abc ghppck fnnlkkct jo h ijgghNc ochk pbc defgh Ljickq skfF rbjnb pbc tjmchmc phGcm jpm ohFcuOOPp jm pbflNbp pbhp skljp ehpm fs pbc Qpckfzftjthc shFjgR hkc ohplkhg defgh ijklm bfmpmu defgh jm jopkftlnct jopf pbc blFho zfzlghpjfo pbkflNb ngfmc nfophnp rjpb pbc egfftq mcnkcpjfomq fkNhom fk fpbck eftjgR sgljtm fs joscnpct hojFhgm mlnb hm nbjFzhoIccmq Nfkjgghmq skljp ehpmq FfoGcRmq sfkcmp hopcgfzc hot zfknlzjocm sflot jgg fk tcht fk jo pbc khjosfkcmpuOOdefgh pbco mzkchtm pbkflNb blFhoSpfSblFho pkhomFjmmjfo ijh tjkcnp nfophnp vpbkflNb ekfGco mGjo fk Flnflm FcFekhocmy rjpb pbc egfftq mcnkcpjfomq fkNhom fk fpbck eftjgR sgljtm fs joscnpct zcfzgcq hot rjpb mlkshncm hot Fhpckjhgm vcuNu ecttjoNq ngfpbjoNy nfophFjohpct rjpb pbcmc sgljtmuTchgpbSnhkc rfkGckm bhic skcUlcopgR ecco joscnpct rbjgc pkchpjoN zhpjcopm rjpb mlmzcnpct fk nfosjkFct dwxu abjm bhm fnnlkkct pbkflNb ngfmc nfophnp rjpb zhpjcopm rbco joscnpjfo nfopkfg zkcnhlpjfom hkc ofp mpkjnpgR zkhnpjnctuVlkjhg nckcFfojcm pbhp joifgic tjkcnp nfophnp rjpb pbc eftR fs pbc tcnchmct nho hgmf nfopkjelpc jo pbc pkhomFjmmjfo fs defghu Qcfzgc kcFhjo joscnpjflm hm gfoN hm pbcjk egfft nfophjom pbc ijklmuOOabc jonlehpjfo zckjftq pbhp jmq pbc pjFc jopckihg skfF joscnpjfo rjpb pbc ijklm pf fomcp fs mRFzpfFm jm E pf EA thRmu TlFhom hkc ofp joscnpjflm lopjg pbcR tcicgfz mRFzpfFmu Wjkmp mRFzpfFm hkc pbc mlttco fomcp fs scick shpjNlcq Flmngc zhjoq bchthnbc hot mfkc pbkfhpu abjm jm sfggfrct eR ifFjpjoNq tjhkkbfchq khmbq mRFzpfFm fs jFzhjkct GjtocR hot gjick slonpjfoq hot jo mfFc nhmcmq efpb jopckohg hot cXpckohg egcctjoN vcuNu ffIjoN skfF pbc NlFmq egfft jo pbc mpffgmyu YhefkhpfkR sjotjoNm jongltc gfr rbjpc egfft ncgg hot zghpcgcp nflopm hot cgcihpct gjick coIRFcmuOOTaVZ012GH3r2b4r2pf2n3oak3g2de3g56OO

From https://www.boxentriq.com/ and http://quipqiup.com/
The plain text should be: the ebola virous causes an acu?e? serious which is often fa?al ...
Google it, found in who's website:
https://www.who.int/news-room/fact-sheets/detail/ebola-virus-disease?gclid=EAIaIQobChMI2Ir6oL_k-QIVDD6tBh3ljw-oEAAYASAAEgKH4_D_BwE
The Ebola virus causes an acute, serious illness which is often fatal if untreated. 

Continue to search "The Ebola virus causes an acute, serious illness which is often fatal if untreated. Ebola virus disease first appeared in"

OO is \n\n, and we need to choose text from different paragraphs in the website...

The Ebola virus causes an acute, serious illness which is often fatal if untreated. Ebola virus disease (EVD) first appeared in 1976 in 2 simultaneous outbreaks, one in what is now, Nzara, South Sudan, and the other in Yambuku, Democratic Republic of Congo. The latter occurred in a village near the Ebola River, from which the disease takes its name.

It is thought that fruit bats of the Pteropodidae family are natural Ebola virus hosts. Ebola is introduced into the human population through close contact with the blood, secretions, organs or other bodily fluids of infected animals such as chimpanzees, gorillas, fruit bats, monkeys, forest antelope and porcupines found ill or dead or in the rainforest.

Ebola then spreads through human-to-human transmission via direct contact (through broken skin or mucous membranes) with the blood, secretions, organs or other bodily fluids of infected people, and with surfaces and materials (e.g. bedding, clothing) contaminated with these fluids. Health-care workers have frequently been infected while treating patients with suspected or confirmed EVD. This has occurred through close contact with patients when infection control precautions are not strictly practiced. Burial ceremonies that involve direct contact with the body of the deceased can also contribute in the transmission of Ebola. People remain infectious as long as their blood contains the virus. 

The incubation period, that is, the time interval from infection with the virus to onset of symptoms is 2 to 21 days. Humans are not infectious until they develop symptoms. First symptoms are the sudden onset of fever fatigue, muscle pain, headache and sore throat. This is followed by vomiting, diarrhoea, rash, symptoms of impaired kidney and liver function, and in some cases, both internal and external bleeding (e.g. oozing from the gums, blood in the stools). Laboratory findings include low white blood cell and platelet counts and elevated liver enzymes.

'''

p1 = 'abc defgh ijklm nhlmcm ho hnlpcq mckjflm jggocmm rbjnb jm fspco shphg js lopkchpctu defgh ijklm tjmchmc vdwxy sjkmp hzzchkct jo ABCD jo E mjFlgphocflm flpekchGmq foc jo rbhp jm ofrq HIhkhq Jflpb Jlthoq hot pbc fpbck jo KhFelGlq xcFfnkhpjn Lczlegjn fs MfoNfu abc ghppck fnnlkkct jo h ijgghNc ochk pbc defgh Ljickq skfF rbjnb pbc tjmchmc phGcm jpm ohFcu Pp jm pbflNbp pbhp skljp ehpm fs pbc Qpckfzftjthc shFjgR hkc ohplkhg defgh ijklm bfmpmu defgh jm jopkftlnct jopf pbc blFho zfzlghpjfo pbkflNb ngfmc nfophnp rjpb pbc egfftq mcnkcpjfomq fkNhom fk fpbck eftjgR sgljtm fs joscnpct hojFhgm mlnb hm nbjFzhoIccmq Nfkjgghmq skljp ehpmq FfoGcRmq sfkcmp hopcgfzc hot zfknlzjocm sflot jgg fk tcht fk jo pbc khjosfkcmpu defgh pbco mzkchtm pbkflNb blFhoSpfSblFho pkhomFjmmjfo ijh tjkcnp nfophnp vpbkflNb ekfGco mGjo fk Flnflm FcFekhocmy rjpb pbc egfftq mcnkcpjfomq fkNhom fk fpbck eftjgR sgljtm fs joscnpct zcfzgcq hot rjpb mlkshncm hot Fhpckjhgm vcuNu ecttjoNq ngfpbjoNy nfophFjohpct rjpb pbcmc sgljtmu TchgpbSnhkc rfkGckm bhic skcUlcopgR ecco joscnpct rbjgc pkchpjoN zhpjcopm rjpb mlmzcnpct fk nfosjkFct dwxu abjm bhm fnnlkkct pbkflNb ngfmc nfophnp rjpb zhpjcopm rbco joscnpjfo nfopkfg zkcnhlpjfom hkc ofp mpkjnpgR zkhnpjnctu Vlkjhg nckcFfojcm pbhp joifgic tjkcnp nfophnp rjpb pbc eftR fs pbc tcnchmct nho hgmf nfopkjelpc jo pbc pkhomFjmmjfo fs defghu Qcfzgc kcFhjo joscnpjflm hm gfoN hm pbcjk egfft nfophjom pbc ijklmu abc jonlehpjfo zckjftq pbhp jmq pbc pjFc jopckihg skfF joscnpjfo rjpb pbc ijklm pf fomcp fs mRFzpfFm jm E pf EA thRmu TlFhom hkc ofp joscnpjflm lopjg pbcR tcicgfz mRFzpfFmu Wjkmp mRFzpfFm hkc pbc mlttco fomcp fs scick shpjNlcq Flmngc zhjoq bchthnbc hot mfkc pbkfhpu abjm jm sfggfrct eR ifFjpjoNq tjhkkbfchq khmbq mRFzpfFm fs jFzhjkct GjtocR hot gjick slonpjfoq hot jo mfFc nhmcmq efpb jopckohg hot cXpckohg egcctjoN vcuNu ffIjoN skfF pbc NlFmq egfft jo pbc mpffgmyu YhefkhpfkR sjotjoNm jongltc gfr rbjpc egfft ncgg hot zghpcgcp nflopm hot cgcihpct gjick coIRFcmu'

p2 = 'The Ebola virus causes an acute, serious illness which is often fatal if untreated. Ebola virus disease (EVD) first appeared in 1976 in 2 simultaneous outbreaks, one in what is now, Nzara, South Sudan, and the other in Yambuku, Democratic Republic of Congo. The latter occurred in a village near the Ebola River, from which the disease takes its name. It is thought that fruit bats of the Pteropodidae family are natural Ebola virus hosts. Ebola is introduced into the human population through close contact with the blood, secretions, organs or other bodily fluids of infected animals such as chimpanzees, gorillas, fruit bats, monkeys, forest antelope and porcupines found ill or dead or in the rainforest. Ebola then spreads through human-to-human transmission via direct contact (through broken skin or mucous membranes) with the blood, secretions, organs or other bodily fluids of infected people, and with surfaces and materials (e.g. bedding, clothing) contaminated with these fluids. Health-care workers have frequently been infected while treating patients with suspected or confirmed EVD. This has occurred through close contact with patients when infection control precautions are not strictly practiced. Burial ceremonies that involve direct contact with the body of the deceased can also contribute in the transmission of Ebola. People remain infectious as long as their blood contains the virus. The incubation period, that is, the time interval from infection with the virus to onset of symptoms is 2 to 21 days. Humans are not infectious until they develop symptoms. First symptoms are the sudden onset of fever fatigue, muscle pain, headache and sore throat. This is followed by vomiting, diarrhoea, rash, symptoms of impaired kidney and liver function, and in some cases, both internal and external bleeding (e.g. oozing from the gums, blood in the stools). Laboratory findings include low white blood cell and platelet counts and elevated liver enzymes.'

#print(len(p1))
#print(len(p2))

smap = {}

for i in range(len(p1)):
	smap[p1[i]] = p2[i]

cs = ''
for i in smap.values():
	cs += i
print(''.join(sorted(cs)))

f = 'TaVZ012GH3r2b4r2pf2n3oak3g2de3g56'
for x in f:
	try:
		print(smap[x],end='')
	except:
		print('?',end='')
print('')

'''
TaVZ012GH3r2b4r2pf2n3oak3g2de3g56
HTB????kN?w?h?w?to?c?nTr?l?Eb?l??
HTB{W3_kNOw_h0w_to_cOnTrOl_EbOlA}
HTB{W3_kNOw_h0w_to_cOnTrOl_EbOl4}
HTB{W3_kN0w_hOw_to_c0nTr0l_Eb0lA}
HTB{W3_kN0w_hOw_to_c0nTr0l_Eb0l4} #Bingo!!
'''
