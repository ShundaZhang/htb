from Crypto.Util.number import bytes_to_long, getPrime, getRandomRange
import socketserver
import signal
from typing import Callable
from secret import FLAG, fast_turbonacci, fast_turbocrypt


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def sendMessage(s, msg):
    s.send(msg.encode())


def receiveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def turbonacci(n: int, p: int, b: int, c: int) -> int:
    if n < 2:
        return n

    return (b * turbonacci(n - 1, p, b, c) +
            c * turbonacci(n - 2, p, b, c)) % p


def lcg(x: int, m: int, n: int, p: int) -> int:
    return (m * x + n) % p


def turbocrypt(pt: int, k: int, f: Callable[[int], int]) -> int:
    return sum((f(i + 1) - f(i)) for i in range(k, pt))


def menu(s) -> int:
    sendMessage(s, "Choose one option\n")
    sendMessage(s, "1. Encrypt flag\n")
    sendMessage(s, "2. Encrypt ciphertext\n")
    sendMessage(s, "3. Exit\n")

    return int(receiveMessage(s, "> "))


def main(s):
    while True:
        b, c, p = getPrime(512), getPrime(512), getPrime(512)

        try:
            for i in range(10):
                assert turbonacci(i, p, b, c) == fast_turbonacci(i, p, b, c)
                assert turbocrypt(i, -1, int) == fast_turbocrypt(i, -1, int)

            break
        except Exception as e:
            sendMessage(s, e)

    sendMessage(s, "Welcome to TurboCipher. Please login first\n")
    sendMessage(s, f"MathFA enabled. Parameters:\n{p = }\n{b = }\n{c = }\n\n")

    nonce = getRandomRange(1, p)
    sendMessage(s, f"Please, use {nonce = } to generate for your TurbOTP\n")

    otp = int(receiveMessage(s, "OTP: "))

    if otp != fast_turbonacci(nonce, p, b, c):
        sendMessage(s, "Login incorrect\n")
        exit(1)

    sendMessage(s, "Login successful\n")

    m, n, k = getPrime(512), getPrime(512), getPrime(512)

    def f(x: int) -> int:
        return lcg(x, m, n, p)

    while (option := menu(s)) != 3:
        if option == 1:
            assert len(FLAG) * 8 <= p.bit_length()
            sendMessage(
                s, f"ct = {fast_turbocrypt(bytes_to_long(FLAG), k, f) % p}\n")

        if option == 2:
            pt = receiveMessage(s, "pt = ").strip().encode()
            assert len(pt) * 8 <= p.bit_length()
            sendMessage(
                s, f"ct = {fast_turbocrypt(bytes_to_long(pt), k, f) % p}\n")

    sendMessage(s, "Thank you for using TurboCipher. See you soon!\n")


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
