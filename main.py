from pygame import *
from classes.tank_hero import Tank
from classes.brick_wall import BrickWall

init()
screen = display.set_mode((600, 600))
display.set_caption("Battle City")
clock = time.Clock()

def showEndWindow(window):
    clock = time.Clock()
    run = True
    while run:
        # обробка подій
        for e in event.get():
            if e.type == QUIT:
                run = False
        display.update()
        clock.tick(60)


#створення героя
tank_hero  = Tank(100, 100, 'images/tank_hero.png', 3, 50, 50, 0)


#створення стін
walls = []
wall1 = BrickWall(300, 300, 'images/brick_wall_test.jpg', 50, 50)
wall2 = BrickWall(250, 300, 'images/brick_wall_test.jpg', 50, 50)
wall3 = BrickWall(200, 300, 'images/brick_wall_test.jpg', 50, 50)
wall4 = BrickWall(150, 300, 'images/brick_wall_test.jpg', 50, 50)
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)


#створення заднього фону
background = transform.scale(image.load("images/background.jfif"), (600, 600))


#ігровий цикл
running = True
while running:
    #обробка подій
    for e in event.get(): #оформлення виходу з гри
        if e.type == QUIT:
            run = False


    keys = key.get_pressed() #створення можливості взаємодіяти


    tank_hero.update(keys) #викликання методу руху танка

    #подія зіткнення зі стінами
    for wall in walls:
        if tank_hero.rect.colliderect(wall.rect):
            if keys[K_a]:
                if tank_hero.rect.left > wall.rect.left:  # Перевіряємо, чи герой не зіткнеться зліва
                    tank_hero.rect.left = wall.rect.right  # Зміщуємо героя праворуч від стінки
                    tank_hero.speed = 0  # Зупиняємо рух героя
            if keys[K_d]:
                if tank_hero.rect.right < wall.rect.right:  # Перевіряємо, чи герой не зіткнеться справа
                    tank_hero.rect.right = wall.rect.left  # Зміщуємо героя ліворуч від стінки
                    tank_hero.speed = 0  # Зупиняємо рух героя
            if keys[K_w]:
                if tank_hero.rect.top > wall.rect.top:  # Перевіряємо, чи герой не зіткнеться зверху
                    tank_hero.rect.top = wall.rect.bottom  # Зміщуємо героя вниз від стінки
                    tank_hero.speed = 0  # Зупиняємо рух героя
            if keys[K_s]:
                if tank_hero.rect.bottom < wall.rect.bottom:  # Перевіряємо, чи герой не зіткнеться знизу
                    tank_hero.rect.bottom = wall.rect.top  # Зміщуємо героя вверх від стінки
                    tank_hero.speed = 0  # Зупиняємо рух героя
        else:
            tank_hero.speed = 5  # Якщо немає зіткнення, продовжуємо рух з нормальною швидкістю

    #промальовка об'єктів
    screen.blit(background, (0, 0)) #задній фон
    tank_hero.draw(screen) #танк
    for wall in walls: #стіни
        wall.draw(screen)

    display.update() #оновлення екрану
    clock.tick(60) #фпс



