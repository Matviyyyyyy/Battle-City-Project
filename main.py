from pygame import *
from tank_hero import Tank
from bush import Bush
from iron_wall import IronWall
from brick_wall import BrickWall

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

tank_hero  = Tank(100, 100, 'tank_hero.png', )

while running:
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            run = False


    display.update()
    clock.tick(60)




