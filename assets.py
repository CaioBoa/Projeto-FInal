import pygame
from os import path
from config import IMG_DIR, SND_DIR, FNT_DIR

BACKGROUND = "background"
CHARACTER = "character"

def load_assets():
    assets = {}
    assets(BACKGROUND) = pygame.image.load(path.join(IMG_DIR,"background.jpg")).convert()
    assets(CHARACTER) = pygame.image.load(path.join(IMG_DIR,"character.png")).convert_alpha()

    return assets