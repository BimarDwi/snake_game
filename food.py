from random import randint


class Food:
    position = []

    def __init__(self, position):
        self.position = position

    def new_position(self):
        self.position = [randint(1, 25), randint(1, 25)]
