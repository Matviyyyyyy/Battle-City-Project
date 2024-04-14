import pygame

class Text:
    def __init__(self, text, font, font_size, color, surface, x, y, is_draw):
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.color = color
        self.surface = surface
        self.x = x
        self.y = y
        self.is_draw = is_draw
    
    def draw_text(self):
        textobj = self.font.render(self.text, 1, self.color)
        textrect = textobj.get_rect()
        textrect.topleft = (self.x, self.y)
        self.surface.blit(textobj, textrect)

