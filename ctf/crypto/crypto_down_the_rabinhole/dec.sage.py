

# This file was *autogenerated* from the file dec.sage
from sage.all_cmdline import *   # import sage library

_sage_const_19776862259930835769533075141648724317136726865325219582974628641663028757626265811083579217562652521882819442186121072998911507994180202653223643709290080839913395525826127153190928840827396123760992080649033993986933259414523207699646834981906819263319717393978144309193843291629147724979917210633945695963741292906203710063193032172565935616940163881309010593278779797311032854042143 = Integer(19776862259930835769533075141648724317136726865325219582974628641663028757626265811083579217562652521882819442186121072998911507994180202653223643709290080839913395525826127153190928840827396123760992080649033993986933259414523207699646834981906819263319717393978144309193843291629147724979917210633945695963741292906203710063193032172565935616940163881309010593278779797311032854042143); _sage_const_18940449739373929782738747330951086701639920358124022449285915914681280430796481828627299763135820762855030234173393995786612606880441619894387463477558992819159868677736220547584576162287130594708254787956440732197673909613467337841562238900614238638819659960733399020443364866675611439229048487547611412841048501574753238490324081535533435151621545695715920828646120795059085207687562 = Integer(18940449739373929782738747330951086701639920358124022449285915914681280430796481828627299763135820762855030234173393995786612606880441619894387463477558992819159868677736220547584576162287130594708254787956440732197673909613467337841562238900614238638819659960733399020443364866675611439229048487547611412841048501574753238490324081535533435151621545695715920828646120795059085207687562); _sage_const_8139131820890905559667838555211733555742225714065473904284826530490173193882559461890851501765452084252909412188575022633596512451349296562551141247433279875212083704533696867645657058965269748533381751261887853181791035505421692256731545740535452608088572835061213186774986415770477686449034066741760771862922788827235376073691257160953903839272893965131226612277505938410382901008254 = Integer(8139131820890905559667838555211733555742225714065473904284826530490173193882559461890851501765452084252909412188575022633596512451349296562551141247433279875212083704533696867645657058965269748533381751261887853181791035505421692256731545740535452608088572835061213186774986415770477686449034066741760771862922788827235376073691257160953903839272893965131226612277505938410382901008254); _sage_const_26981290975895303933094134784682647576666219028610175215312705398803184876873073206073503314367717924247311343215620922642215797499997039996235807898656819655954778538207489354154710796202412578870511364360408739855039573753404337104901925571890067221867326539447741757218265017060345184819121122211405292705642802582423249795098475142694876497945367191724577275836649641722277321440333 = Integer(26981290975895303933094134784682647576666219028610175215312705398803184876873073206073503314367717924247311343215620922642215797499997039996235807898656819655954778538207489354154710796202412578870511364360408739855039573753404337104901925571890067221867326539447741757218265017060345184819121122211405292705642802582423249795098475142694876497945367191724577275836649641722277321440333); _sage_const_11417442976137891276889457530453693512824297007151561589652706330477531354073557298919952168938641673547415923544612769937040826488039629275033613885416852757446100888628373584968290007182319967658770715301605453943639269415203462531753249668211460008832837924575003999865632991329309338991536326471187269457640505585240846158952935988441171094886116683100214189858525596159931001818615 = Integer(11417442976137891276889457530453693512824297007151561589652706330477531354073557298919952168938641673547415923544612769937040826488039629275033613885416852757446100888628373584968290007182319967658770715301605453943639269415203462531753249668211460008832837924575003999865632991329309338991536326471187269457640505585240846158952935988441171094886116683100214189858525596159931001818615); _sage_const_18355127503780127719693553150263322113757549849264731376621241697648137569897555203319854095104524520716185245672659763235856966677160994023952943459682923666302498240656511471051133821432105321005228730688019003306690750456433049212247022010356640992865785005342800448602013572898416040572578635571772069565860571397553306232025854213437948953083273924864099046923310816080854899416432 = Integer(18355127503780127719693553150263322113757549849264731376621241697648137569897555203319854095104524520716185245672659763235856966677160994023952943459682923666302498240656511471051133821432105321005228730688019003306690750456433049212247022010356640992865785005342800448602013572898416040572578635571772069565860571397553306232025854213437948953083273924864099046923310816080854899416432); _sage_const_186 = Integer(186); _sage_const_4 = Integer(4); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_256 = Integer(256); _sage_const_93 = Integer(93); _sage_const_8 = Integer(8)#Franklin Reiter Attack
#https://richardfan1126.medium.com/cyber-apocalypse-ctf-2022-writeup-down-the-rabinhole-3fd2940aca45
#https://hackmd.io/@amyriad/acsc#Two-Rabin-crypto-Score-360-20-Solves
#https://chovid99.github.io/posts/cyber-apocalypse-ctf-2022/

from Crypto.Util.number import *

n1 = _sage_const_19776862259930835769533075141648724317136726865325219582974628641663028757626265811083579217562652521882819442186121072998911507994180202653223643709290080839913395525826127153190928840827396123760992080649033993986933259414523207699646834981906819263319717393978144309193843291629147724979917210633945695963741292906203710063193032172565935616940163881309010593278779797311032854042143 
c1 = _sage_const_18940449739373929782738747330951086701639920358124022449285915914681280430796481828627299763135820762855030234173393995786612606880441619894387463477558992819159868677736220547584576162287130594708254787956440732197673909613467337841562238900614238638819659960733399020443364866675611439229048487547611412841048501574753238490324081535533435151621545695715920828646120795059085207687562 
c2 = _sage_const_8139131820890905559667838555211733555742225714065473904284826530490173193882559461890851501765452084252909412188575022633596512451349296562551141247433279875212083704533696867645657058965269748533381751261887853181791035505421692256731545740535452608088572835061213186774986415770477686449034066741760771862922788827235376073691257160953903839272893965131226612277505938410382901008254 
n2 = _sage_const_26981290975895303933094134784682647576666219028610175215312705398803184876873073206073503314367717924247311343215620922642215797499997039996235807898656819655954778538207489354154710796202412578870511364360408739855039573753404337104901925571890067221867326539447741757218265017060345184819121122211405292705642802582423249795098475142694876497945367191724577275836649641722277321440333 
c3 = _sage_const_11417442976137891276889457530453693512824297007151561589652706330477531354073557298919952168938641673547415923544612769937040826488039629275033613885416852757446100888628373584968290007182319967658770715301605453943639269415203462531753249668211460008832837924575003999865632991329309338991536326471187269457640505585240846158952935988441171094886116683100214189858525596159931001818615 
c4 = _sage_const_18355127503780127719693553150263322113757549849264731376621241697648137569897555203319854095104524520716185245672659763235856966677160994023952943459682923666302498240656511471051133821432105321005228730688019003306690750456433049212247022010356640992865785005342800448602013572898416040572578635571772069565860571397553306232025854213437948953083273924864099046923310816080854899416432 
l = _sage_const_186 

#print(GCD(n1-4,n2-4)//3)
'''
sage: prime_factors(200243800433087265358395332994095289067)
[200243800433087265358395332994095289067]
sage: prime_factors(600731401299261796075185998982285867201)
[3, 200243800433087265358395332994095289067]
'''
coeff = GCD(n1-_sage_const_4 ,n2-_sage_const_4 )//_sage_const_3 

e = _sage_const_2 
B = coeff
delta1 = (B + n1) >> _sage_const_1 
delta2 = (B + n2) >> _sage_const_1 
c1 = (c1 + delta1**_sage_const_2 ) % n1
c2 = (c2 + delta1**_sage_const_2 ) % n1
c3 = (c3 + delta2**_sage_const_2 ) % n2
c4 = (c4 + delta2**_sage_const_2 ) % n2

# Source: https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/Attack-Franklin-Reiter/exploit.sage
def gcd(a, b):
     while b:
         a, b = b, a % b
     return a.monic()
def franklinreiter(C1, C2, e, N, a, b):
     P = PolynomialRing(Zmod(N), names=('X',)); (X,) = P._first_ngens(1)
     g1 = (a*X + b)**e - C1
     g2 = X**e - C2
     result = -gcd(g1, g2).coefficients()[_sage_const_0 ]
     return result

bg = bytes_to_long(b'\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3\xa3')

soln = franklinreiter(c2, c1, e, n1, _sage_const_1  << ((_sage_const_256 -_sage_const_93 )*_sage_const_8 ), bg + delta1 - (delta1 << ((_sage_const_256 -_sage_const_93 )*_sage_const_8 ))) - delta1
print(long_to_bytes(int(soln)))
soln = franklinreiter(c4, c3, e, n2, _sage_const_1  << ((_sage_const_256 -_sage_const_93 )*_sage_const_8 ), bg + delta2 - (delta2 << ((_sage_const_256 -_sage_const_93 )*_sage_const_8 ))) - delta2
print(long_to_bytes(int(soln)))

#b'HTB{You_were_supposed_to_find_the_gcd_trick_then_search_and_find_the_ACSC_writeup_learn_some_'
#b'interesting_stuff_and_solve_the_challege_but_I_forgot_about_the_most_basic_thing_I_m_sorry:(}'
#HTB{You_were_supposed_to_find_the_gcd_trick_then_search_and_find_the_ACSC_writeup_learn_some_interesting_stuff_and_solve_the_challege_but_I_forgot_about_the_most_basic_thing_I_m_sorry:(}
