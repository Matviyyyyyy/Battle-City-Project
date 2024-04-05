import pygame
class Bush:
    def __init__(self, x, y, hits, filename):
        self.x = x
        self.y = y
        self.hits = hits
        self.filename = filename
    def draw(self, window):
        window.blit(self.filename, (self.rect.x, self.rect.y))

