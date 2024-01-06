import pygame
from pygame.locals import *

# utility class to get settings for the game
pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
state_machine = {"in_play": False, "in_title": True, "gameover": False, "in_end": False}
score = 0
lives = 0
select_sound = pygame.mixer.Sound("sounds/select.wav")
shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
hurt_sound = pygame.mixer.Sound("sounds/lostlife.wav")
enemy_hurt_sound = pygame.mixer.Sound("sounds/enemyhurt.wav")
game_over_sound = pygame.mixer.Sound("sounds/gameover.wav")
