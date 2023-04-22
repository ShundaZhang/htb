from secret import FLAG, N

MENU = '''
YALM (Yet Another Lost Modulus):

1. Get secret
2. Test encryption
3. Exit
'''


class YALM:

    def __init__(self):
        self.e = 3
        self.n = N

    def get_secret(self):
        message = f'Hey! This is my secret... it is secure because RSA is extremely strong and very hard to break... Here you go: {FLAG}'
        m = int(message.encode().hex(), 16)
        c = pow(m, self.e, self.n)

        return hex(c)

    def test_encryption(self):
        plaintext = input('Plaintext: ').strip()

        m = int(plaintext, 16)
        cs = []

        while m:
            c = pow(m, self.e, self.n)
            cs.append(c)
            m //= self.n

        if len(cs) > 1:
            return 'Too many messages!'

        return 'Thanks for the message!'


def main():
    yalm = YALM()

    while True:
        print(MENU)

        option = int(input('Option: '))

        if option == 1:
            print(f'Ciphertext: {yalm.get_secret()}')
        elif option == 2:
            print(yalm.test_encryption())
        else:
            break


if __name__ == '__main__':
    main()
