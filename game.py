import pygame

from enemy import Enemy
from player import Player
from projectile import Projectile
from direction import Direction

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360
FPS = 30


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Walking Simulator")
bg = pygame.transform.scale(pygame.image.load("assets/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(x=Player.default_height, y=SCREEN_HEIGHT - Player.default_height)

enemies = []
bullets = []

for i in range(10):
    enemies.append(Enemy(SCREEN_WIDTH + (100*i), SCREEN_HEIGHT - Enemy.default_height))


def redraw_screen():
    screen.fill((124, 181, 222))
    screen.blit(bg, (0, 0))
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    player.draw(screen)
    pygame.display.update()


def start():
    is_running = True
    while is_running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        for enemy in enemies:
            enemy.move()

        for bullet in bullets:
            if SCREEN_WIDTH > bullet.x > 0:
                bullet.move()
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if len(bullets) < Projectile.max_num_on_screen:
                bullets.append(
                    Projectile(round(player.x + player.width // 2), round(player.y + 0.5*player.height // 2), int(player.direction)))

        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.direction = Direction.LEFT
            player.is_moving = True
        elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.width:
            player.direction = Direction.RIGHT
            player.is_moving = True
        else:
            player.is_moving = False

        if keys[pygame.K_UP] and not player.is_jumping:
            player.is_jumping = True

        player.move()
        redraw_screen()


if __name__ == '__main__':
    start()
