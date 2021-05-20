import pygame
import os

from direction import Direction
from entity import Entity


class Player(Entity):

    def __init__(self, x, y):
        Entity.__init__(self, x, y, vel=5)
        self.is_moving = False
        self.is_jumping = False
        self.jump_height = 10
        self.jump_count = self.jump_height
        self.direction = Direction.RIGHT
        self.set_sprites(type(self).__name__, self.width, self.height)

    def move(self):
        Entity.move(self)
        if self.is_jumping:
            if self.jump_count >= - self.jump_height:
                direction = 1
                if self.jump_count < 0:
                    direction = -1
                self.y -= (self.jump_count ** 2) * 0.3 * direction
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = self.jump_height