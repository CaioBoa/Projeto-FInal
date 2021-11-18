import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, BACKGROUND
from sprites import asteroid, character, wall

def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_astros = pygame.sprite.Group()
    all_walls = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups["all astros"] = all_astros
    groups["all walls"] = all_walls

    player = character(groups, assets)
    all_sprites.add(player)

    #para gerar asteróides
    a = 0
    w = 0
    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        #gerador de asteróides
        a += 1
        w += 1
        astro_cd = 120
        if a == astro_cd:
            astro = asteroid(groups,assets)
            all_sprites.add(astro)
            all_astros.add(astro)
            a = 0
        if w/2 == astro_cd:
            walll = wall (groups,assets)
            all_sprites.add(walll)
            all_walls.add(walll)
            a = 0  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.speedy += 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        player.speedy -= 10

        if state == PLAYING:
            hits_astro = pygame.sprite.spritecollide(player, all_astros, True, pygame.sprite.collide_mask)
            if len(hits_astro) > 0:
                player.kill()
                state = DONE
            hits_wall = pygame.sprite.spritecollide(player, all_walls, True, pygame.sprite.collide_mask)
            if len(hits_wall) > 0:
                player.kill()
                state = DONE

        all_sprites.update()

        window.fill(BLACK)
        window.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()