import pygame as pg
from config import * 
import math
import random


class Player(pg.sprite.Sprite): # 
    def __init__(self, game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER #
        self.groups = self.game.all_sprites # 
        pg.sprite.Sprite.__init__(self,self.groups) # 

        self.x = x*TILESIZE 
        self.y = y*TILESIZE 
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0 # для перемещения персонажа, временные переменные на 1 такт
        self.y_change = 0 # для перемещения персонажа, временные переменные на 1 такт

        self.facing = 'down' # это для анимации. Куда смотрит персонаж
        
        self.image = pg.Surface([self.width,self.height])
        self.image.fill(RED) # 

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement() # добавляем
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0

    def movement(self): # метод для движения
        keys = pg.key.get_pressed() # будет содержать все нажатые клавиши
        if keys[pg.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pg.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pg.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pg.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'


# создаем класс для стены
class Block(pg.sprite.Sprite):
    def __init__(self, game,x,y):
        self.game = game
        self._layer = BLOCK_LAYER # на каком слое находится
        self.groups = self.game.all_sprites , self.game.blocks # к каким группам относится
        pg.sprite.Sprite.__init__(self,self.groups) # 

        self.x = x*TILESIZE 
        self.y = y*TILESIZE 
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pg.Surface([self.width,self.height])
        self.image.fill(BLUE) 

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y


































































































































