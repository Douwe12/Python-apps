import pygame   
import sys
import time as t
 
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
background = pygame.image.load("GameTest1\pygame_background.png")
pygame.display.set_caption("Movement")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.flip()

