# Добавляем экран с заставкой
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
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.intro_bacgraund = pg.image.load('img/introbackground.png')# изображение интро
        
        self.font = pg.font.Font('fonts/ofont.ru_Pixel Cyr.ttf',32) # партируем шрифт
        
    def createTilemap(self):    
        for i,row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column == 'B': Block(self,j,i)
                if column == 'P': Player(self,j,i)
                if column == 'E': Enemy(self,j,i)
                
    
    
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
        
    # Работа над первым экраном
    def intro_screen(self):
        intro = True
        
        title = self.font.render('Потрясающая игра', True, BLACK)
        title_rect = title.get_rect(x=10,y=10)
        
        # создаем кнопку
        play_button = Button(10,50,100,50,WHITE,BLACK,'Игра',32)
        
        while intro:
            for event in pg.event.get(): # если выходим, то выходим
                if event.type == pg.QUIT:
                    intro = False
                    self.running = True
            
            mouse_pos = pg.mouse.get_pos() # получаем координаты для определения нажатия на кнопку
            mouse_pressed = pg.mouse.get_pressed() # получаем координаты для определения нажатия на кнопку
            # проверяем, нажата ли кнопка воспроизведения
            if play_button.is_pressed(mouse_pos,mouse_pressed): # если кнопка плей нажата
                intro = False
            
            self.screen.blit(self.intro_bacgraund, (0,0))
            self.screen.blit(title,title_rect)
            self.screen.blit(play_button.image,play_button.rect)
            self.clock.tick(FPS)
            pg.display.update()
            


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pg.quit()


















































































































































