import pygame
import sys
from sprite import Sprite
from pygame.locals import *
from bullet import Bullet
import settings

bullets = []

pygame.init()


def keydown(key):
    keys = pygame.key.get_pressed()
    return keys[key]


class Player(Sprite):
    def __init__(self, window_width, window_height):
        self.x = 500
        self.y = window_height - 300
        self.dy = 0
        self.velocity = 0
        self.acceleration = 0.5
        self.FRICTION = 0.6
        self.GRAVITY = 6
        self.is_firing = False
        self.cooldown_right = 0
        self.cooldown_left = 0
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30) / 1000

        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height
        self.b = Bullet(self.x + 50, self.y)
        self.player_images = [
            self.load_image(Rect(0, 0, 256, 256), (150, 150)),
            self.load_image(Rect(256, 0, 250, 256), (150, 150)),
        ]
        self.cur_player_image = self.player_images[0]
        self.width, self.height = self.cur_player_image.get_size()

    def update(self, dt):
        if keydown(K_d):
            self.velocity = 20
            self.velocity = self.velocity + self.acceleration
        if keydown(K_a):
            self.velocity = 20
            self.velocity = -1 * (self.velocity + self.acceleration)
        if keydown(K_SPACE):
            self.dy = -10
        if keydown(K_RIGHT):
            bullets.append(Bullet(self.x + 10, self.y + self.width / 8))
            if int(self.cooldown_right) == 0:
                self.cooldown_right = 1.8
                pygame.mixer.Sound.play(settings.shoot_sound)
        if keydown(K_LEFT):
            bullets.append(Bullet(self.x + 10, self.y + self.width / 8, -1))
            if int(self.cooldown_left) == 0:
                self.cooldown_left = 1.8
                pygame.mixer.Sound.play(settings.shoot_sound)
        if keydown(K_q):
            sys.exit()

        if self.cooldown_right > 0:
            self.cooldown_right -= dt
        if self.cooldown_left > 0:
            self.cooldown_left -= dt
        for bullet in bullets:
            if (
                bullet.x + bullet.width > 0
                and bullet.x + bullet.width < self.WINDOW_WIDTH
            ):
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        self.dy = self.dy + self.GRAVITY * dt
        self.y += self.dy
        self.x += self.velocity
        self.velocity *= self.FRICTION

    def render(self, screen):
        self.width, self.height = self.cur_player_image.get_size()

        player = Rect(self.x, self.y, self.width, self.height)

        self.cur_player_image = self.player_images[0]
        for bullet in bullets:
            self.cur_player_image = self.player_images[1]
            bullet.render(screen)

        screen.blit(self.cur_player_image, player)
        # pygame.draw.rect(screen, (136, 74, 156), player)
