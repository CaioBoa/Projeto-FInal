import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT,SND_DIR
from config import FNT_DIR
from cursors import cursors

def over_screen(screen,score):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,"Game Over.png")).convert()
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    ButtomD = (600,840,560,610)
    ButtomE = (910,1150,560,610)

    running = True

    pygame.mixer.music.load(path.join(SND_DIR,"endgame.mp3"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    pygame.time.delay(1500)
    while running:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        if ButtomD[0] <= mouse[0] <= ButtomD[1] and ButtomD[2] <= mouse[1] <= ButtomD[3] or ButtomE[0] <= mouse[0] <= ButtomE[1] and ButtomE[2] <= mouse[1] <= ButtomE[3]:
            pygame.mouse.set_cursor(cursors[0])
        else:
            pygame.mouse.set_cursor(cursors[2])
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
        final_score = font.render("{0}".format(score), True, (0,0,0))
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        if score < 10:
            screen.blit(final_score,(780,285))
        elif score >= 10:
            screen.blit(final_score,(680,285))
        pygame.display.update()

    return state