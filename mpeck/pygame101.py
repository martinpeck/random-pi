import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Drawing')

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

DISPLAYSURF.fill(WHITE)

pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0), (291,106), (235,277), (56,277), (0,106)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

                    
