class Tank:
    def __init__(self, start_x, start_y, filename, speed):
        self.start_x = start_x
        self.start_y = start_y
        self.filename = filename
        self.speed = speed

    def move_up(self):
        self.start_y += self.speed

    def move_down(self):
        self.start_y -= self.speed

    def move_left(self):
        self.start_x -=self.speed

    def move_right(self):
        self.start_x +=self.speed
