from Crypto.Util.number import *
from secrets import *
import json

"""
from Crypto.PublicKey import DSA
k = DSA.generate(2048)
print(f"{k.p = }")
print(f"{k.q = }")
print(f"{k.g = }")
"""
p = 30514860220781649196505378618677588344627509796136052197766721133333403517227804826248671926331671978511695325934422209350872533631963158343821543243314354301612941382823755283391175569282500778759917825290265500008435125458284371701669393617263164707568562478942069967845682300866897274415749964510071038555145487346022921591488265881313448995313340365972250251431925090356830155846705412769705029295847471355919584592321591959772488755986181054597974081870037624260173234561447688627353479361867003340196122160639547860024025674714107946196423198018724048310862485718766310003158603549746994074302705926658218700843
q = 26189572440233739420990528170531051459310363621928135990243626537967
g = 6111748161621056558453263711027460170929636824002846224800107291166700007147256826554286465237732729099376511591848799483754962591483370638607627034808201246023891469880792589537431156477847873086973414247654773443349132863425799271140168302068820170758172107172379842519843597077356839020025609506792115532019927453283319270046204956352057936972814681479252626295814756888943630138110534869191473166355939365725603055249365076889191708484425425599800051451167006426087674425090967640170968963795028092131692666710522291627118158125917935888441403300632869010691598781782043810771106247022549721544793735832383283054
x = randbelow(p)
y = pow(g, x, p)

def sign(message):
    m = bytes_to_long(message)
    k = randbelow(p)
    r = pow(g, k, p) % q
    s = (inverse(k, q) * (m + x*r)) % q
    return r, s

def verify(message, r, s):
    assert 0 < r < q
    assert 0 < s < q
    m = bytes_to_long(message)
    w = pow(s, -1, q)
    u1 = (m * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return r == v

menu = """Vitalium Storage Panel Menu:
[0] Get public key of server
[1] Make an account
[2] View coordinates of vitalium stashes
[3] Exit
"""

def panel():
    while True:
        try:
            print(menu)
            option = int(input("Enter option > "))
            if option == 0:
                print(json.dumps({
                    'p': p,
                    'q': q,
                    'g': g,
                    'y': y
                }))
            elif option == 1:
                username = input("Enter username > ")
                message = json.dumps({"username": username, "admin": False})
                r, s = sign(message.encode())
                print(json.dumps({
                    'r': r,
                    's': s,
                    'message': message
                }))
            elif option == 2:
                r = int(input("r > "))
                s = int(input("s > "))
                message = input("message > ").encode()
                if verify(message, r, s):
                    data = json.loads(message)
                    if data["admin"]:
                        print(f"Hello admin! Here are the coordinates to your vitalium stash: {open('flag.txt').read()}")
                    else:
                        print(f"You must be admin to see the coordinates.")
                else:
                    print(f"Signature Invalid. Breach attempt detected, exiting...")
                    exit(-1)
            else:
                print("Exiting")
                exit(0)
        except Exception as e:
            print("An error occurred, exiting", e)
            exit(-1)
            
panel()
