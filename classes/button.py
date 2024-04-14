import pygame

class Button:
    def __init__(self, text, font, font_size, color, bg_color, surface, x, y, width, height, is_draw):
        self.text = text
        self.font = font  
        self.font_size = font_size
        self.font = pygame.font.Font(self.font, self.font_size)
        self.color = color
        self.bg_color = bg_color
        self.surface = surface
        self.clicked = False
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_draw = is_draw
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.clicked = False



    
    def change_color(self, c1, c2):
        self.bg_color = c1
        self.color = c2

