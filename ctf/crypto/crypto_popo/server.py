from secret import FLAG
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime, GCD
from random import randint
from math import lcm

class POPO:
    def __init__(self, m):
        self.m = m
        self.p = getPrime(1024)
        self.q = getPrime(1024)
        self.n = self.p * self.q
        self.phi = (self.p-1) * (self.q-1)
        self.l = lcm(self.p-1, self.q-1)
        self.n2 = self.n * self.n
        self.g = self.n + 1
        self.gm = pow(self.g, self.m, self.n2)
        self.optim = 0

        while GCD(self.g, self.n) != 1:
            self.g = randint(self.n, self.n2)

        while (pow(self.g, self.l, self.n2) - 1 // self.n) == 1:
            self.g = randint(self.n, self.n2)

        self.r = randint(self.n, self.n2)

    def anonymize(self, m, r=0):
        if m > 0 and m != self.m and m > 0:
            if self.optim == 0:
                local = pow(self.g, m, self.n2)
            else:
                local = m
        else:
            local = self.gm

        if self.optim == 0:
            self.optim = 1

        if r == 0:
            r = self.r
        
        b = pow(r, self.n, self.n2)
        c = local * b % (self.n2)
        return {'c' : c, 'n' : self.n}


    def reset_optim(self):
        self.optim = 0

    def test_standard_encryption(self, m1, m2):
        r1 = randint(0, self.n)
        r2 = randint(0, self.n)
        c1 = self.encrypt(m1, r=r1)["c"]
        self.reset_optim()
        c2 = self.encrypt(m2, r=r2)["c"]
        self.reset_optim()
        return {'additive_he' : (c1*c2) % (self.n2), 'res' : (c1*c2) % (self.n2) == self.encrypt(m1 + m2, r1*r2)['c']}

    def validate_role(self, gm):
        if gm == self.gm:
            return {'λ' : self.l}
        else:
            return {"Error": "not enough knowledge provided"}


def menu():
    print("\nPOPO - v.1.0.0. Choose your action:\n")
    print("1. Encrypt")
    print("2. Knowledge proof")
    print("3. Test homomorphic encryption")
    print("4. Reset optimization")

    option = input("\n> ")
    return option

def main():
    popo = POPO(bytes_to_long(FLAG))

    while True:
        choice = int(menu())
        try:
            if choice == 1:
                menu_m = input("\nProvide a message: ").strip()
                print(popo.anonymize(int(menu_m)))
            elif choice == 2:
                menu_gm = input("\nProvide gm: ").strip().encode()
                print(popo.validate_role(int(menu_gm)))
            elif choice == 3:
                menu_multiple_m = input("\nProvide two messages formatted as m1,m2 : ").strip().encode().split(b',')
                print(popo.test_standard_encryption(bytes_to_long(menu_multiple_m[0]), bytes_to_long(menu_multiple_m[1])))
            elif choice == 4:
                popo.reset_optim()
            else:
                print('Nothing to see here.')
                exit(1)
        except Exception as e:
            print("Error during execution")



if __name__ == "__main__":
    main()
