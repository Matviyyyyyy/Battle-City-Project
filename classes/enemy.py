from pygame import *

class Enemy():
    def __init__(self, x, y, filename, speed, width, height, angle, armor):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.filename = filename
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullets = []
        self.armor = armor

    def draw(self, window):
        rotated_enemy = transform.rotate(self.image, self.angle)
        window.blit(rotated_enemy, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(window)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 500:
            self.speed = self.speed * (-1)
            self.angle = 90
        if self.rect.x <= 200:
            self.speed = self.speed * (-1)
            self.angle = 270

    def dest(self, bullet):
        self.bullets.remove(bullet)