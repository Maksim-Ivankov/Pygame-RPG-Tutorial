import pygame as pg
from config import * 
import math
import random


class Player(pg.sprite.Sprite): # класс наследуется от Sprite - значительно упростит создание спрайтов
    def __init__(self, game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER # на какаом слое экрана должен отображаться спрайт, например трава, потом вода, потом спрайт
        self.groups = self.game.all_sprites # объект всех спрайтов на уровень выше
        pg.sprite.Sprite.__init__(self,self.groups) # хуй знает что это

        self.x = x*TILESIZE 
        self.y = y*TILESIZE 
        self.width = TILESIZE
        self.height = TILESIZE

        # пока игрок будет просто квадратом
        self.image = pg.Surface([self.width,self.height])
        self.image.fill(RED) # заливаем в красный

        self.rect = self.image.get_rect() # создаем хитбокс
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        pass

















































































































































