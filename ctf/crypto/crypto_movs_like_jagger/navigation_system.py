from ecdsa import ellipticcurve as ecc
from random import randint

a = -35
b = 98
p = 434252269029337012720086440207
Gx = 16378704336066569231287640165
Gy = 377857010369614774097663166640
ec_order = 434252269029337012720086440208

E = ecc.CurveFp(p, a, b)
G = ecc.Point(E, Gx, Gy, ec_order)


def generateKeyPair():
    private = randint(1, 2**64)
    public = G * private
    return(public, private)


def calculatePointsInSpace():
    Q, nQ = generateKeyPair()
    P, nP = generateKeyPair()
    return [Q, nQ, P, nP]


def checkCoordinates(data: dict) -> list:
    if data['destination_x'] == "" or data['destination_y'] == "":
        raise ValueError('Empty coordinates...')

    try:
        destination_x = int(data['destination_x'], 16)
        destination_y = int(data['destination_y'], 16)
    except:
        raise ValueError('Coordinates are not in the right format (hex)')

    return (destination_x, destination_y)


def checkDestinationPoint(data: dict, P: ecc.Point, nQ: int, E: ecc.CurveFp) -> list:
    destination_x, destination_y = checkCoordinates(data)
    destination_point = ecc.Point(E, destination_x, destination_y, ec_order)
    secret_point = P * nQ
    same_x = destination_point.x() == secret_point.x()
    same_y = destination_point.y() == secret_point.y()

    if (same_x and same_y):
        return True
    else:
        return False
