import socketserver
import signal
from pofwork import phash


DEBUG_MSG = "DEBUG MSG - "
WELCOME_MSG = """Virgil says:
Klaus I'm connecting the serial debugger to your memory.
Please stay still. We don't want anything wrong to happen.
Ok you should be able to see debug messages now..\n\n"""


with open('memories.txt', 'r') as f:
    MEMORIES = [m.strip() for m in f.readlines()]


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def sendMessage(s, msg):
    s.send(msg.encode())


def recieveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def main(s):
    block = ""
    counter = 0
    sendMessage(s, WELCOME_MSG)

    while True:
        block += MEMORIES[counter]

        sendMessage(s, DEBUG_MSG +
                    f"You need to validate this memory block: {block}\n")

        first_key = recieveMessage(s, DEBUG_MSG + "Enter first key: ")
        second_key = recieveMessage(s, DEBUG_MSG + "Enter second key: ")

        try:
            first_key, second_key = int(first_key), int(second_key)
            proof_of_work = phash(block, first_key, second_key)
        except:
            sendMessage(s, "\nVirgil says: \n"
                        "Be carefull Klaus!! You don't want to damage yourself.\n"
                        "Let's start over.")
            exit()

        if proof_of_work == 0:
            block += f" ({first_key}, {second_key}). "
            sendMessage(s, "\nVirgil says: \nWow you formed a new memory!!\n")
            counter += 1
            sendMessage(
                s, f"Let's try again {4 - counter} times just to be sure!\n\n")
        else:
            sendMessage(s, DEBUG_MSG + f"Incorect proof of work\n"
                        "\nVirgil says: \n"
                        "You calculated something wrong Klaus we need to start over.")
            exit()

        if counter == 4:
            sendMessage(s, "It seems that everything are working fine.\n"
                        "Wait what is that...\n"
                        "Klaus this is important!!\n"
                        "This can help you find your father!!\n"
                        f"{MEMORIES[-1]}")
            exit()


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
