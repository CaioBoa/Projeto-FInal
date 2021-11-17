import random
import pygame
from config import CHAR_HEIGHT, CHAR_WIDTH, WIDTH, HEIGHT, AST_HEIGHT
from assets import CHARACTER, ASTEROID, WALL

class character(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CHARACTER]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - CHAR_WIDTH / 2
        self.rect.y = HEIGHT - CHAR_HEIGHT 
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    
    def update(self):

        self.rect.y -= self.speedy

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - CHAR_HEIGHT:
            self.rect.y = HEIGHT - CHAR_HEIGHT
        if self.rect.y < HEIGHT - CHAR_HEIGHT and self.speedy == 0:
            self.speedy = -3

class asteroid(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ASTEROID]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        randomy = random.randint(AST_HEIGHT + 5 , HEIGHT - AST_HEIGHT - 5)
        self.rect.x = WIDTH - 50
        self.rect.y = randomy
        self.speedx = 2
        self.groups = groups
        self.assets = assets
    
    def update(self):

        self.rect.x -= self.speedx

        if self.rect.x < 0:
            self.kill()

class wall(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[WALL]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        randomy = random.randint(AST_HEIGHT + 5 , HEIGHT - AST_HEIGHT - 5)
        vel = (random.randint(1,4))
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

