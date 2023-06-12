from Crypto.Util.number import long_to_bytes, GCD
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import hashlib
import random
import socketserver
import signal
from secret import FLAG

LOGO = ("""
╭━━━┳╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╭╮
┃╭━╮┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱┃┃
┃┃╱┃┃╰━┳━┳━━┳━━┳━┳╮╱╭┳━┻╮╭╋━━┫╰━┳━┳━━╮
┃╰━╯┃╭╮┃╭┫╭╮┃╭━┫╭┫┃╱┃┃╭╮┃┃┃╭╮┃╭╮┃╭┫╭╮┃
┃╭━╮┃╰╯┃┃┃╭╮┃╰━┫┃┃╰━╯┃╰╯┃╰┫╭╮┃╰╯┃┃┃╭╮┃
╰╯╱╰┻━━┻╯╰╯╰┻━━┻╯╰━╮╭┫╭━┻━┻╯╰┻━━┻╯╰╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╰╯\n""")


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


def bytes_to_bits(input):
    return ''.join(format(i, '08b') for i in input)


class DisruptionSpell(object):

    def __init__(self, n):
        self.n = n

    def spawnScroll(self):
        intList = []
        intList.append(random.randint(1, self.n))
        sum = intList[0]

        for i in range(1, self.n):
            intList.append(random.randint(sum + 1, (sum + i) * 2))
            sum = sum + intList[i]

        x1 = random.randint(sum + 1, sum * 2)

        while True:
            x2 = random.randint(1, x1)
            if GCD(x2, x1) == 1:
                break

        scrollOfWorthiness = []

        for i in range(self.n):
            scrollOfWorthiness.append(x2 * intList[i] % x1)

        return scrollOfWorthiness

    def disrupt(self, scrollOfWorthiness, flag_bits):
        disruptedFlag = 0

        for i in range(len(flag_bits)):
            if int(flag_bits[i]) != 0: disruptedFlag += scrollOfWorthiness[i]

        return long_to_bytes(disruptedFlag).hex()


class Wizard:

    def __init__(self):
        self.magicka = 108314726549199134030277012155370097074
        self.armor = 31157724864730593494380966212158801467
        self.stamina = 32
        self.critChance = random.randint(1337, self.magicka - 1)
        self.spell = random.randint(1337, self.magicka - 1)

    def attack(self):
        self.spell = (self.armor * self.spell + self.critChance) % self.magicka
        spellAttack = self.spell >> (self.magicka.bit_length() - self.stamina)
        return spellAttack

    def dontAcceptDefeat(self, playerHealth, flag):
        flag = flag.lstrip('HTB{').rstrip('}')
        flag_bits = bytes_to_bits(flag.encode())

        distruptionSpell = DisruptionSpell(len(flag_bits))
        scrollOfWorthiness = distruptionSpell.spawnScroll()
        disruptedFlag = distruptionSpell.disrupt(scrollOfWorthiness, flag_bits)

        for _ in range(playerHealth):
            self.spell = (self.armor * self.spell +
                          self.critChance) % self.magicka

        finalSpellIngredient = str(self.spell >> (self.magicka.bit_length() -
                                                  self.stamina)).encode()
        finalSpellIngredient = hashlib.md5(finalSpellIngredient).digest()
        finalSpell = AES.new(finalSpellIngredient, AES.MODE_CBC)
        disruptedFlag = finalSpell.encrypt(
            pad("You're a wizard Harry, ".encode() + disruptedFlag.encode(),
                AES.block_size)).hex()

        return disruptedFlag, scrollOfWorthiness


def main(s):
    encryptionWizard = Wizard()
    playerHealth = 100
    wizardHealth = 200

    try:
        sendMessage(s, LOGO)
        sendMessage(s, " * The Basilisk is approaching... *\n")
        sendMessage(s, " - You think you're a wizard?")

        while playerHealth > 0 and wizardHealth > 0:
            block = receiveMessage(s, "\n > ")
            spellAttack = encryptionWizard.attack()
            if int(block) != spellAttack:
                playerHealth -= 1
                sendMessage(s, " - This is too easy...\n")
                sendMessage(s, str(spellAttack))
            else:
                wizardHealth -= 1
                sendMessage(s, " - You won't be so lucky next time!\n")

        if playerHealth <= 0:
            sendMessage(s, " - You can't even save your self!\n")
            s.close()
        else:
            disruptedFlag, scrollOfWorthiness = encryptionWizard.dontAcceptDefeat(
                playerHealth, FLAG)
            scrollOfWorthinessSize = len(scrollOfWorthiness)

            sendMessage(s, f"\n {str(scrollOfWorthinessSize)}\n")

            for i in scrollOfWorthiness:
                sendMessage(s, f"{str(i)}\n")

            sendMessage(s, f"{disruptedFlag}\n")

            s.close()

    except:
        try:
            sendMessage(s, "Unexpected error occured.\n")
            s.close()
        except:
            pass
        exit()


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
