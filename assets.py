import pygame
from os import path
from config import CHAR_HEIGHT, CHAR_WIDTH, IMG_DIR, SND_DIR, FNT_DIR, WIDTH, HEIGHT, AST_WIDTH, AST_HEIGHT, WLL_WIDTH, WLL_HEIGHT

BACKGROUND = "background"
CHARACTER = "character"
ASTEROID = "asteroid"
WALL = "wall"

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(path.join(IMG_DIR,"background.jpg")).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND],(WIDTH,HEIGHT))
    assets[CHARACTER] = pygame.image.load(path.join(IMG_DIR,"character.png")).convert_alpha()
    assets[CHARACTER] = pygame.transform.scale(assets[CHARACTER],(CHAR_WIDTH,CHAR_HEIGHT))
    assets[ASTEROID] = pygame.image.load(path.join(IMG_DIR,"asteroid.png")).convert_alpha()
    assets[ASTEROID] = pygame.transform.scale(assets[BACKGROUND],(AST_WIDTH,AST_HEIGHT))
    assets[WALL] = pygame.image.load(path.join(IMG_DIR,"parede.png")).convert_alpha()
    assets[WALL] = pygame.transform.scale(assets[BACKGROUND],(WLL_WIDTH,WLL_HEIGHT))

    return assets