import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT
from config import FNT_DIR

def over_screen(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,"Game Over.png")).convert()
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    ButtomD = (600,840,560,610)
    ButtomE = (910,1150,560,610)

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ButtomD[0] <= mouse[0] <= ButtomD[1] and ButtomD[2] <= mouse[1] <= ButtomD[3]:
                    state = GAME
                    running = False
                if ButtomE[0] <= mouse[0] <= ButtomE[1] and ButtomE[2] <= mouse[1] <= ButtomE[3]:
                    state = QUIT
                    running = False
        
        font = pygame.font.Font(path.join(FNT_DIR,"ARCADE_N.TTF"), 180)
        #vou pedir ajuda do professor pra conseguir importar o score
        final_score = font.render("{0}".format("5"), True, (0,0,0))
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        screen.blit(final_score,(780,285))
        pygame.display.update()

    return state