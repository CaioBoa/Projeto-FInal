import pygame
from config import FPS, OVER, WIDTH, HEIGHT, BLACK, FNT_DIR, SND_DIR, Back_Speed
from assets import load_assets
from sprites import Asteroid, Character, Wall, Coin
from os import path
from cursors import cursors

def game_screen(window):
    # Load Assets
    assets = load_assets()
    # Load sounds
    music_setter = 0
    coin_sound = assets["sound_coin"]
    dmg_sound = assets["sound_dmg"]
    # Load Clock
    clock = pygame.time.Clock()
    # Load Groups and Sprites
    all_sprites = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()
    all_obstacles = pygame.sprite.Group()
    all_coins = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups["all obstacles"] = all_obstacles
    groups["all coins"] = all_coins
    # Create Player
    player = Character(groups, assets)
    all_sprites.add(player)
    # Sprites Generator Start
    missile_timer = 0
    wall_timer = 0
    coin_timer = 0
    # Background Movement Start
    Bx = 0
    Bx2 = WIDTH
    # Tutorial Timer Start
    tutorial_timer = 0
    # Game Loop
    DONE = 0
    PLAYING = 1
    # Game State
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        score = player.getScore()
        # Screen Settings
        font2 = pygame.font.Font(path.join(FNT_DIR,"ARCADE_N.TTF"), 34)
        guide = font2.render("Hold Space to fly", True, (255,255,0))
        
        clock.tick(FPS)

        font2 = pygame.font.Font(path.join(FNT_DIR,"ARCADE_N.TTF"), 34)
        guide = font2.render("Hold Space to fly", True, (255,255,0))
        tutorial_timer += 1

        mouse = pygame.mouse.get_pos()
        if 0 < mouse[0] < WIDTH and 0 < mouse[1] < HEIGHT:
            pygame.mouse.set_cursor(cursors[2])

        if score < 5:
            Background = assets["background"]
            missile_speed = 10
            missile_cd = 180
            wall_cd = 210
            coin_cd = 60
            if music_setter == 0:
                pygame.mixer.music.load(path.join(SND_DIR,"FORSDF.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                music_setter += 1
        elif score >= 5:
            Background = assets["background1"]
            missile_speed = 15
            missile_cd = 150
            wall_cd = 170
            coin_cd = 60
            if music_setter == 1:
                pygame.mixer.music.load(path.join(SND_DIR,"space.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                music_setter += 1
        elif score >= 20:
            Background = assets["background2"]
            missile_speed = 20
            missile_cd = 120
            wall_cd = 130
            coin_cd = 60
            if music_setter == 2:
                pygame.mixer.music.load(path.join(SND_DIR,"desert.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                music_setter += 1
        elif score >= 100:
            Background = assets["background3"]
            window.blit(score_count, (WIDTH-700, 15))
            missile_speed = 40
            missile_cd = 60
            wall_cd = 60
            coin_cd = 60
            if music_setter == 3:
                pygame.mixer.music.load(path.join(SND_DIR,"pink_soldiers.mp3")) 
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                music_setter = None

        # sprites timers
        missile_timer += 1
        wall_timer += 1
        coin_timer += 1

        if missile_timer == missile_cd:
            astro = Asteroid(groups,assets,player.rect.y,missile_speed)
            all_sprites.add(astro)
            all_obstacles.add(astro)
            missile_timer = 0
        if wall_timer == wall_cd:
            walll = Wall (groups,assets)
            all_sprites.add(walll)
            all_obstacles.add(walll)
            wall_timer = 0  
        if coin_timer == coin_cd:
            coinn = Coin (groups,assets)
            all_sprites.add(coinn)
            all_coins.add(coinn)
            coin_timer = 0 

        #Background Speed
        Bx -= Back_Speed
        Bx2 -= Back_Speed
        if Bx <= -WIDTH:
            Bx = WIDTH-1
        if Bx2 <= -WIDTH:
            Bx2 = WIDTH-1

        # Events
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
            hits_obstacle = pygame.sprite.spritecollide(player, all_obstacles, True, pygame.sprite.collide_mask)
            if len(hits_obstacle) > 0:
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
            
        window.blit(Background, (Bx, 0))
        window.blit(Background, (Bx2, 0))
        if score < 10:
            window.blit(score_count, (WIDTH-500, 15))
        elif score >= 10 and score < 100:
            window.blit(score_count, (WIDTH-560, 15))
        elif score >= 100:
            window.blit(score_count, (WIDTH-620, 15))
        if tutorial_timer <= 200:
            window.blit(guide, (WIDTH/2-100, HEIGHT/2-50))

        all_sprites.draw(window)

        pygame.display.update()

    if state == DONE:
        
        return (OVER, player)