import pygame
from os import path
from assets import load_assets
from config import IMG_DIR, SND_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT
from cursors import cursors



def init_screen(screen):
    assets = load_assets()
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,"Início Jogo.png")).convert()
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    ButtomD = (130,640,240,375)
    
    running = True
    pygame.mixer.music.load(path.join(SND_DIR,"cidadeSDF.mp3"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    while running:
        
        mouse = pygame.mouse.get_pos()
        if ButtomD[0] <= mouse[0] <= ButtomD[1] and ButtomD[2] <= mouse[1] <= ButtomD[3]:
            pygame.mouse.set_cursor(cursors[0])
        else:
            pygame.mouse.set_cursor(cursors[2])
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if ButtomD[0] <= mouse[0] <= ButtomD[1] and ButtomD[2] <= mouse[1] <= ButtomD[3]:
                    state = GAME
                    running = False

        screen.fill(BLACK)
        screen.blit(background,background_rect)
        pygame.display.update()

    return state