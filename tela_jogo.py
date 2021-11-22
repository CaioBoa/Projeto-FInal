import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, FNT_DIR, Back_Speed
from assets import load_assets, BACKGROUND
from sprites import asteroid, character, wall, coin

def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_astros = pygame.sprite.Group()
    all_walls = pygame.sprite.Group()
    all_coins = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups["all astros"] = all_astros
    groups["all walls"] = all_walls
    groups["all coins"] = all_coins

    player = character(groups, assets)
    all_sprites.add(player)

    #para gerar asteróides
    a = 0
    w = 0
    c = 0
    #Movimento do Fundo
    Bx = 0
    Bx2 = WIDTH
    score = 0
    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        #gerador de asteróides
        a += 1
        w += 1
        c += 1
        astro_cd = 120
        if a == astro_cd:
            astro = asteroid(groups,assets,player.rect.y)
            all_sprites.add(astro)
            all_astros.add(astro)
            a = 0
        if w/2 == astro_cd:
            walll = wall (groups,assets)
            all_sprites.add(walll)
            all_walls.add(walll)
            w = 0  
        if c/2 == astro_cd:
            coinn = coin (groups,assets)
            all_sprites.add(coinn)
            all_coins.add(coinn)
            c = 0 

        Bx -= Back_Speed
        Bx2 -= Back_Speed
        if Bx2 == 0:
            Bx = WIDTH
        if Bx == 0:
            Bx2 = WIDTH

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
            hits_coin = pygame.sprite.spritecollide(player, all_coins, True, pygame.sprite.collide_mask)
            if len(hits_coin) > 0:
                score += 1

        #contador de moedas
        font = pygame.font.SysFont((FNT_DIR,"ARCADE_N.TTF"), 68)
        #não consegui fazer a fonte funcionar se alguém ae quiser tentar
        score_count = font.render("Score = {0}".format(score), True, (0,255,255))

        all_sprites.update()

        window.fill(BLACK)
        window.blit(assets[BACKGROUND], (Bx, 0))
        window.blit(assets[BACKGROUND], (Bx2, 0))
        window.blit(score_count, (10, 10))
        all_sprites.draw(window)

        pygame.display.update()