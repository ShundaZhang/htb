from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime, inverse
from Crypto.PublicKey import RSA as PYRSA
from math import gcd
from hashlib import sha1
import re


class CryptoError(Exception):
    """Base class for all exceptions in this module."""


class VerificationError(CryptoError):
    """Raised when verification fails."""


class RSA():

    def __init__(self, key_length):
        self.asn1 = b"\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14"
        self.e = 3
        phi = 0

        while gcd(self.e, phi) != 1:
            p, q = getPrime(key_length // 2), getPrime(key_length // 2)
            phi = (p - 1) * (q - 1)
            self.n = p * q

        self.d = inverse(self.e, phi)
        self.key = PYRSA.construct((self.n, self.e), True)

    def encrypt(self, message):
        message = bytes_to_long(message)
        return pow(message, self.e, self.n)

    def decrypt(self, encrypted_message):
        message = pow(encrypted_message, self.d, self.n)
        return long_to_bytes(message)

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

        keylength = len(long_to_bytes(self.n))
        cleartext = self.asn1 + hash_value
        padded = self.pad(cleartext, keylength)

        payload = bytes_to_long(padded)
        block = self.decrypt(payload)

        return block

    def verify(self, message, signature):
        keylength = len(long_to_bytes(self.n))
        decrypted = self.encrypt(signature)
        clearsig = decrypted.to_bytes(keylength, "big")

        r = re.compile(b'\x00\x01\xff+?\x00(.{15})(.{20})', re.DOTALL)
        m = r.match(clearsig)

        if not m:
            raise VerificationError('Verification failed')

        if m.group(1) != self.asn1:
            raise VerificationError('Verification failed')

        if m.group(2) != sha1(message).digest():
            raise VerificationError('Verification failed')

        return True

    def export_key(self):
        return self.key.export_key('PEM').decode()
