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

class Point:

    def __int__(self, x, y, vx, vy, vw, theta):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.vw = vw
        self.theta = theta



class Object:
    def __init__(self, objs:list):
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



def main():
    pygame.init()

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("2D-Physics-Engine")

    clock = pygame.time.Clock()

    while True:
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

            pygame.display.flip()

            clock.tick(60)

        # I hated having to force quit windows when an error appeared
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)


if __name__ == '__main__':
    main()