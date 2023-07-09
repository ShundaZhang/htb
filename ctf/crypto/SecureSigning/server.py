from hashlib import sha256
from secret import FLAG

WELCOME_MSG = """
Welcome to my Super Secure Signing service which uses unbreakable hash function.
We combine your Cipher with our secure key to make sure that it is more secure than it should be.
"""


def menu():
    print("1 - Sign Your Message")
    print("2 - Verify Your Message")
    print("3 - Exit")


def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])


def H(m):
    return sha256(m).digest()


def main():
    print(WELCOME_MSG)

    while True:
        try:
            menu()
            choice = int(input("> "))
        except:
            print("Try again.")
            continue

        if choice == 1:
            message = input("Enter your message: ").encode()
            hsh = H(xor(message, FLAG))
            print(f"Hash: {hsh.hex()}")
        elif choice == 2:
            message = input("Enter your message: ").encode()
            hsh = input("Enter your hash: ")
            if H(xor(message, FLAG)).hex() == hsh:
                print("[+] Signature Validated!\n")
            else:
                print(f"[!] Invalid Signature!\n")
        else:
            print("Good Bye")
            exit(0)


if __name__ == "__main__":
    main()