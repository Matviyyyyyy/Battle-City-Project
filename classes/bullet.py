from pygame import *

class Bullet:
    def __init__(self, x, y, filename, speed, width, height, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.filename = filename
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
    def update(self):
        if self.angle == 90:
            self.rect.y -= self.speed
        if self.angle == 180:
            self.rect.x -= self.speed
        if self.angle == 270:
            self.rect.y += self.speed
        if self.angle == 0:
            self.rect.x += self.speed
        if self.angle == 45:
            self.rect.y -= self.speed
            self.rect.x += self.speed
        if self.angle == 135:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        if self.angle == 315:
            self.rect.y += self.speed
            self.rect.x += self.speed
        if self.angle == 225:
            self.rect.x -= self.speed
            self.rect.y += self.speed



    def draw(self, window):
        rotated_bullet = transform.rotate(self.image, self.angle)
        window.blit(rotated_bullet, (self.rect.x, self.rect.y))

