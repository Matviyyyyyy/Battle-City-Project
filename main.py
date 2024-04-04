import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
fps = pygame.time.Clock()
pygame.display.set_caption("Battle City")


running = True

while running:
    pygame.display.update()
    fps.tick(60)



