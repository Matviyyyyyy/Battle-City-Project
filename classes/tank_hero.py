from pygame import *

class Tank:
    def __init__(self, x, y, filename, speed, width, height, angle, num_bullets, armor):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.filename = filename
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.num_bullets = num_bullets
        self.armor = armor
        self.bullets = []



    def draw(self, window):
        rotated_tank = transform.rotate(self.image, self.angle)
        window.blit(rotated_tank, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(window)


    def update(self, keys):
        if keys[K_a] and not keys[K_w] and not keys[K_s]:
            self.rect.x -= self.speed
            self.angle = 90
        if keys[K_d] and not keys[K_w] and not keys[K_s]:
            self.rect.x += self.speed
            self.angle = 270
        if keys[K_w] and not keys[K_a] and not keys[K_d]:
            self.rect.y -= self.speed
            self.angle = 0
        if keys[K_s] and not keys[K_a] and not keys[K_d]:
            self.rect.y += self.speed
            self.angle = 180
        if keys[K_a] and keys[K_w]:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.angle = 45
        if keys[K_a] and keys[K_s]:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.angle = 135
        if keys[K_d] and keys[K_w]:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.angle = 315
        if keys[K_d] and keys[K_s]:
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.angle = 225

    def update2(self, keys):
        if keys[K_LEFT] and not keys[K_UP] and not keys[K_DOWN]:
            self.rect.x -= self.speed
            self.angle = 90
        if keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN]:
            self.rect.x += self.speed
            self.angle = 270
        if keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT]:
            self.rect.y -= self.speed
            self.angle = 0
        if keys[K_DOWN] and not keys[K_LEFT] and not keys[K_RIGHT]:
            self.rect.y += self.speed
            self.angle = 180
        if keys[K_LEFT] and keys[K_UP]:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.angle = 45
        if keys[K_LEFT] and keys[K_DOWN]:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.angle = 135
        if keys[K_RIGHT] and keys[K_UP]:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.angle = 315
        if keys[K_RIGHT] and keys[K_DOWN]:
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.angle = 225

    
    def dest(self, bullet):
        self.bullets.remove(bullet)

        




