from random import randint

class Coordinate():
    x = None
    y = None

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def gen_rand_coord(self, width):
        self.x = randint(0, width)
        self.y = randint(0, width)
