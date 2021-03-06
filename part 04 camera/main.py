import pygame as pg
import sys
from tilemap import *
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) # 开启持续按键
        self.load_data()
        

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder,'map2.txt'))

    def new(self):
        # 初始化
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                # 生成player同时防止生成的player在wall里面
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # 为True则game loop 一直运行
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) /  1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit(0)

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        # 画出横向方格
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        # 画出纵向方格
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            '''
            pygame.surface.blit(sourse,dest,area = None,special_flag=0)
            这里的surface不是模块名而是一个创建好了的surface实例
            法表示将一个surface对象画在另一个surface对象之上，
            sourse为要画的surface对象，表示要将哪一个surface对象画在调用的实例上，
            而dest则是要画在实例surface对象的什么位置，
            如果这个参数传入的是一个rect对象，则会取rect对象的左上角的点作为要开始画的地方，
            而与rect对象的大小是无关的，
            '''
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # 捕捉键盘事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
        

    def show_start_screen(self):
        pass

# 开始
def main():
    try:
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()
    except SystemExit:
        print("正常退出")
if __name__ == '__main__':
    main()
