from secret import FLAG, p, a, b
from random import randint
from utils import EllipticCurve

class PRNG:

    def __init__(self, p, mul1, mul2):
        self.mod = p * 6089788258325039501929073418355467714844813056959443481824909430411674443639248386564763122373451773381582660411059922334086996696436657009055324008041039
        self.exp = 2
        self.mul1 = mul1
        self.mul2 = mul2
        self.inc = int.from_bytes(b'Coordinates lost in space', 'big')
        self.seed = randint(2, self.mod - 1)

    def rotate(self):
        self.seed = (self.mul1 * pow(self.seed, 3) + self.mul2 * self.seed +
                     self.inc) % self.mod
        return self.seed, pow(self.seed, self.exp, self.mod)


class Relic:

    def __init__(self, p, a, b):
        self.E = EllipticCurve(p, a, b)
        self.P = None
        self.EP = None
        self.p = p
        self.prng = PRNG(p, a, b)

    def setupPoints(self, x):
        if x >= self.p:
            return 'Coordinate greater than curve modulus'

        try:
            self.P = self.E.get_point(x)
            self.EP = self.P
        except:
            return 'Point not on curve'

        return ('Point confirmed on curve', self.P.x, self.P.y)

    def nextPoints(self):
        seed, enc_seed = self.prng.rotate()
        self.P *= seed
        self.EP *= enc_seed
        return ('New Points', self.EP.x, self.EP.y, self.P.x, self.P.y)


def menu():
    print('Options:\n')
    print('1. Setup Point')
    print('2. Receive new point')
    print('3. Find true point')
    option = input('> ')
    return option


def main():
    artifact = Relic(p, a, b)
    setup = False

    while True:
        try:
            option = menu()
            if option == '1':
                print('Enter x coordinate.')
                x = int(input('x : '))
                response = artifact.setupPoints(x)
                if response[0] == 'Point confirmed on curve':
                    setup = True
                print(response)
            elif option == '2':
                if setup:
                    response = artifact.nextPoints()
                    print('Response')
                    print((response[0], response[1], response[2]))
                else:
                    print('Configure origin point first')
            elif option == '3':
                if setup:
                    print('Input x,y')
                    Px = int(input('x: '))
                    Py = int(input('y: '))
                    response = artifact.nextPoints()
                    if Px == response[3] and Py == response[4]:
                        print(
                            'You have confirmed the location. However, It\'s dangerous to go alone. Take this: ',
                            FLAG)
                    else:
                        print('The vessels will never be found...')
                    exit()
                else:
                    print('Configure origin point first')
            else:
                print("Invalid option, shutting down...")
                exit()
        except Exception as e:
            response = f'An error occured: {e}'
            print(response)
            exit()


if __name__ == '__main__':
    assert p.bit_length() == 256
    main()
