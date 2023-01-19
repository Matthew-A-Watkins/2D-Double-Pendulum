import os
import sys
import numpy as np
import pygame

# GLOBAL VARIABLES
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 1000
HEIGHT = 500


class MyPoint:
    def __init__(self, x, y, vx, vy, vw, theta):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.vw = vw
        self.theta = theta


class Object:
    def __init__(self, objs: list):
        self.objs = objs

    def move(self, vx, vy, vw):
        total_vx = 0
        total_vy = 0
        total_vw = 0

        for obj in self.objs:
            total_vx += obj.vx
            total_vy += obj.vy
            total_vw += obj.vw

        total_vx += vx
        total_vy += vy
        total_vw += vw
    def draw(self, color, surface):
        last_point = None
        for point in self.objs:
            print(last_point, point)
            if last_point is not None:
                print("drawing {} to {}".format(last_point, (point.x, point.y)))
                pygame.draw.line(surface, color, last_point, (point.x, point.y), 5)
            last_point = (point.x, point.y)


def main():
    pygame.init()

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("2D-Physics-Engine")

    clock = pygame.time.Clock()

    while True:
        obj = Object([MyPoint(WIDTH/2, HEIGHT/2, 0, 0, 0, 0), MyPoint(10, 10, 0, 0, 0, 0)])
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        print("EXIT KEY PRESSED")
                        pygame.quit()
                        sys.exit()

            screen.fill(BLACK)

            obj.draw(WHITE, screen)

            pygame.display.flip()

            clock.tick(60)

        # I hated having to force quit windows when an error appeared
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()
