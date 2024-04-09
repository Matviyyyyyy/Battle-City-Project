from pygame import *

class Tank:
    def __init__(self, x, y, filename, speed, width, height, angle):
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

    def draw(self, window):
        rotated_tank = transform.rotate(self.image, self.angle)
        window.blit(rotated_tank, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(window)

    def update(self, keys):
        if keys[K_a]:
            self.rect.x -= self.speed
            self.angle = 90
        if keys[K_d]:
            self.rect.x += self.speed
            self.angle = 270
        if keys[K_w]:
            self.rect.y -= self.speed
            self.angle = 0
        if keys[K_s]:
            self.rect.y += self.speed
            self.angle = 180

        for bullet in self.bullets:
            bullet.angle = self.angle + 90




