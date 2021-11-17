import pygame
from os import path
from config import CHAR_HEIGHT, CHAR_WIDTH, IMG_DIR, SND_DIR, FNT_DIR, WIDTH, HEIGHT, AST_WIDTH, AST_HEIGHT

BACKGROUND = "background"
CHARACTER = "character"
ASTEROID = "asteroid"

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(path.join(IMG_DIR,"background.jpg")).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND],(WIDTH,HEIGHT))
    assets[CHARACTER] = pygame.image.load(path.join(IMG_DIR,"character.png")).convert_alpha()
    assets[CHARACTER] = pygame.transform.scale(assets[CHARACTER],(CHAR_WIDTH,CHAR_HEIGHT))
    assets[ASTEROID] = pygame.image.load(path.join(IMG_DIR,"asteroid.png")).convert_alpha()
    assets[ASTEROID] = pygame.transform.scale(assets[BACKGROUND],(AST_WIDTH,AST_HEIGHT))

    return assets