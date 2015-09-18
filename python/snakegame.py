#!/usr/bin/env python
import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

playsurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Rasberry Snake')

redcolour = pygame.Color(255, 0, 0)
blackcolour = pygame.Color(0, 0, 0)
whitecolour = pygame.Color(255, 255, 255)
greycolour = pygame.Color(150, 150, 150)

snakeposition = [100,100]
snakesegments = [[100,100],[80,100],[60,100]]
raspberryposition = [300,300]
raspberryspawned = 1
direction = 'right'
changedirection = direction

def gameover():
    gameoverfont = pygame.font.Font('freesansbold.ttf', 72)
    gameoversurf = gameoverfont.render('game over', True, greycolour)
    gameoverrect = gameoversurf.get_rect()
    gameoverrect.midtop = (320, 10)
    playsurface.blit(gameoversurf, gameoverrect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:

            if event.key == K_RIGHT or event.key == ord('d'):
                changedirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changedirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changedirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changedirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changedirection == 'right' and not direction =='left':
        direction = changedirection
    if changedirection == 'left' and not direction =='right':
        direction = changedirection
    if changedirection == 'up' and not direction =='down':
        direction = changedirection
    if changedirection == 'down' and not direction =='up':
        direction = changedirection

    if direction == 'right':
        snakeposition[0] += 20
    if direction == 'left':
        snakeposition[0] -= 20
    if direction == 'up':
        snakeposition[1] -= 20
    if direction == 'down':
        snakeposition[1] += 20

    snakesegments.insert(0,list(snakeposition))

    if snakeposition[0] == raspberryposition[0] and snakeposition[1] == raspberryposition[1]:
        raspberryspawned = 0
    else:
        snakesegments.pop()
    
    if raspberryspawned == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryposition = [int(x*20),int(y*20)]

    raspberryspawned = 1
    playsurface.fill(blackcolour)

    for position in snakesegments:
        pygame.draw.rect(playsurface, whitecolour, Rect(position[0],position[1],20,20))

    pygame.draw.rect(playsurface, redcolour, Rect(raspberryposition[0],raspberryposition[1],20,20))

    pygame.display.flip()

    if snakeposition[0] > 620 or snakeposition[0] < 0:
        gameover()

    if snakeposition[1] > 460 or snakeposition[1] < 0:
         gameover()

        
    for snakebody in snakesegments[1:]:
        if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
            gameover()

    fpsClock.tick(4)

        
