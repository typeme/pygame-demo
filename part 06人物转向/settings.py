import pygame as pg
# 定义了一些颜色 (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 游戏基本设定 
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 80 # 刷新率
TITLE = "part 06 Demo"
BGCOLOR = DARKGREY # 背景颜色

TILESIZE = 64 # 方格的尺寸
GRIDWIDTH = WIDTH / TILESIZE  # 每行方格的数量
GRIDHEIGHT = HEIGHT / TILESIZE # 每列方格的数量

# Player settings
PLAYER_SPEED = 300.0
PLAYER_ROT_SPEED = 250.0
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

