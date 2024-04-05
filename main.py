from pygame import *
import time

init()
screen = display.set_mode((600, 600))
fps = time.Clock()
display.set_caption("Battle City")
def showEndWindow(window, message):
    clock = time.Clock()
    run = True
    font.init()
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                run = False
            display.update()
        clock.tick(60)

running = True

while running:




