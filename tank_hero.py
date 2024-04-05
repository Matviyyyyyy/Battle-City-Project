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

    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed