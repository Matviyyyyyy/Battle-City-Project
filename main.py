from pygame import *

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

while running:
    # обробка подій
    for e in event.get():
        if e.type == QUIT:
            run = False


    display.update()
    clock.tick(60)




