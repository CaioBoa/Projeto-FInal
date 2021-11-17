import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, BACKGROUND
from sprites import character

def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    player = character(groups, assets)
    all_sprites.add(player)

    DONE = 0
    PLAYING = 1
    keys_down = {}
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE:
                        player.speedy -= 8
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_SPACE:
                            player.speedy += 8

        all_sprites.update()

        window.fill(BLACK)
        window.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()