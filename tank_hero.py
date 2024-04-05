from pygame import *

class Tank:
    def __init__(self, x, y, filename, speed, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.filename = filename
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move_up(self):
        self.y += self.speed

    def move_down(self):
        self.y -= self.speed

    def move_left(self):
        self.x -=self.speed

    def move_right(self):
        self.x +=self.speed
