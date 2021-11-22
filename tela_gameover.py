import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT

def over_screen(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,"Game Over.png")).convert()
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        screen.fill(BLACK)
        screen.blit(background,background_rect)
        pygame.display.update()

    return state