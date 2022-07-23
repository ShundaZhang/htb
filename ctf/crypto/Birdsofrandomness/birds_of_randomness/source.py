from ecdsa import ellipticcurve as ecc
from Crypto.Util.number import isPrime
import os
import socketserver
import signal


FLAG = '--REDACTED--'


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


class TrainRoute:
    def __init__(self, a=None):
        self.p = 17101937747109687265202713197737423
        self.Gx = 3543321030468950376213178213609418
        self.Gy = 14807290861072031659976937040569354
        self.ec_order = 17101937747109687496599931614463506
        self.E = ecc.CurveFp(self.p, 2, 3)
        self.G = ecc.Point(self.E, self.Gx, self.Gy, self.ec_order)
        a, x = divmod(a, 30268)
        a, y = divmod(a, 30306)
        a, z = divmod(a, 30322)
        self.seed = int(x) + 1, int(y) + 1, int(z) + 1

    def rotate(self):
        x, y, z = self.seed
        x = (171 * x) % 30269
        y = (172 * y) % 30307
        z = (170 * z) % 30323
        self.seed = x, y, z

    def goToNextStation(self):
        while True:
            self.rotate()
            x, y, z = self.seed
            if(isPrime(x) and isPrime(y) and isPrime(z)):
                d = x * y * z
                new_point = d * self.G
                return int(new_point.x()), int(new_point.y())


def getTicketNumber():
    return int(os.urandom(32).hex(), 16)


def sendMessage(s, msg):
    s.send(msg.encode())


def receiveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def main(s):
    route = TrainRoute(getTicketNumber())

    station_coords = route.goToNextStation()
    sendMessage(
        s, f'The coordinates of the departing station were: {station_coords}\n')

    destination_coords = route.goToNextStation()
    sendMessage(s, 'Your lover has arrived to the destination. Hurry up!\n')

    pegions_left = 6
    sendMessage(
        s, f'Luckily you have {pegions_left} mechapegions in your pockets.\n')
    sendMessage(
        s, 'Use them to find out if your lover is at the destination you think.\n')

    while True:
        sendMessage(s, f'{pegions_left} mechapegions awaiting instructions.\n')
        x = receiveMessage(s, 'Enter the x coordinate: ')
        y = receiveMessage(s, 'Enter the y coordinate: ')
        pegions_left -= 1

        try:
            guessed_coords = ecc.Point(route.E, int(x), int(y), route.ec_order)
            guessed_coords = (int(guessed_coords.x()), int(guessed_coords.y()))
        except Exception as e:
            print(e)
            sendMessage(
                s, 'The mechapegion got lost, maybe try valid coordinates next time\n')
            exit()

        if guessed_coords == destination_coords:
            sendMessage(
                s, f'You found your lover. Here is your flag: {FLAG}\n')
            exit()

        if pegions_left:
            sendMessage(s, f'Try again, your lover is not there\n')
        else:
            sendMessage(s, 'Maybe it wasn\'t meant to be\n')
            exit()


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
