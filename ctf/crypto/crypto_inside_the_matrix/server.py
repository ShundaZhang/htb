from sage.all_cmdline import *
# from utils import ascii_print
import os
from secret import FLAG

assert len(FLAG) == 25


class Book:

    def __init__(self):
        self.size = 5
        self.prime = None

    def parse(self, pt: bytes):
        pt = [b for b in pt]
        return matrix(GF(self.prime), self.size, self.size, pt)

    def generate(self):
        key = os.urandom(self.size**2)
        return self.parse(key)

    def rotate(self):
        self.prime = random_prime(2**6, False, 2**4)

    def encrypt(self, message: bytes):
        self.rotate()
        key = self.generate()
        message = self.parse(message)
        ciphertext = message * key
        return ciphertext, key


def menu():
    print("Options:\n")
    print("[L]ook at page")
    print("[T]urn page")
    print("[C]heat\n")
    option = input("> ")
    return option


def main():
    book = Book()
    ciphertext, key = book.encrypt(FLAG)
    page_number = 1

    while True:
        option = menu()
        if option == "L":
            # ascii_print(ciphertext, key, page_number)
            print(ciphertext, key, page_number)
        elif option == "T":
            ciphertext, key = book.encrypt(FLAG)
            page_number += 2
            print()
        elif option == "C":
            print(f"\n{list(ciphertext)}\n{list(key)}\n")
        else:
            print("\nInvalid option!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
