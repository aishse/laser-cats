import sys
import pygame
import random
from pygame.locals import *
from player import Player
from enemy import Enemy
import settings


pygame.init()


class PlayState:
    def __init__(self):
        self.enemies = []
        self.collided = False

        self.timer, self.time = 0, random.randint(2, 4)
        self.health_timer = self.time
        self.p = Player(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        self.e = Enemy(100, 100)
        self.ground = Rect(
            0, settings.WINDOW_HEIGHT - 100, settings.WINDOW_WIDTH + 200, 100
        )
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30) / 1000

        self.font = pygame.font.Font("golem-script.ttf", 28)

        # Fill background
        self.background = pygame.Surface(settings.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((135, 184, 118))

        # blit/render everything to the screen
        settings.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def rungame(self):
        while settings.state_machine["in_play"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if settings.lives < 0:
                pygame.mixer.Sound.play(settings.select_sound)
                settings.state_machine["in_play"] = False
                settings.state_machine["in_end"] = True

            if self.p.collides(self.ground):
                self.p.dy = 0
                self.p.y = self.ground.y - self.p.height - 4
            else:
                self.p.dy = self.p.dy + 6 * self.dt

            self.timer += self.dt

            for enemy in self.enemies:
                if (
                    enemy.direction == -1
                    and enemy.x - 20 <= self.p.x + self.p.width
                    and enemy.x < settings.WINDOW_WIDTH - enemy.width
                ) or (
                    enemy.direction == 1
                    and enemy.x + 20 >= self.p.x
                    and enemy.x > enemy.width
                ):
                    enemy.velocity = 0
                    if (
                        self.p.y >= enemy.y - 30
                        and self.p.y <= enemy.y - 30 + enemy.width
                        and int(self.health_timer) == 0
                    ):
                        pygame.mixer.Sound.play(settings.hurt_sound)
                        self.health_timer = 5
                        settings.lives -= 1

                else:
                    enemy.x += enemy.velocity
            if self.health_timer > 0:
                self.health_timer -= self.dt
            # settings.lives -= 1
            # print(self.health_timer)
            # print(int(self.health_timer))

            if int(self.timer) == self.time:
                self.spawn_enemy()
                self.timer = 0
                self.time = random.randint(2, 4)
                # print("new spawntime: " + str(self.time))

            self.p.update(self.dt)
            self.render()

    def spawn_enemy(self):
        ypos = random.randint(50, settings.WINDOW_HEIGHT - 200)
        xpos = random.choice([settings.WINDOW_WIDTH, -300])
        e = Enemy(xpos, ypos)
        for enemy in self.enemies:
            if enemy.collides(e):
                while not enemy.collides(e):
                    e.y = random.randint(100, settings.WINDOW_HEIGHT - 300)
        e.generate_random_img()
        if len(self.enemies) <= 2:
            self.enemies.append(e)

    def render(self):
        settings.screen.blit(self.background, (0, 0))
        for enemy in self.enemies:
            if enemy.health <= 0:
                self.enemies.pop(self.enemies.index(enemy))
                settings.score += 1
            else:
                enemy.render(settings.screen)
        score_text = self.font.render("Score: " + str(settings.score), 1, (10, 10, 10))
        health_text = self.font.render(
            "Cooldown: " + str(int(self.health_timer)), 1, (10, 10, 10)
        )
        lives_text = self.font.render("Lives: " + str(settings.lives), 1, (10, 10, 10))
        self.p.render(settings.screen)
        pygame.draw.rect(settings.screen, (38, 131, 80), self.ground)

        settings.screen.blit(score_text, (20, 20))
        if settings.lives >= 0:
            settings.screen.blit(lives_text, (20, 60))

        settings.screen.blit(health_text, (20, 100))
        self.clock.tick(30)

        pygame.display.flip()
