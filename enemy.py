import pygame
import os

#from main import SCREEN_WIDTH

from direction import Direction
from entity import Entity


class Enemy(Entity):

    def __init__(self, x, y, direction=Direction.RIGHT, width=Entity.default_width, height=Entity.default_height):
        Entity.__init__(self, x, y, 3)
        self.direction = direction
        self.set_sprites(type(self).__name__, self.width, self.height)
        self.is_moving = True

    def move(self):
        Entity.move(self)
        if self.x > 600:
            self.direction = Direction.LEFT
        if self.x < 0:
            self.direction = Direction.RIGHT
