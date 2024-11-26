import pygame as pg
from config import * 
import math
import random


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
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement() 
        self.animate()
        self.collide_enemy() 
        self.rect.x += self.x_change
        self.colide_blocks('x')
        self.rect.y += self.y_change
        self.colide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0

    def movement(self): 
        keys = pg.key.get_pressed() 
        if keys[pg.K_LEFT]:
            for sprite in self.game.all_sprites: 
                sprite.rect.x+=PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pg.K_RIGHT]:
            for sprite in self.game.all_sprites: 
                sprite.rect.x-=PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pg.K_UP]:
            for sprite in self.game.all_sprites: 
                sprite.rect.y+=PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pg.K_DOWN]:
            for sprite in self.game.all_sprites: 
                sprite.rect.y-=PLAYER_SPEED
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

    def animate(self): 
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
        if self.facing == 'down':
            if self.y_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else: 
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 1
        if self.facing == 'up':
            if self.y_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else: 
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 1
        if self.facing == 'left':
            if self.x_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else: 
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 1
        if self.facing == 'right':
            if self.x_change == 0: 
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else: 
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 1
               
    def collide_enemy(self):
        hits = pg.sprite.spritecollide(self,self.game.enemies, False)
        if hits: 
            self.kill() 
            self.game.playing = False 
   
   

class Enemy(pg.sprite.Sprite): # 
    def __init__(self, game,x,y):
        self.game = game
        self._layer = ENEMY_LAYER #
        self.groups = self.game.all_sprites ,self.game.enemies
        pg.sprite.Sprite.__init__(self,self.groups) # 

        self.x = x*TILESIZE 
        self.y = y*TILESIZE 
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.facing = random.choice(['left','right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7,30)
        
        self.x_change = 0 
        self.y_change = 0 

        self.image = self.game.enemy_spritesheet.get_sprite(3,2,self.width,self.height)

        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self): 
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop-=1
            if self.movement_loop<= - self.max_travel:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop+=1
            if self.movement_loop>= self.max_travel:
                self.facing = 'left'
                
    def animate(self):
        left_animations = [self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height)]
        if self.facing == 'left':
            if self.x_change == 0: 
                self.image = self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height)
            else: 
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 1
        if self.facing == 'right':
            if self.x_change == 0: 
                self.image = self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height)
            else: 
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop+=0.1
                if self.animation_loop >=3: 
                    self.animation_loop = 1
        

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

# создаем кнопку
class Button:
    def __init__(self, x,y,width,height,fg,bg,content,fontsize):
        self.font = pg.font.Font('fonts/ofont.ru_Pixel Cyr.ttf',32) # партируем шрифт
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg
        
        self.image = pg.Surface((self.width,self.height)) # создаем поверхность
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.width/2,self.height/2))
        self.image.blit(self.text,self.text_rect)
        
    def is_pressed(self,pos,pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False






























































































































