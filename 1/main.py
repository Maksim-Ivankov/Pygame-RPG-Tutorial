# Создали структуру проекта

import pygame as pg
from sprites import *
from config import * 
import sys

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pg.time.Clock()
        # self.font = pg.font.Font('Arial',32)
        self.running = True
        
    def new(self):
        self.playing = True 
        # создадим словари, который будут содержать в себе все объекты игры
        self.all_sprites = pg.sprite.LayeredUpdates() # наличие одной гшруппы позволит обновлять их все вместе сразу
        self.blocks = pg.sprite.LayeredUpdates() # наличие одной гшруппы позволит обновлять их все вместе сразу
        self.enemies = pg.sprite.LayeredUpdates() # наличие одной гшруппы позволит обновлять их все вместе сразу
        self.attacks = pg.sprite.LayeredUpdates() # наличие одной гшруппы позволит обновлять их все вместе сразу

        self.player = Player(self,1,2) # создаем экземпляр класса игрока
        
    def events(self): # метод будет содержать все события
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
        
    def update(self): # метод будет обновлять игру
        self.all_sprites.update()
        
    def draw(self): # метод будет отображать все спрайты на экране
        self.screen.fill(BLACK) # просто залили экран
        self.all_sprites.draw(self.screen) # отрисовали всех спрайтов
        self.clock.tick(FPS) # задаем ФПС
        pg.display.update() 
        
    def main(self): # основной метод, который работает постоянно, пока мы играем
        # игровой цикл - game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
        
    def game_over(self):
        pass
        
    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pg.quit()


















































































































































