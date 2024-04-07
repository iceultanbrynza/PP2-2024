import pygame
import random
import time, sys
from pygame.locals import *
pygame.init()

#color palette
colorBLACK = (0, 0, 0) 
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
#display
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBLACK)

SCORE = 0
COINS = 0
BACKGROUND = pygame.image.load("./RacerGame/racer_resources/AnimatedStreet.png")
FPS = pygame.time.Clock()

pygame.mixer.music.load("./RacerGame/racer_resources/race_mus.wav")
pygame.mixer.music.play(-1)

#objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./RacerGame/racer_resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def movement(self): 
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left>0:
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_d] and self.rect.x + self.rect.w < WIDTH:
            self.rect.move_ip(5, 0) 
            print(self.rect.x)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./RacerGame/racer_resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)
    def movement(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), 0)
class Peaceful(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load = pygame.image.load("./RacerGame/racer_resources/coin.png")
        self.image = pygame.transform.scale(self.load, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)
    def movement(self):
        self.rect.move_ip(0, 5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), 0)
    def collision(self):
        global COINS
        COINS +=1
        self.rect.top = 0
        self.rect.center = (random.randint(40, WIDTH-40), 0)
P1 = Player()
E1 = Enemy()
C1 = Peaceful()
#Grouping the sprites
enemies = pygame.sprite.Group()
all_objects = pygame.sprite.Group()
peaceful_objects = pygame.sprite.Group()
enemies.add(E1)
all_objects.add(P1)
all_objects.add(E1)
all_objects.add(C1)
peaceful_objects.add(C1)
#Event for changing the speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
SPEED = 5
VOLUME = 1
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED+=0.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                VOLUME+=1
                pygame.mixer.music.set_volume(VOLUME)
            if event.key == pygame.K_LEFT:
                VOLUME-=1
                pygame.mixer.music.set_volume(VOLUME)
    screen.blit(BACKGROUND, (0,0))
    scores = font_small.render(str(SCORE), True, colorBLACK)
    coin_amount = font_small.render(str(COINS), True, colorYELLOW)
    result1 = font_small.render(f"Your score: {SCORE}", True, colorYELLOW)
    result2 = font_small.render(f"100 tenge collected: {COINS}", True, colorYELLOW)
    screen.blit(scores, (10,10))
    screen.blit(coin_amount, (370, 10))
    for entity in all_objects:
        entity.movement()
        screen.blit(entity.image, entity.rect) #(surface to blit, coordinates where to blit)
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('./RacerGame/racer_resources/crash.wav').play()
        time.sleep(0.5)
        screen.fill(colorRED)
        screen.blit(game_over, (30, 250))
        screen.blit(result1, (130, 325))
        screen.blit(result2, (95, 350))
        pygame.display.flip()
        time.sleep(2)
        done = True
    if pygame.sprite.spritecollideany(P1, peaceful_objects): 
        for entity in peaceful_objects:
            entity.collision()


    pygame.display.flip()
    FPS.tick(60)