from pygame import *
from tank_hero import Tank

init()
screen = display.set_mode((600, 600))
display.set_caption("Battle City")
clock = time.Clock()

def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                run = False
        display.update()
        clock.tick(60)

running = True

tank_hero = Tank(100, 100, 'tank_hero.png', 10, 50, 50)

background = transform.scale(image.load("background.jfif"), (600, 600))

while running:
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            run = False

    tank_hero.update()

    screen.blit(background, (0, 0))
    tank_hero.draw(screen)
    display.update()
    clock.tick(60)




