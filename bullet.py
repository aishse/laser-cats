import pygame
from sprite import Sprite
from pygame.locals import *


class Bullet(Sprite):
    def __init__(self, x, y, direction=1):
        self.x = x
        self.y = y
        self.width = 90
        self.height = 50
        self.vel = 80 * direction
        self.image = self.load_image(Rect(512, 0, 253, 252), (self.width, self.height))

    def render(self, screen):
        bullet = Rect(self.x, self.y, self.width, self.height)
        temp_rect = Rect(300, 300, 90, 10)
        screen.blit(self.image, bullet)
        # pygame.draw.rect(screen, (136, 74, 156), bullet)
