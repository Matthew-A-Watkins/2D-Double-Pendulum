import sys

import pygame

# GLOBAL VARIABLES
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 1000
HEIGHT = 1000


# instead of using sprite class, I decided that I wanted to go an alternative route with simply using pygame
# as a renderer
class Pendulum:

    def __init__(self, color, window, height=100, width=20, gravity=False):
        self.color = color
        self.height = height
        self.width = width
        self.window = window

        self.x = int(WIDTH / 2) - width/2
        self.y = int(HEIGHT / 2) - height
    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.window, self.color, rect)

    def move(self, new_pos: tuple):
        self.x += new_pos[0]
        self.y += new_pos[1]


def main():
    pygame.init()

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Pendulum")

    clock = pygame.time.Clock()

    pend = Pendulum(WHITE, screen)
    pends = []
    pends.append(pend)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        for obj in pends:
            obj.draw()


        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
