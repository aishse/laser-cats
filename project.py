import pygame
import sys
from pygame.locals import *
from states import titlescreenstate as titles, playstate as play, scorestate as score
import settings

# Initialise screen
pygame.init()


background = pygame.Surface(settings.screen.get_size())
background = background.convert()
background.fill((114, 148, 210))


settings.screen.blit(background, (0, 0))
pygame.display.flip()

pygame.display.set_caption("Laser Cats")
titlestate = titles.TitleScreen()


def main():
    while not settings.state_machine["gameover"]:
        settings.score = 0
        settings.lives = 9

        pygame.mixer.music.load("sounds/title_screen.wav")
        pygame.mixer.music.play(-1)
        titlestate.update()

        pygame.mixer.music.stop()
        # print("switching to playstate")

        pygame.mixer.music.load("sounds/gamesong.wav")
        pygame.mixer.music.play(-1)
        playstate = play.PlayState()
        playstate.rungame()
        pygame.mixer.music.stop()

        pygame.mixer.music.load("sounds/title_screen.wav")
        pygame.mixer.music.play(-1)
        scorestate = score.ScoreScreen()

        mid_font = pygame.font.Font("golem-script.ttf", 48)
        msg = mid_font.render("Check the console!", 1, (10, 10, 10))
        settings.screen.blit(msg, (100, 204))
        pygame.display.flip()

        name = input("Enter username for leaderboard: ")
        write_to_leaderboard(settings.score, name, "leaderboard.txt")
        fetch_leaderboard("leaderboard.txt")
        high_score = get_userscore(name, "leaderboard.txt")
        print("Your high score is: " + str(high_score))

        input("Press any key to continue the game: ")
        print("Go back to the game window!")
        scorestate.update()
        pygame.mixer.music.stop()


# write to a leaderboard
def write_to_leaderboard(score, name, file):
    index = 0
    with open(file, "r+") as fp:
        contents = fp.readlines()
        fp.seek(0)

        for line in fp:
            entry = line.split(":")

            if score < int(entry[1].strip()):
                index += 1
                # print("line " + str(index))

        contents.insert(index, name + ": " + str(score) + "\n")
        fp.seek(0)
        fp.writelines(contents)


def get_userscore(name, file):
    with open(file, "r") as fp:
        for line in fp:
            entry = line.split(":")

            if entry[0] == name:
                return int(entry[1].strip())
    return None


def fetch_leaderboard(file):
    with open(file, "r") as fp:
        for line in fp:
            print(line)


if __name__ == "__main__":
    main()
