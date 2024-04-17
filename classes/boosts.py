from pygame import *

class Boost:
    def __init__(self, x, y, filename, width, height):
        self.x = x
        self.y = y
        self.filename = filename
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
