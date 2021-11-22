from os import path

# Caminho para as pastas de som, imagem e fonte
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Configurações gerais
WIDTH = 1255
HEIGHT = 640
FPS = 60 

# Tamanho sprites
    #Personagem
CHAR_WIDTH = 80
CHAR_HEIGHT = 100
    #Asteroide
AST_WIDTH = 40
AST_HEIGHT = 50
    #Paredes
WLL_WIDTH = 20
WLL_HEIGHT = 70
    #Coins
COIN_WIDTH = 30
COIN_HEIGHT = 30
    #Background Speed
Back_Speed = 2

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados do jogo
INIT = 0
GAME = 1
OVER = 2
QUIT = 3