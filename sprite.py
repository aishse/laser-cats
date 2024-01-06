import pygame
from pygame.locals import *


class Sprite:
    def collides(self, object):
        if (
            self.y + self.height + 8 >= object.y
            and self.y + self.height + 8 <= object.y + object.height
        ):
            if (
                self.x + self.width >= object.x
                and self.x + self.width <= object.x + object.width
            ):
                return True
        return False

    def load_image(self, rect, dimensions=(150, 150)):
        sheet = pygame.image.load("spritesheet.png").convert()

        rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(sheet, (0, 0), rect)
        image.set_colorkey((0, 0, 0))
        image = pygame.transform.scale(image, dimensions)
        return image
