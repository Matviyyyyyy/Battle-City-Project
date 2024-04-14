from classes.button import Button

class LevelButton(Button):
    def __init__(self, text, font, font_size, color, bg_color, surface, x, y, width, height, is_draw, is_openly):
        super().__init__( text, font, font_size, color, bg_color, surface, x, y, width, height, is_draw)
        self.is_openly = is_openly

    def open(self):
        self.is_openly = True
    