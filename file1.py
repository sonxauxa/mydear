import os, sys, pygame

from pygame.locals import *

fpsClock = pygame.time.Clock()
pygame.init()
surface = pygame.display.set_mode((600, 600))
background = pygame.Color(255, 255, 255)
image = pygame.image.load("2.png")
while True:
    surface.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(60)
        surface.blit(image, (0, 0),  (0, 0, 132, 102))
