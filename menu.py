from pygame import *
import sys
from classes.text import Text
from classes.button import Button
from classes.levelbutton import LevelButton
from classes.image import Image
from classes.settings import Settings
import main


init()
screen = display.set_mode((800, 600))
display.set_caption("Battle City")
clock = time.Clock()
font_tnw = 'Fonts/timesbd.ttf'
font_b = 'Fonts/BROADW.TTF'
mb = transform.scale(image.load("images/menu_background.png"), (800, 600))
menu_text = Text('Menu:', font_tnw, 36, (255, 255, 255), screen, 350, 100, True)
play_button = Button('Play', font_tnw, 36, (150, 150, 150), (20, 100, 20),  screen, 320, 300, 180, 80, True)
game_text = Text('Game:', font_tnw, 36, (255, 255, 255), screen, 350, 20, True)
settings_button = Button('Settings', font_tnw, 36, (150, 150, 150), (50, 50, 50),  screen, 320, 180, 180, 80, True)
b_c_text = Text('Battle City', font_b, 48, (255, 255, 255), screen, 270, 20, True)
num_players_text = Text('Choose the number of players', font_tnw, 36, (255, 255, 255), screen, 200, 180, False)
settings_text = Text('Settings:', font_tnw, 36, (255, 255, 255), screen, 340, 100, False)
player_num1_button = Button('1', font_tnw, 36, (150, 150, 150), (50, 50, 50),  screen, 280, 250, 80, 80, False)
player_num2_button = Button('2', font_tnw, 36, (150, 150, 150), (50, 50, 50),  screen, 450, 250, 80, 80, False)
exit_button = Button('Exit', font_tnw, 36, (180, 180, 180), (40, 20, 10),  screen, 320, 420, 180, 80, True)
select_tank_button = Button('Choose a tank', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 300, 380, 220, 80, False)
back_button1 = Button('Back', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 300, 500, 220, 80, False)
select_level_text = Text("Choose a level", font_tnw, 36, (255, 255, 255), screen, 300, 100, False)
level1_button = LevelButton('level 1', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 60, 160, 220, 80, False, True)
level2_button = LevelButton('level 2', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 60, 320, 220, 80, False, False)
level3_button = LevelButton('level 3', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 520, 160, 220, 80, False, False)
select_tank_text = Text('Choose a tank', font_tnw, 36, (255, 255, 255), screen, 300, 100, False)
back_button2 = Button('Back', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 300, 500, 220, 80, False)
back_button3 = Button('Back', font_tnw, 36, (150, 150, 150),  (50, 50, 50), screen, 300, 500, 220, 80, False)
image_tank1 = Image("images/tank_hero.png", 50, 160, 80, 80, False)
description1 = Text('Speed: 2, Number of shells: 10, armor: 1.', font_tnw, 24, (255, 255, 255), screen, 160, 170, False)
tank1_button1 = LevelButton("", None, 10, (150, 150, 150),  (50, 50, 50), screen, 600, 150, 80, 80, False, True)
tank1_button2 = LevelButton("", None, 10, (150, 150, 150),  (50, 50, 50), screen, 700, 150, 80, 80, False, True)
settings = Settings(1, 1, 1)
def changes(*args):
    for obj in args:
        obj.is_draw = not obj.is_draw

def main_menu():
    while True:
        screen.blit(mb, (0, 0))
        if menu_text.is_draw == True:
            menu_text.draw_text()
        if b_c_text.is_draw == True:
            b_c_text.draw_text()
        if num_players_text.is_draw == True:
            num_players_text.draw_text()
        if settings_text.is_draw == True:
            settings_text.draw_text()
        if select_level_text.is_draw == True:
            select_level_text.draw_text()
        if select_tank_text.is_draw == True:
            select_tank_text.draw_text()
        if image_tank1.is_draw == True:
            image_tank1.draw(screen)
        if description1.is_draw == True:
            description1.draw_text()
        
        mouse_pos = mouse.get_pos()
        if mouse_pos[0] > play_button.x and mouse_pos[0] < play_button.x + play_button.width and mouse_pos[1] > play_button.y and mouse_pos[1] < play_button.y + play_button.height:
            play_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            play_button.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > settings_button.x and mouse_pos[0] < settings_button.x + settings_button.width and mouse_pos[1] > settings_button.y and mouse_pos[1] < settings_button.y + settings_button.height:
            settings_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            settings_button.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > exit_button.x and mouse_pos[0] < exit_button.x + exit_button.width and mouse_pos[1] > exit_button.y and mouse_pos[1] < exit_button.y + exit_button.height:
            exit_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            exit_button.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > select_tank_button.x and mouse_pos[0] < select_tank_button.x + select_tank_button.width and mouse_pos[1] > select_tank_button.y and mouse_pos[1] < select_tank_button.y + select_tank_button.height:
            select_tank_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            select_tank_button.change_color((50, 50, 50), (150, 150, 150))
        
        if mouse_pos[0] > back_button1.x and mouse_pos[0] < back_button1.x + back_button1.width and mouse_pos[1] > back_button1.y and mouse_pos[1] < back_button1.y + back_button1.height:
            back_button1.change_color((180, 180, 180), (255, 255, 255))
        else:
            back_button1.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > back_button2.x and mouse_pos[0] < back_button2.x + back_button2.width and mouse_pos[1] > back_button2.y and mouse_pos[1] < back_button2.y + back_button2.height:
            back_button2.change_color((180, 180, 180), (255, 255, 255))
        else:
            back_button2.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > back_button3.x and mouse_pos[0] < back_button3.x + back_button3.width and mouse_pos[1] > back_button3.y and mouse_pos[1] < back_button3.y + back_button3.height:
            back_button3.change_color((180, 180, 180), (255, 255, 255))
        else:
            back_button3.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > level1_button.x and mouse_pos[0] < level1_button.x + level1_button.width and mouse_pos[1] > level1_button.y and mouse_pos[1] < level1_button.y + level1_button.height and level1_button.is_openly is True:
            level1_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            level1_button.change_color((50, 50, 50), (150, 150, 150))

        if mouse_pos[0] > level2_button.x and mouse_pos[0] < level2_button.x + level2_button.width and mouse_pos[1] > level2_button.y and mouse_pos[1] < level2_button.y + level2_button.height and level2_button.is_openly is True:
            level2_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            level2_button.change_color((50, 50, 50), (150, 150, 150))
        
        if mouse_pos[0] > level3_button.x and mouse_pos[0] < level3_button.x + level3_button.width and mouse_pos[1] > level3_button.y and mouse_pos[1] < level3_button.y + level3_button.height and level3_button.is_openly is True:
            level3_button.change_color((180, 180, 180), (255, 255, 255))
        else:
            level3_button.change_color((50, 50, 50), (150, 150, 150))

        if settings.num_players == 1:
            player_num1_button.change_color((180, 180, 180), (255, 255, 255))
            player_num2_button.change_color((50, 50, 50), (150, 150, 150))
        elif settings.num_players == 2:
            player_num2_button.change_color((180, 180, 180), (255, 255, 255))
            player_num1_button.change_color((50, 50, 50), (150, 150, 150))

        if settings.tank1 == 1:
            tank1_button1.change_color((0, 180, 0), (255, 255, 255))
        elif tank1_button1.is_openly is True:
            tank1_button1.change_color((180, 180, 180), (255, 255, 255))
        else:
            tank1_button1.change_color((50, 50, 50), (255, 255, 255))
        
        if settings.tank2 == 1:
            tank1_button2.change_color((0, 180, 0), (255, 255, 255))
        elif tank1_button2.is_openly is True:
            tank1_button2.change_color((180, 180, 180), (255, 255, 255))
        else:
            tank1_button2.change_color((50, 50, 50), (255, 255, 255))


        if play_button.is_draw == True:
            play_button.draw()
            if play_button.clicked == True:
                changes(menu_text, settings_button, play_button, exit_button, select_level_text, level1_button, level2_button, level3_button, back_button3)
        if level1_button.is_draw == True:
            level1_button.draw()
            if level1_button.clicked == True and level1_button.is_openly is True:
                main.game(1, settings)
        if level2_button.is_draw == True:
            level2_button.draw()
            if level2_button.clicked == True and level2_button.is_openly is True:
                main.game(2, settings)
        if level3_button.is_draw == True:
            level3_button.draw()
            if level3_button.clicked == True and level3_button.is_openly is True:
                main.game(3, settings)
        if tank1_button1.is_draw is True:
            tank1_button1.draw()
            if tank1_button1.clicked == True and tank1_button1.is_openly is True:
                settings.tank1 = 1
        if tank1_button2.is_draw is True:
            tank1_button2.draw()
            if tank1_button2.clicked == True and tank1_button2.is_openly is True:
                settings.tank2 = 1
        if settings_button.is_draw == True:
            settings_button.draw()
            if settings_button.clicked == True:
                changes(menu_text, settings_button, play_button, num_players_text, settings_text, player_num1_button, player_num2_button, exit_button, select_tank_button, back_button1)
        if player_num1_button.is_draw == True:
            player_num1_button.draw()
            if player_num1_button.clicked == True:
                settings.num_players = 1 if settings.num_players == 2 else 1
        if player_num2_button.is_draw == True:
            player_num2_button.draw()
            if player_num2_button.clicked == True:
                settings.num_players = 2 if settings.num_players == 1 else 2
        if select_tank_button.is_draw == True:
            select_tank_button.draw()
            if select_tank_button.clicked == True:
                changes(num_players_text, settings_text, player_num1_button, player_num2_button, select_tank_button, back_button1, select_tank_text, back_button2, image_tank1, description1, tank1_button1, tank1_button2)
        if back_button1.is_draw == True:
            back_button1.draw()
            if back_button1.clicked == True:
                changes(menu_text, settings_button, play_button, num_players_text, settings_text, player_num1_button, player_num2_button, exit_button, select_tank_button, back_button1)
        if back_button2.is_draw == True:
            back_button2.draw()
            if back_button2.clicked == True:
                changes(num_players_text, settings_text, player_num1_button, player_num2_button, select_tank_button, back_button1, select_tank_text, back_button2, image_tank1, description1, tank1_button1, tank1_button2)
        if back_button3.is_draw == True:
            back_button3.draw()
            if back_button3.clicked == True:
                changes(menu_text, settings_button, play_button, exit_button, select_level_text, level1_button, level2_button, level3_button, back_button3)
        if exit_button.is_draw == True:
            exit_button.draw()
            if exit_button.clicked == True:
                quit()  
                sys.exit()
        
        
        for e in event.get():
            if e.type == QUIT:
                quit()
                sys.exit()
            play_button.handle_event(e)
            settings_button.handle_event(e)
            player_num1_button.handle_event(e)
            player_num2_button.handle_event(e)
            exit_button.handle_event(e)
            select_tank_button.handle_event(e)
            back_button1.handle_event(e)
            level1_button.handle_event(e)
            level2_button.handle_event(e)
            level3_button.handle_event(e)
            back_button2.handle_event(e)
            back_button3.handle_event(e)
            tank1_button1.handle_event(e)
            tank1_button2.handle_event(e)

        display.update()

main_menu()