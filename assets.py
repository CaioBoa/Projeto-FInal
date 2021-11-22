import pygame
from os import path
from config import CHAR_HEIGHT, CHAR_WIDTH, IMG_DIR, SND_DIR, FNT_DIR, WIDTH, HEIGHT, AST_WIDTH, AST_HEIGHT, WLL_WIDTH, WLL_HEIGHT, COIN_WIDTH, COIN_HEIGHT

BACKGROUND = "background"
BACKGROUND1 = "background1"
CHARACTER = "character"
ASTEROID = "asteroid"
WALL = "wall"
COIN = "coin"

def load_assets():
    assets = {}
    #sprites
    assets[BACKGROUND] = pygame.image.load(path.join(IMG_DIR,"f1_flo.png")).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND],(WIDTH,HEIGHT))
    assets[BACKGROUND1] = pygame.image.load(path.join(IMG_DIR,"f2_esp.png")).convert()
    assets[BACKGROUND1] = pygame.transform.scale(assets[BACKGROUND1],(WIDTH,HEIGHT))
    assets[CHARACTER] = pygame.image.load(path.join(IMG_DIR,"jetpack.png")).convert_alpha()
    assets[CHARACTER] = pygame.transform.scale(assets[CHARACTER],(CHAR_WIDTH,CHAR_HEIGHT))
    assets[ASTEROID] = pygame.image.load(path.join(IMG_DIR,"Missel.png")).convert_alpha()
    assets[ASTEROID] = pygame.transform.scale(assets[ASTEROID],(AST_WIDTH,AST_HEIGHT))
    assets[WALL] = pygame.image.load(path.join(IMG_DIR,"parede.png")).convert_alpha()
    assets[WALL] = pygame.transform.scale(assets[WALL],(WLL_WIDTH,WLL_HEIGHT))
    assets[COIN] = pygame.image.load(path.join(IMG_DIR,"coin.png")).convert_alpha()
    assets[COIN] = pygame.transform.scale(assets[COIN],(COIN_WIDTH,COIN_HEIGHT))

    return assets