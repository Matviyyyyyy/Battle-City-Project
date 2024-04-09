from pygame import *
class BrickWall:
    def __init__(self, x, y, filename, width, height):
        self.x = x
        self.y = y
        self.filename = filename
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.num_hits = 0


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def hit(self):
        self.num_hits += 1
    
    