# створи гру "Лабіринт"!
from pygame import *


def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    font.init()
    text = font.Font(None, 70).render(message, True, (255, 255, 255))
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                run = False

        window.blit(text, (250, 250))
        display.update()
        clock.tick(60)


class GameObject():
    def __init__(self, x, y, filename, speed, w, h):
        self.x = x
        self.y = y
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameObject):
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


class Enemy(GameObject):
    def __init__(self, x, y, filename, speed, startPos, finishPos, w, h):
        super().__init__(x, y, filename, speed, w, h)
        self.startPos = startPos
        self.finishPos = finishPos

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 500:
            self.speed = self.speed * (-1)
        if self.rect.x <= 200:
            self.speed = self.speed * (-1)


class Wall():
    def __init__(self, x, y, w, h, color):
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


init()
window = display.set_mode((700, 500))
clock = time.Clock()
gold = GameObject(0, 0, "D:\\Projects\\gamess\\Gold-Free-Download-PNG.png", 0, 100, 100)
enemy = Enemy(250, 250, "D:\\Projects\\gamess\\1477179.png", 5, 100, 500, 65, 65)
hero = Hero(630, 50, "D:\\Projects\\gamess\\Hero-No-Background.png", 5, 35, 35)
run = True
background = transform.scale(image.load("D:\\Projects\\gamess\\depositphotos_10679924-stock-photo-sand-texture.jpg"),
                             (700, 500))
walls = []
walls.append(Wall(0, 0, 10, 100, (166, 18, 18)))
walls.append(Wall(0, 0, 200, 10, (166, 18, 18)))
walls.append(Wall(600, 0, 200, 10, (166, 18, 18)))
walls.append(Wall(690, 0, 10, 100, (166, 18, 18)))
walls.append(Wall(600, 100, 100, 10, (166, 18, 18)))
walls.append(Wall(450, 0, 150, 10, (166, 18, 18)))
walls.append(Wall(450, 0, 10, 250, (166, 18, 18)))
walls.append(Wall(350, 240, 100, 10, (166, 18, 18)))
walls.append(Wall(350, 0, 10, 240, (166, 18, 18)))
walls.append(Wall(200, 0, 150, 10, (166, 18, 18)))
walls.append(Wall(600, 100, 10, 370, (166, 18, 18)))
walls.append(Wall(200, 460, 420, 10, (166, 18, 18)))
walls.append(Wall(200, 100, 10, 370, (166, 18, 18)))
walls.append(Wall(0, 100, 200, 10, (166, 18, 18)))
for wall in walls:
    if hero.rect.colliderect(wall.rect):
        showEndWindow(window, "Ти програв!")
    if hero.rect.colliderect(enemy.rect):
        showEndWindow(window, "Ти програв!")
    if hero.rect.colliderect(gold.rect):
        showEndWindow(window, "Ти виграв!")

while run:
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            run = False



    # оновлення обєктів
    hero.update()
    enemy.update()

    # тоді показати "ти переміг"
    # відмалювати
    window.blit(background, (0, 0))
    hero.draw(window)
    enemy.draw(window)
    gold.draw(window)
    for wall in walls:
        wall.draw(window)
    display.update()

    clock.tick(60)
