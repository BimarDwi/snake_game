import keyboard


class Snake:
    body_before = [
        [2, 14], [2, 15]
    ]

    body_after = [

    ]

    head_before = [2, 15]  # [vertical, horizontal]

    head_after = []

    speed = [0, 1]  # [v_speed, h_speed]

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

        if self.head_before[0] == 0:
            self.head_after = [25, self.head_before[1]]
            self.body_after.append(self.head_before)
            self.head_before = self.head_after

            for body in self.body_before:
                self.body_after.append(body)

            self.body_after.pop()
            self.body_before = self.body_after
            self.body_after = []

        elif self.head_before[0] == 26:
            self.head_after = [1, self.head_before[1]]
            self.body_after.append(self.head_before)
            self.head_before = self.head_after

            for body in self.body_before:
                self.body_after.append(body)

            self.body_after.pop()
            self.body_before = self.body_after
            self.body_after = []

        elif self.head_before[1] == 0:
            self.head_after = [self.head_before[0], 25]
            self.body_after.append(self.head_before)
            self.head_before = self.head_after

            for body in self.body_before:
                self.body_after.append(body)

            self.body_after.pop()
            self.body_before = self.body_after
            self.body_after = []

        elif self.head_before[1] == 26:
            self.head_after = [self.head_before[0], 1]
            self.body_after.append(self.head_before)
            self.head_before = self.head_after

            for body in self.body_before:
                self.body_after.append(body)

            self.body_after.pop()
            self.body_before = self.body_after
            self.body_after = []

    def add_length(self):
        vector_vertical = self.body_before[-1][0] - self.body_before[-2][0]
        vector_horizontal = self.body_before[-1][1] - self.body_before[-2][1]
        vector = [vector_vertical, vector_horizontal]
        self.body_before.append([self.body_before[-1][0] + vector[0], self.body_before[-1][1] + vector[1]])
