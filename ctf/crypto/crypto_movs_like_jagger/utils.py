import random

locations = [
    'the Galactic Federation\'s head courters',
    'Urkir',
    'Rohendel',
    'Longhir',
    'Vinyr',
    'the Dying Sun',
    'Thoccarth',
    'the Glowing Sea'
]


def generateLocation(success: bool) -> list:
    if success:
        return 'secret location of the weapons'
    else:
        return random.choice(locations)
