import pygame
import os

from direction import Direction


class Entity(object):
    default_width = 64
    default_height = 64

    sprites_walk_right = []
    sprites_walk_left = []

    def __init__(self, x, y, vel, jump_height=0, width=default_width, height=default_height):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.height = height
        self.is_moving = False
        self.is_jumping = False

        self.step_count = 0

    def set_sprites(self, name, width, height):
        self.sprites_walk_right = [
            pygame.transform.scale(pygame.image.load(os.path.join('assets', name, 'R1.png')), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets', name, 'R2.png')), (width, height)),
        ]
        self.sprites_walk_left = [
            pygame.transform.scale(pygame.image.load(os.path.join('assets', name, 'L1.png')), (width, height)),
            pygame.transform.scale(pygame.image.load(os.path.join('assets', name, 'L2.png')), (width, height)),
        ]

    def move(self):
        if self.is_moving:
            self.x += self.vel * int(self.direction)
            self.step_count += 1

    def draw(self, screen):
        if self.is_jumping:
            if self.direction == Direction.LEFT:
                screen.blit(self.sprites_walk_left[0], (self.x, self.y))
            elif self.direction == Direction.RIGHT:
                screen.blit(self.sprites_walk_right[0], (self.x, self.y))
        else:
            if self.direction == Direction.LEFT:
                screen.blit(self.sprites_walk_left[(self.step_count // 3) % 2], (self.x, self.y))
            elif self.direction == Direction.RIGHT:
                screen.blit(self.sprites_walk_right[(self.step_count // 3 % 2)], (self.x, self.y))
