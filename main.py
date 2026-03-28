import pygame
import time
from pygame.locals import *

SIZE = 40


class Apple:

    def __init__(self, game_screen):

        self.apple = pygame.image.load("./resources/apple.jpg")
        self.game_screen = game_screen

        self.x, self.y = SIZE * 3, SIZE * 3  # * should be multiple of 40

    def draw(self):

        self.game_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


class Snake:

    def __init__(
        self, game_screen, bg_color: tuple[int], Height: int, Weight: int, length: int
    ):

        self.length = length
        self.game_screen = game_screen
        self.block = pygame.image.load("./resources/block.jpg").convert()
        self.x, self.y = [SIZE] * self.length, [SIZE] * self.length
        self.bg_color = bg_color
        self.Height, self.Weight = Height, Weight
        self.dir = None
        self.delta = 40

    def draw(self):

        self.game_screen.fill(self.bg_color)
        for x, y in zip(self.x, self.y):
            self.game_screen.blit(self.block, (x, y))
        pygame.display.flip()

    def move_up(self):
        self.y[0] -= self.delta
        self.y[0] = max(self.y[0], 5)
        self.draw()

    def move_down(self):
        self.y[0] += self.delta
        self.y[0] = min(self.y[0], self.Height - 45)
        self.draw()

    def move_left(self):
        self.x[0] -= self.delta
        self.x[0] = max(self.x[0], 5)
        self.draw()

    def move_right(self):
        self.x[0] += self.delta
        self.x[0] = min(self.x[0], self.Weight - 45)
        self.draw()

    def walk(self):

        for i in range(self.length - 1, 0, -1):

            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

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

        self.snake = Snake(self.surface, bg_color, Height, Weight, 10)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):

        self.snake.walk()
        self.apple.draw()

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

            self.play()
            time.sleep(0.5)


# * game settings  :

Weight, Height = 705, 505
bg_color = (255, 255, 255)


if __name__ == "__main__":

    game = Game(Height, Weight, bg_color)

    game.run()
