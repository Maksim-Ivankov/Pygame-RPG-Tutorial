# Анимация персонажа

import pygame as pg
from sprites import *
from config import * 
import sys

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.character_spritesheet = Spritesheet('img/character.png') 
        self.terrain_spritesheet = Spritesheet('img/terrain.png') 
        
    def createTilemap(self):    
        for i,row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column == 'B': Block(self,j,i)
                if column == 'P': Player(self,j,i)
                
    
    
    def new(self):
        self.playing = True 
        
        self.all_sprites = pg.sprite.LayeredUpdates() 
        self.blocks = pg.sprite.LayeredUpdates() 
        self.enemies = pg.sprite.LayeredUpdates() 
        self.attacks = pg.sprite.LayeredUpdates() 

        self.createTilemap()
        
        
    def events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
        
    def update(self): 
        self.all_sprites.update()
        
    def draw(self): # 
        self.screen.fill(BLACK) # 
        self.all_sprites.draw(self.screen) # 
        self.clock.tick(FPS) # 
        pg.display.update() 
        
    def main(self): # 
        # 
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


















































































































































