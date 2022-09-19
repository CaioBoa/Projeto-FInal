from inspect import _void
import pygame
from os import path
from config import CHAR_HEIGHT, CHAR_WIDTH, IMG_DIR, SND_DIR, WIDTH, HEIGHT, AST_WIDTH, AST_HEIGHT, WLL_WIDTH, WLL_HEIGHT, COIN_WIDTH, COIN_HEIGHT

def load_assets():
    # create dict to store assets
    assets = {}
    assets["background"] = pygame.image.load(path.join(IMG_DIR,"f1_flo.png")).convert()
    assets["background"] = pygame.transform.scale(assets["background"],(WIDTH,HEIGHT))
    assets["background1"] = pygame.image.load(path.join(IMG_DIR,"f2_esp.png")).convert()
    assets["background1"] = pygame.transform.scale(assets["background1"],(WIDTH,HEIGHT))
    assets["background2"] = pygame.image.load(path.join(IMG_DIR,"desert.png")).convert()
    assets["background2"] = pygame.transform.scale(assets["background2"],(WIDTH,HEIGHT))
    assets["background3"] = pygame.image.load(path.join(IMG_DIR,"round6.png")).convert()
    assets["background3"] = pygame.transform.scale(assets["background3"],(WIDTH,HEIGHT))
    assets["character"] = pygame.image.load(path.join(IMG_DIR,"jetpack.png")).convert_alpha()
    assets["character"] = pygame.transform.scale(assets["character"],(CHAR_WIDTH,CHAR_HEIGHT))
    assets["asteroid"] = pygame.image.load(path.join(IMG_DIR,"Missel.png")).convert_alpha()
    assets["asteroid"] = pygame.transform.scale(assets["asteroid"],(AST_WIDTH,AST_HEIGHT))
    assets["wall"] = pygame.image.load(path.join(IMG_DIR,"parede.png")).convert_alpha()
    assets["wall"] = pygame.transform.scale(assets["wall"],(WLL_WIDTH,WLL_HEIGHT))

    assets["coin"] = pygame.image.load(path.join(IMG_DIR,"coin.png")).convert_alpha()
    assets["coin"] = pygame.transform.scale(assets["coin"],(COIN_WIDTH,COIN_HEIGHT))
    # all sound sprites
    assets["sound_dmg"] = pygame.mixer.Sound(path.join(SND_DIR,"Dano.mp3"))
    pygame.mixer.Sound.set_volume(assets["sound_dmg"],0.5)
    assets["sound_coin"] = pygame.mixer.Sound(path.join(SND_DIR,"coin.mp3"))
    pygame.mixer.Sound.set_volume(assets["sound_coin"],0.3)

    return assets