import random
import pygame
from config import WIDTH, HEIGHT
from assets import CHARACTER

class character(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CHARACTER]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    
    def update(self):

        self.rect.y += self.speedy

        if self.rect.top > 0:
            self.rect.top = 0
        if self.rect.bottom < HEIGHT:
            self.rect.bottom = HEIGHT