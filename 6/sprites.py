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
        self.animation_loop = 0 # переменная для анимациии

        self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement() 
        self.animate()
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
    
    def colide_blocks(self,direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self,self.game.blocks, False) 
            if hits: 
                if self.x_change>0: 
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change<0: 
                    self.rect.x = hits[0].rect.right
        if direction == 'y':
            hits = pg.sprite.spritecollide(self,self.game.blocks, False) 
            if hits: 
                if self.y_change>0: 
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change<0:
                    self.rect.y = hits[0].rect.bottom

    def animate(self): # метод анимации персонажа
        # ниже определяем кадры анимации в 4 стороны
        down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]
        # логика самой анимации 
        if self.facing == 'down':
            # если стоим на месте, то просто установим статичное изображение
            if self.y_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else: 
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 0
        if self.facing == 'up':
            # если стоим на месте, то просто установим статичное изображение
            if self.y_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else: 
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 0
        if self.facing == 'left':
            # если стоим на месте, то просто установим статичное изображение
            if self.x_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else: 
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 0
        if self.facing == 'right':
            # если стоим на месте, то просто установим статичное изображение
            if self.x_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else: 
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 0
                

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

































































































































