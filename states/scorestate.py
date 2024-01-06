import sys
import pygame
from pygame.locals import *
import settings


class ScoreScreen:
    def __init__(self):
        # Display some text
        pygame.init()

        self.background = pygame.Surface(settings.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((101, 125, 214))

        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30) / 1000

        settings.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def update(self):
        while settings.state_machine["in_end"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        sys.exit()
                    if event.key == K_SPACE:
                        pygame.mixer.Sound.play(settings.select_sound)
                        settings.state_machine["in_end"] = False
                        settings.state_machine["in_play"] = True

            self.render()

    def render(self):
        settings.screen.blit(self.background, (0, 0))
        big_font = pygame.font.Font("golem-script.ttf", 96)
        mid_font = pygame.font.Font("golem-script.ttf", 48)
        small_font = pygame.font.Font("golem-script.ttf", 24)
        text = big_font.render("GAME OVER :(", 1, (10, 10, 10))
        score = mid_font.render("Score: " + str(settings.score), 1, (10, 10, 10))
        subtitle = small_font.render(
            "Enter your name for the leaderboard and press space to play again",
            1,
            (10, 10, 10),
        )

        self.background.blit(text, (324, 204))
        self.background.blit(score, (506, 304))

        self.background.blit(subtitle, ((1200 - subtitle.get_width()) / 2, 360))

        self.clock.tick(30)
        pygame.display.flip()
