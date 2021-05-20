import pygame


class Projectile(object):

    default_color = (0, 0, 0)
    max_num_on_screen = 5

    def __init__(self, x, y, facing, radius=2, color=default_color, velocity=8):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = velocity * facing

    def move(self):
        self.x += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
