import pygame
from os import path
from config import CHAR_HEIGHT, CHAR_WIDTH, IMG_DIR, SND_DIR, FNT_DIR

BACKGROUND = "background"
CHARACTER = "character"

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(path.join(IMG_DIR,"background.jpg")).convert()
    assets[CHARACTER] = pygame.image.load(path.join(IMG_DIR,"character.png")).convert_alpha()
    assets[CHARACTER] = pygame.transform.scale(assets[CHARACTER],(CHAR_WIDTH,CHAR_HEIGHT))

    return assets