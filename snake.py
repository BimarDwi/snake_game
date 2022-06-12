import keyboard


class Snake:
    body_before = [
        [2, 4], [2, 3], [2, 2]
    ]

    body_after = [

    ]

    head_before = [2, 5]  # [vertical, horizontal]

    head_after = []

    speed = [0, 1]  # [v_speed, h_speed]

    def __init__(self, new_body=None):

        if new_body is not None:
            self.body_before.append(new_body)

    def direction(self):
        w = keyboard.is_pressed("w")
        a = keyboard.is_pressed("a")
        s = keyboard.is_pressed("s")
        d = keyboard.is_pressed("d")
        if w is True and self.speed[0] == 0:
            self.speed = [-1, 0]
        elif s is True and self.speed[0] == 0:
            self.speed = [1, 0]
        elif d is True and self.speed[1] == 0:
            self.speed = [0, 1]
        elif a is True and self.speed[1] == 0:
            self.speed = [0, -1]
        else:
            pass

    def move(self):
        self.head_after = [self.head_before[0] + self.speed[0], self.head_before[1] + self.speed[1]]
        self.body_after.append(self.head_before)
        self.head_before = self.head_after

        for body in self.body_before:
            self.body_after.append(body)

        self.body_after.pop()
        self.body_before = self.body_after
        self.body_after = []
