import pygame
import random
import math
from pygame import mixer
import time
import os

mixer.init()
pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

screen=pygame.display.set_mode((1200,801))
pygame.display.set_caption('Level 2')
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

background=pygame.image.load('bg.png')

spaceshipimg=pygame.image.load('arcade.png')

monkeyimg=[]
monkeyX=[]
monkeyY=[]
monkeyspeedX=[]
monkeyspeedY=[]

no_of_monkey=1

for i in range(no_of_monkey):

    monkeyimg.append(pygame.image.load('enemy.png'))
    monkeyX.append(random.randint(0,736))
    monkeyY.append(random.randint(30,150))
    monkeyspeedX.append(-1)
    monkeyspeedY.append(40)

score=0

bulletimg=pygame.image.load('bullet.png')
check=False
bulletX=386
bulletY=490

player_X=470
player_Y=580
changeX=0
running=True

font=pygame.font.SysFont('Arial',32,'bold')

def score_text():
    img=font.render(f'Score:{score}',True,'white')
    screen.blit(img,(10,10))

font_gameover=pygame.font.SysFont('Arial',64,'bold')

def gameover():
    img_gameover = font_gameover.render('GAME OVER', True, 'white')
    screen.blit(img_gameover, (200, 250))
    # pygame.display.update() 
    time.sleep(5)
    # if event.key == pygame.K_SPACE:
    #     continue
    # else:
    #     time.sleep(3)
    exit()






while running:

    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-5
            if event.key==pygame.K_RIGHT:
                changeX=5
            if event.key==pygame.K_SPACE:
                if check is False:
                    bulletSound=mixer.Sound('laser.mpeg')
                    bulletSound.play()
                    check=True
                    bulletX=player_X+16

        if event.type==pygame.KEYUP:
            changeX=0
    player_X+=changeX  #player_X=player_X-changeX
    if player_X<=0:
        player_X=0
    elif player_X>=736:
        player_X=736
    for i in range(no_of_monkey):
        if monkeyY[i] > 420:
            for j in range(no_of_monkey):
                monkeyY[j] = 2000
            gameover()
            break
        monkeyX[i]+=monkeyspeedX[i]
        if monkeyX[i]<=0:
            monkeyspeedX[i]=1
            monkeyY[i]+=monkeyspeedY[i]
        if monkeyX[i]>=736:
            monkeyspeedX[i]=-1
            monkeyY[i]+=monkeyspeedY[i]
            
        if score==1:
            os.wait(5)
            if event.key == pygame.K_SPACE:
                continue
            else:
                gameover()
        

        distance = math.sqrt(math.pow(bulletX - monkeyX[i], 2) + math.pow(bulletY - monkeyY[i], 2))
        if distance < 27:
            explosion= mixer.Sound('explosion.wav')
            explosion.play()
            bulletY = 480
            check = False
            monkeyX[i] = random.randint(0, 736)
            monkeyY[i] = random.randint(30, 150)
            score += 1
        screen.blit(monkeyimg[i], (monkeyX[i], monkeyY[i]))

    if bulletY<=0:
        bulletY=490
        check=False
    if check:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY-=5








    screen.blit(spaceshipimg, (player_X, player_Y))
    score_text()
    pygame.display.update()


class Game:
    pass