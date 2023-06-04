from random import randint, seed, sample, getstate
import math
from secret import SEED, FLAG, INIT


class MH:

    def __init__(self, size):
        keys = self.generateKeys(size)
        self.public_key = keys[0]
        self.private_key = keys[1]

    def generateKeys(self, n):
        private_key = [INIT] + [0 for _ in range(n - 1)]

        for i in range(1, n):
            total = sum(private_key)
            private_key[i] = randint(total * 2, total * 3)

        total = sum(private_key)
        modulo = randint(total * 2, total * 3)

        while True:
            multiplier = randint(modulo // 4, modulo - 1)
            if math.gcd(multiplier, modulo) == 1:
                break

        public_key = [multiplier * private_key[i] % modulo for i in range(n)]

        return public_key, private_key

    def encrypt(self, plaintext):
        ciphertext = []

        for number in plaintext:
            result = 0
            bits = bin(number)[2:].zfill(32)

            for bit, multiplier in zip(bits, self.public_key):
                result += multiplier * int(bit)

            ciphertext.append(result)

        return ciphertext


def encrypt(plaintext):
    random_number = randint(1, 2**8)

    shuffled_flag = ''.join(sample(plaintext, len(plaintext)))

    encrypted_flag = 0

    for char in shuffled_flag:
        char = ord(char)
        encrypted_flag = encrypted_flag * pow(random_number, char)
        encrypted_flag += char

    return encrypted_flag


def main():
    seed(SEED)
    state = getstate()

    encrypted_flag = encrypt(FLAG)

    mh = MH(32)

    encrypted_state_one = mh.encrypt(state[1])
    encrypted_state = [state[0], encrypted_state_one, state[2]]

    with open("out.txt", "w") as f:
        out = f"{encrypted_flag}\n{encrypted_state}\n{mh.public_key}\n"
        f.write(out)


if __name__ == "__main__":
    main()
