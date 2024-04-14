from pygame import *
from classes.tank_hero import Tank
from classes.brick_wall import BrickWall
from classes.iron_wall import IronWall
from classes.bush import Bush
from classes.bullet import Bullet
from classes.map_renderer import MapRenderer
from classes.enemy import Enemy



def game(level, settings):  

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


    # створення героя
    if settings.tank1 == 1:
        tank_hero = Tank(150, 100, 'images/tank_hero.png', 2, 50, 50, 0, 10, 1)
    
    if settings.num_players == 2:
        if settings.tank2 == 1:
            tank_hero2 = Tank(250, 100, 'images/tank_hero.png', 2, 50, 50, 0, 10, 1)


    enemy_tank = Enemy(200, 400, "images/enemy.gif", 3, 50, 50, 270)
    if level == 1:
        map_renderer = MapRenderer("files_template/map1.txt", 50)
    elif level == 2:
        map_renderer = MapRenderer("files_template/map2.txt", 50)
    map_renderer.draw_map()

    # створення заднього фону
    background = transform.scale(image.load("images/background.jfif"), (600, 600))


    running = True
    while running:

        keys = key.get_pressed()  # створення можливості взаємодіяти

        # обробка подій
        for e in event.get():  # оформлення виходу з гри
            if e.type == QUIT:
                run = False
                
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if tank_hero.angle == 315:
                        tank_hero.bullets.append(Bullet(tank_hero.rect.x, tank_hero.rect.y, "images/bullet.webp", 7, 15, 15, 45))
                    elif tank_hero.angle == 270:
                        tank_hero.bullets.append(Bullet(tank_hero.rect.x, tank_hero.rect.y, "images/bullet.webp", 7, 15, 15, 0))
                    else: 
                        tank_hero.bullets.append(Bullet(tank_hero.rect.x, tank_hero.rect.y, "images/bullet.webp", 7, 15, 15, tank_hero.angle + 90))
                if e.key == K_RSHIFT and settings.num_players == 2:
                    if tank_hero2.angle == 315:
                        tank_hero2.bullets.append(Bullet(tank_hero2.rect.x, tank_hero2.rect.y, "images/bullet.webp", 7, 15, 15, 45))
                    elif tank_hero2.angle == 270:
                        tank_hero2.bullets.append(Bullet(tank_hero2.rect.x, tank_hero2.rect.y, "images/bullet.webp", 7, 15, 15, 0))
                    else: 
                        tank_hero2.bullets.append(Bullet(tank_hero2.rect.x, tank_hero2.rect.y, "images/bullet.webp", 7, 15, 15, tank_hero2.angle + 90))
                        
        keys_tank1 = key.get_pressed()
        tank_hero.update(keys_tank1) # Оновлення руху першого танка

        if settings.num_players == 2:
            keys_tank2 = key.get_pressed()
            tank_hero2.update(keys_tank2) # Оновлення руху другого танка

        enemy_tank.update()
                

        # подія зіткнення зі стінами
        for block in map_renderer.blocks:
            if tank_hero.rect.colliderect(block.rect) and not isinstance(block, Bush):
                if keys[K_a]:
                    if tank_hero.rect.left > block.rect.left:  # Перевіряємо, чи герой не зіткнеться зліва
                        tank_hero.rect.left = block.rect.right  # Зміщуємо героя праворуч від стінки
                        tank_hero.speed = 0  # Зупиняємо рух героя

                if keys[K_d]:
                    if tank_hero.rect.right < block.rect.right:  # Перевіряємо, чи герой не зіткнеться справа
                        tank_hero.rect.right = block.rect.left  # Зміщуємо героя ліворуч від стінки
                        tank_hero.speed = 0  # Зупиняємо рух героя

                if keys[K_w]:
                    if tank_hero.rect.top > block.rect.top:  # Перевіряємо, чи герой не зіткнеться зверху
                        tank_hero.rect.top = block.rect.bottom  # Зміщуємо героя вниз від стінки
                        tank_hero.speed = 0  # Зупиняємо рух героя

                if keys[K_s]:
                    if tank_hero.rect.bottom < block.rect.bottom:  # Перевіряємо, чи герой не зіткнеться знизу
                        tank_hero.rect.bottom = block.rect.top  # Зміщуємо героя вверх від стінки
                        tank_hero.speed = 0  # Зупиняємо рух героя
            else:
                tank_hero.speed = 2  # Якщо немає зіткнення, продовжуємо рух з нормальною швидкістю

            for bullet in tank_hero.bullets:
                    if bullet.rect.colliderect(block.rect) and not isinstance(block, Bush):
                        if isinstance(block, BrickWall):
                            block.hit()
                            tank_hero.dest(bullet)

                        if isinstance(block, IronWall):
                            tank_hero.dest(bullet)

            if settings.num_players == 2:
                if tank_hero2.rect.colliderect(block.rect) and not isinstance(block, Bush):
                    if keys[K_LEFT]:
                        if tank_hero2.rect.left > block.rect.left:
                            tank_hero2.rect.left = block.rect.right
                            tank_hero2.speed = 0

                    if keys[K_RIGHT]:
                        if tank_hero2.rect.right < block.rect.right:
                            tank_hero2.rect.right = block.rect.left
                            tank_hero2.speed = 0

                    if keys[K_UP]:
                        if tank_hero2.rect.top > block.rect.top:
                            tank_hero2.rect.top = block.rect.bottom
                            tank_hero2.speed = 0

                    if keys[K_DOWN]:
                        if tank_hero2.rect.bottom < block.rect.bottom:
                            tank_hero2.rect.bottom = block.rect.top
                            tank_hero2.speed = 0
                else:
                    tank_hero2.speed = 2  # Якщо немає зіткнення, продовжуємо рух з нормальною швидкістю
            
                for bullet in tank_hero2.bullets:
                    if bullet.rect.colliderect(block.rect) and not isinstance(block, Bush):
                        if isinstance(block, BrickWall):
                            block.hit()
                            tank_hero2.dest(bullet)
                    
                        if isinstance(block, IronWall):
                            tank_hero2.dest(bullet)

        
            if isinstance(block, BrickWall):
                map_renderer.destruction(block)

            if enemy_tank.rect.x - 400 < tank_hero.rect.x < enemy_tank.rect.x + 400 and enemy_tank.rect.y - 50 < tank_hero.rect.y < enemy_tank.rect.y + 50 and block.x or enemy_tank.rect.x - 50 < tank_hero.rect.x < enemy_tank.rect.x + 50 and enemy_tank.rect.y - 400 < tank_hero.rect.y < enemy_tank.rect.y + 400:
                enemy_tank.angle = 180


        # Перевіряємо, чи виходить танк за межі поля
        if tank_hero.rect.left < 0:
            tank_hero.rect.left = 0
            tank_hero.speed = 0
        if tank_hero.rect.right > 600:
            tank_hero.rect.right = 600
            tank_hero.speed = 0
        if tank_hero.rect.top < 0:
            tank_hero.rect.top = 0
            tank_hero.speed = 0
        if tank_hero.rect.bottom > 600:
            tank_hero.rect.bottom = 600
            tank_hero.speed = 0
        if tank_hero.armor <= 0:
            pass
        if settings.num_players == 2:            
            if tank_hero.rect.left < 0:
                tank_hero.rect.left = 0
                tank_hero.speed = 0
            if tank_hero.rect.right > 600:
                tank_hero.rect.right = 600
                tank_hero.speed = 0
            if tank_hero.rect.top < 0:
                tank_hero.rect.top = 0
                tank_hero.speed = 0
            if tank_hero.rect.bottom > 600:
                tank_hero.rect.bottom = 600
                tank_hero.speed = 0
            if tank_hero.armor <= 0:
                pass
        # промальовка об'єктів
        screen.blit(background, (0, 0))  # задній фон
        enemy_tank.draw(screen)
        tank_hero.draw(screen)  # танк
        if settings.num_players == 2:
            tank_hero2.draw(screen)
        for block in map_renderer.blocks:  # стіни
            block.draw(screen)
        for bullet in tank_hero.bullets:
            bullet.update()
        if settings.num_players == 2:
            for bullet in tank_hero2.bullets:
                bullet.update()
        display.update()  # оновлення екрану
        clock.tick(60)  # фпс


