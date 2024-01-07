import sys
import pygame
from pygame.locals import *
import settings


class TitleScreen:
    def __init__(self):
        # Display some text
        pygame.init()

        self.background = pygame.Surface(settings.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((114, 148, 210))

        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30) / 1000

        settings.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def update(self):
        while settings.state_machine["in_title"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        sys.exit()
                    if event.key == K_b:
                        pygame.mixer.Sound.play(settings.select_sound)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("sounds/title_screen2.wav")
                        pygame.mixer.music.play(-1)
                    if event.key == K_SPACE:
                        pygame.mixer.Sound.play(settings.select_sound)
                        settings.state_machine["in_title"] = False
                        settings.state_machine["in_play"] = True

            self.render()

    def render(self):
        settings.screen.blit(self.background, (0, 0))
        big_font = pygame.font.Font("golem-script.ttf", 96)
        mid_font = pygame.font.Font("golem-script.ttf", 24)
        text = big_font.render("LASER CATS!", 1, (10, 10, 10))

        subtitle = mid_font.render("Press space to continue", 1, (10, 10, 10))

        self.background.blit(text, (345, 204))
        self.background.blit(subtitle, (468, 320))
        self.clock.tick(30)
        pygame.display.flip()
