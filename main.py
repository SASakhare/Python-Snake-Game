import pygame
import time
from pygame.locals import *


class Snake:

    def __init__(self, game_screen, bg_color: tuple[int], Height: int, Weight: int):

        self.game_screen = game_screen
        self.block = pygame.image.load("./resources/block.jpg").convert()
        self.x, self.y = 100, 400
        self.bg_color = bg_color
        self.Height, self.Weight = Height, Weight
        self.dir = None

    def draw(self):

        self.game_screen.fill(self.bg_color)
        self.game_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.y -= 5
        self.y = max(self.y, 5)
        self.draw()

    def move_down(self):
        self.y += 5
        self.y = min(self.y, self.Height - 45)
        self.draw()

    def move_left(self):
        self.x -= 5
        self.x = max(self.x, 5)
        self.draw()

    def move_right(self):
        self.x += 5
        self.x = min(self.x, self.Weight - 45)
        self.draw()

    def walk(self):

        if self.dir == "up":
            self.move_up()
        elif self.dir == "down":
            self.move_down()
        elif self.dir == "left":
            self.move_left()
        elif self.dir == "right":
            self.move_right()


class Game:

    def __init__(self, Height: int, Weight: int, bg_color: tuple[int]):

        self.Height, self.Weight = Height, Weight

        pygame.init()

        self.surface = pygame.display.set_mode((self.Weight, self.Height))
        self.surface.fill(bg_color)

        self.snake = Snake(self.surface, bg_color, Height, Weight)
        self.snake.draw()

    def run(self):

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.dir = "up"

                    if event.key == K_DOWN:
                        self.snake.dir = "down"

                    if event.key == K_LEFT:
                        self.snake.dir = "left"

                    if event.key == K_RIGHT:
                        self.snake.dir = "right"

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)


# * game settings  :

Weight, Height = 705, 505
bg_color = (255, 255, 255)


if __name__ == "__main__":

    game = Game(Height, Weight, bg_color)

    game.run()
