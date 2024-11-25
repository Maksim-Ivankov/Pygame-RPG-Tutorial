import pygame as pg
from config import * 
import math
import random
#

class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()
        
    def get_sprite(self,x,y,width,height): 
        sprite = pg.Surface([width,height])
        sprite.blit(self.sheet, (0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK) 
        return sprite

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
        
        self.x_change = 0 
        self.y_change = 0 

        self.facing = 'down' 
        

        self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement() 
        self.rect.x += self.x_change
        self.colide_blocks('x')
        self.rect.y += self.y_change
        self.colide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0

    def movement(self): 
        keys = pg.key.get_pressed() 
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
    
    def colide_blocks(self,direction): # метод определяет колизию, параметр - направление
        if direction == 'x':
            hits = pg.sprite.spritecollide(self,self.game.blocks, False) # проверяем, находится ли хитбокс игрока в хитбоксе блока
            if hits: # еслли находится
                if self.x_change>0: # проверяем движется игрок влево или вправо
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change<0: # проверяем движется игрок влево или вправо
                    self.rect.x = hits[0].rect.right
        if direction == 'y':
            hits = pg.sprite.spritecollide(self,self.game.blocks, False) # проверяем, находится ли хитбокс игрока в хитбоксе блока
            if hits: # еслли находится
                if self.y_change>0: # проверяем движется игрок влево или вправо
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change<0: # проверяем движется игрок влево или вправо
                    self.rect.y = hits[0].rect.bottom

class Block(pg.sprite.Sprite):
    def __init__(self, game,x,y):
        self.game = game
        self._layer = BLOCK_LAYER 
        self.groups = self.game.all_sprites , self.game.blocks 
        pg.sprite.Sprite.__init__(self,self.groups) # 

        self.x = x*TILESIZE 
        self.y = y*TILESIZE 
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960,448,self.width,self.height)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pg.sprite.Sprite):
    def __init__(self, game,x,y):
        self.game = game
        self._layer = GROUND_LAYER 
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups) # 

        self.x = x*TILESIZE 
        self.y = y*TILESIZE 
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64,352,self.width,self.height)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

































































































































