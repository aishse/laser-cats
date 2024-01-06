import pygame
import random
from sprite import Sprite
from pygame.locals import *
from player import bullets
import settings


class Enemy(Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.health = 160
        self.enemy_img = [
            self.load_image(Rect(1024, 0, 256, 256), (100, 100)),
            self.load_image(Rect(768, 0, 256, 256), (100, 100)),
            self.load_image(Rect(0, 256, 256, 256), (100, 100)),
            self.load_image(Rect(256, 256, 253, 256), (100, 100)),
            self.load_image(Rect(512, 256, 256, 256), (100, 100)),
        ]
        self.enemy = random.choice(self.enemy_img)

        if self.x > 600:
            self.direction = -1
        else:
            self.direction = 1
        self.velocity = 10 * self.direction

    def generate_random_img(self):
        self.enemy = random.choice(self.enemy_img)

    def render(self, screen):
        for bullet in bullets:
            if bullet.collides(self):
                self.health -= 8
                pygame.mixer.Sound.play(settings.enemy_hurt_sound)
            if self.health == 0:
                break

        if self.health != 0:
            health_lost = Rect(self.x - 30, self.y - 30, 160, 10)
            health_left = Rect(self.x - 30, self.y - 30, self.health, 10)

            # enemy = Rect(self.x, self.y, self.width, self.height)
            self.width, self.height = self.enemy.get_size()

            enemy = Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, (255, 53, 73), health_lost)
            pygame.draw.rect(screen, (0, 255, 0), health_left)

            screen.blit(self.enemy, enemy)
            # pygame.draw.rect(screen, (255, 128, 128), enemy)
