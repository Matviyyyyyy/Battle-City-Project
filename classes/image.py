import pygame
class Image:
    def __init__(self, filename, x, y, width, height, is_draw):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (width, height))  # змінюємо розмір картинки
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = width
        self.height = height
        self.border_color = (255, 255, 255)  # колір рамки за замовчуванням
        self.border_width = 2  # ширина рамки за замовчуванням
        self.is_draw = is_draw

    def draw(self, surface):
        # Відображення картинки
        surface.blit(self.image, self.rect)

        # Отримання координат для рамки
        border_rect = pygame.Rect(self.rect.x - self.border_width, self.rect.y - self.border_width, self.width + 2*self.border_width, self.height + 2*self.border_width)

        # Відмальовування рамки
        pygame.draw.rect(surface, self.border_color, border_rect, self.border_width)

        

        