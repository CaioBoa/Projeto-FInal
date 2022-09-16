import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT,SND_DIR
from config import FNT_DIR
from cursors import cursors

def over_screen(screen,player):
    # Screen Settings
    running = True
    background = pygame.image.load(path.join(IMG_DIR,"Game Over.png")).convert()
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()
    buttomD = (600,840,560,610)
    buttomE = (910,1150,560,610)
    # Music Settings
    pygame.mixer.music.load(path.join(SND_DIR,"endgame.mp3"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    pygame.time.delay(1500)

    # Run Screen
    while running:
        #Screen Settings
        font = pygame.font.Font(path.join(FNT_DIR,"ARCADE_N.TTF"), 170)
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        # Init Mouse
        mouse = pygame.mouse.get_pos()
        # Mouse Style Over Button
        if buttomD[0] <= mouse[0] <= buttomD[1] and buttomD[2] <= mouse[1] <= buttomD[3] or buttomE[0] <= mouse[0] <= buttomE[1] and buttomE[2] <= mouse[1] <= buttomE[3]:
            pygame.mouse.set_cursor(cursors[0])
        else:
            pygame.mouse.set_cursor(cursors[2])
        # Event Settings
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttomD[0] <= mouse[0] <= buttomD[1] and buttomD[2] <= mouse[1] <= buttomD[3]:
                    state = GAME
                    running = False
                elif buttomE[0] <= mouse[0] <= buttomE[1] and buttomE[2] <= mouse[1] <= buttomE[3]:
                    state = QUIT
                    running = False
        # Show Score
        score = player.getScore()
        score_text = font.render("{0}".format(score), True, (0,0,0))
        if score < 10:
            screen.blit(score_text,(800,285))
        elif score >= 10 and score < 100 :
            screen.blit(score_text,(700,285))
        elif score >= 100:
            screen.blit(score_text,(610,285))
        # Update Screen
        pygame.display.update()

    return state