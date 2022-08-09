from Crypto.Util.number import bytes_to_long, long_to_bytes
from hashlib import sha1
import gmpy2

class RSA():

    def __init__(self, key_length):
        self.asn1 = b"\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14"
        self.e = 3
        phi = 0

    def pad(self, message, target_length):
        max_message_length = target_length - 11
        message_length = len(message)

        if message_length > max_message_length:
            raise OverflowError(
                "%i bytes needed for message, but there is only"
                " space for %i" % (message_length, max_message_length))

        padding_length = target_length - message_length - 3

        return b"".join(
            [b"\x00\x01", padding_length * b"\xff", b"\x00", message])

    def sign(self, message):
        hash_value = sha1(message).digest()

        keylength = 2048//8
        cleartext = self.asn1 + hash_value
        padded = self.pad(cleartext, keylength)

        payload = bytes_to_long(padded)
	return payload

def parseEmail():
    with open("email.txt", "r") as f:
        data = f.readlines()
    user = data[0].strip()[len("From: "):]
    return user.encode(), "".join(data)


rsa = RSA(2048)
user, data = parseEmail()
signature = rsa.sign(user)
print signature

#986236757547332986472011617696226561292849812918563355472727826767720188564083584387121625107510786855734801053524719833194566624465665316622563244215340671405971599343902468620306327831715457360719532421388780770165778156818229863337344187575566725786793391480600129482653072861971002459947277805295727097226389568776499707662505334062639449916265137796823793276300221537201727072401742985542559596685092673521228140822200236743113743661549252453726123450722876929538747702356573783116366629850199080495560991841329893037291900147497007197055572787780928474439122360300066096881077059728668470508523742314639984

#'\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x000!0\t\x06\x05+\x0e\x03\x02\x1a\x05\x00\x04\x14\xdb}\xdd?yeA\xdaO\x80]yHo\xd3w\x07\x9c2p'

x='\x00\x01\xff\x000!0\t\x06\x05+\x0e\x03\x02\x1a\x05\x00\x04\x14\xdb}\xdd?yeA\xdaO\x80]yHo\xd3w\x07\x9c2p'
x += 217*'\x00'

x = bytes_to_long(x)
print hex(x)
print gmpy2.iroot(x,3)
#994743055801596368131619876861883420729547954957569195003693435400932739719594287994577619462354210007224089820831699884770415323130791945374295041634009381818725832503119507015719394888165181349768697984+1
print hex(994743055801596368131619876861883420729547954957569195003693435400932739719594287994577619462354210007224089820831699884770415323130791945374295041634009381818725832503119507015719394888165181349768697985**3)
print '=========================================='
print hex(994743055801596368131619876861883420729547954957569195003693435400932739719594287994577619462354210007224089820831699884770415323130791945374295041634009381818725832503119507015719394888165181349768697985)[2:-1]

#HTB{4_8131ch3n84ch32_254_vu1n}
