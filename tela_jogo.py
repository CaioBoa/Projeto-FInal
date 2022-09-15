import pygame
from config import FPS, OVER, WIDTH, HEIGHT, BLACK, FNT_DIR, SND_DIR, Back_Speed
from assets import load_assets
from sprites import asteroid, character, wall, coin
from os import path
from cursors import cursors

def game_screen(window):
    u = 0
    clock = pygame.time.Clock()
    assets = load_assets()

    coin_sound = assets["sound_coin"]
    dmg_sound = assets["sound_dmg"]


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
    #missile_speed
    missile_speed = 10
    #guide count
    guide_count = 0

    DONE = 0
    PLAYING = 1
    
    state = PLAYING
    pygame.mixer.music.load(path.join(SND_DIR,"FORSDF.mp3")) 
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    # ===== Loop principal =====
    while state != DONE:
        #game_sound.play()
        score = player.getScore()
        
        clock.tick(FPS)

        font2 = pygame.font.Font(path.join(FNT_DIR,"ARCADE_N.TTF"), 34)
        guide = font2.render("Hold Space to fly", True, (255,255,0))
        guide_count += 1

        mouse = pygame.mouse.get_pos()
        if 0 < mouse[0] < WIDTH and 0 < mouse[1] < HEIGHT:
            pygame.mouse.set_cursor(cursors[2])

        #gerador de asteróides
        a += 1
        w += 1
        c += 1
        missile_cd = 180
        wall_cd = 210
        coin_cd = 60

        if a == missile_cd:
            astro = asteroid(groups,assets,player.rect.y,missile_speed)
            all_sprites.add(astro)
            all_astros.add(astro)
            a = 0
        if w == wall_cd:
            walll = wall (groups,assets)
            all_sprites.add(walll)
            all_walls.add(walll)
            w = 0  
        if c == coin_cd:
            coinn = coin (groups,assets)
            all_sprites.add(coinn)
            all_coins.add(coinn)
            c = 0 

        Bx -= Back_Speed
        Bx2 -= Back_Speed
        if Bx <= -WIDTH:
            Bx = WIDTH-1
        if Bx2 <= -WIDTH:
            Bx2 = WIDTH-1

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
                #som dano
                dmg_sound.play()
                
                player.kill()
                
                state = DONE

            hits_wall = pygame.sprite.spritecollide(player, all_walls, True, pygame.sprite.collide_mask)
            if len(hits_wall) > 0:
                #som dano
                dmg_sound.play()
                
                player.kill()
                
                state = DONE

            hits_coin = pygame.sprite.spritecollide(player, all_coins, True, pygame.sprite.collide_mask)
            if len(hits_coin) > 0:
                player.plusScore()
                coin_sound.play()

        #contador de moedas
        font = pygame.font.Font(path.join(FNT_DIR,"ARCADE_N.TTF"), 56)
        score_count = font.render("Score = {0}".format(score), True, (0,255,255))

        all_sprites.update()

        window.fill(BLACK)
        Background = assets["background"]
        
        if score >= 5:
            Background = assets["background1"]
            missile_speed = 15
            missile_cd = 150
            wall_cd = 170
            if u == 0:
                pygame.mixer.music.load(path.join(SND_DIR,"space.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                u += 1
        if score >= 20:
            Background = assets["background2"]
            missile_speed = 20
            missile_cd = 120
            wall_cd = 130
            if u == 1:
                pygame.mixer.music.load(path.join(SND_DIR,"desert.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                u += 1
        if score >= 100:
            Background = assets["background3"]
            window.blit(score_count, (WIDTH-700, 15))
            missile_speed = 40
            missile_cd = 60
            wall_cd = 60
            if u == 2:
                pygame.mixer.music.load(path.join(SND_DIR,"pink_soldiers.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                u += 1
            

        window.blit(Background, (Bx, 0))
        window.blit(Background, (Bx2, 0))
        if score < 10:
            window.blit(score_count, (WIDTH-500, 15))
        elif score >= 10 and score < 100:
            window.blit(score_count, (WIDTH-560, 15))
        elif score >= 100:
            window.blit(score_count, (WIDTH-620, 15))
        if guide_count <= 200:
            window.blit(guide, (WIDTH/2-100, HEIGHT/2-50))

        all_sprites.draw(window)

        pygame.display.update()

    if state == DONE:
        
        return (OVER, player)