import random
from tkinter import scrolledtext
import pygame
from config import CHAR_HEIGHT, WIDTH, HEIGHT, WLL_HEIGHT, Back_Speed

class Character(pygame.sprite.Sprite):
    
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets["character"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = HEIGHT - CHAR_HEIGHT 
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.score = 0
    
    def update(self):

        self.rect.y -= self.speedy

        self.rect.y = max(self.rect.y, 0)
        if self.rect.y > HEIGHT - CHAR_HEIGHT:
            self.rect.y = HEIGHT - CHAR_HEIGHT
        if self.rect.y < HEIGHT - CHAR_HEIGHT and self.speedy == 0:
            self.speedy = -3
    
    def getScore(self):
        return self.score
    
    def plusScore(self):
        self.score += 1
    

class Asteroid (pygame.sprite.Sprite):
    def __init__(self,groups,assets,rectt,speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets["asteroid"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        randomy = rectt
        self.rect.x = WIDTH - 50
        self.rect.y = randomy
        self.speedx = speed
        self.groups = groups
        self.assets = assets
    
    def update(self):

        self.rect.x -= self.speedx

        if self.rect.x < 0:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets["wall"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        randomy = random.randint(WLL_HEIGHT, HEIGHT - WLL_HEIGHT - 5)
        vel = Back_Speed
        self.rect.x = WIDTH - 50

        #falta checar umas coisas da parede(motando so o basico dela)
        self.rect.y = randomy
        self.speedx = vel
        self.groups = groups
        self.assets = assets

    def update(self):
        self.rect.x -= self.speedx

        if self.rect.x < 0:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets["coin"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        randomy = random.randint(WLL_HEIGHT + 5 , HEIGHT - WLL_HEIGHT - 5)
        vel = 2
        self.rect.x = WIDTH - 50

        self.rect.y = randomy
        self.speedx = vel
        self.groups = groups
        self.assets = assets

    def update(self):
        self.rect.x -= self.speedx

        if self.rect.x < 0:
            self.kill()


