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
HEIGHT = 1000


# instead of using sprite class, I decided that I wanted to go an alternative route with simply using pygame
# as a renderer
class Pendulum:

    # everything is in SI units (kg, Meters, seconds...)
    def __init__(self, color, window, height=100, width=2, gravity=True, mass=5, angle=0, omega=0):
        self.color = color
        self.height = height
        self.width = width
        self.window = window
        self.angle = angle
        self.mass = mass
        self.omega = omega
        self.gravity = gravity
        self.cm = (0, 0)
        self.vx = 0
        self.vy = 0
        self.x = int(WIDTH / 2) - width/2
        self.y = int(HEIGHT / 2) - height
        self.end_pos_x = 0
        self.end_pos_y = 0
    def draw(self):

        self.end_pos_x = self.x + self.height * np.sin(self.angle*2*np.pi)
        self.end_pos_y = self.y + self.height * np.cos(self.angle * 2 * np.pi)

        # i am lazy
        self.check_bounds(self.end_pos_x, self.end_pos_y, self.x, self.y)


        pygame.draw.line(self.window, self.color, (self.x, self.y),
                         (self.end_pos_x, self.end_pos_y), self.width)

        # CM
        dx = self.x + self.height * np.sin(self.angle*2*np.pi)/2
        dy = self.y + self.height * np.cos(self.angle * 2 * np.pi)/2
        self.cm = (dx, dy)
        pygame.draw.circle(self.window, RED, (dx, dy), self.width*2)

    def move(self, new_pos: tuple = (0, 0)):
        self.x += new_pos[0] + self.vx
        self.y += new_pos[1] + self.vy

    def rotate(self, angle_addition: float = 0):
        if not self.check_bounds(self.end_pos_x, self.end_pos_y, self.x, self.y):
            self.angle += angle_addition + self.omega

    def check_bounds(self, ex, ey, x, y):
        out_of_bounds = 0

        if self.y >= HEIGHT-self.height:
            self.y = HEIGHT-self.height
            out_of_bounds += 1
        elif y <= 0-self.height:
            self.y = 0-self.height
            out_of_bounds += 1

        if self.x >= WIDTH-self.width:
            self.x = WIDTH-self.width
            out_of_bounds += 1

        elif self.x <= 0-self.height:
            self.x = 0-self.height
            out_of_bounds += 1

        if self.end_pos_y >= HEIGHT+self.height:
            self.end_pos_y = HEIGHT+self.height
            out_of_bounds += 1

        elif self.end_pos_y <= 0-self.height:
            self.end_pos_y = 0-self.height
            out_of_bounds += 1

        if self.end_pos_x >= WIDTH-self.width:
            self.end_pos_x = WIDTH-self.width
            out_of_bounds += 1

        elif self.end_pos_x <= 0+self.width:
            self.end_pos_x = 0+self.width
            out_of_bounds += 1

        return out_of_bounds >= 2
def main():
    pygame.init()

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Pendulum")

    clock = pygame.time.Clock()

    pend = Pendulum(WHITE, screen)
    pends = [pend]

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        pygame.quit()
                        sys.exit()


            screen.fill(BLACK)
            #for obj in pends:
            pend.rotate(0.01)
            print(pend.angle)

            for obj in pends:
                obj.move((3, 3))
            for obj in pends:
                obj.draw()


            pygame.display.flip()
            clock.tick(60)

        # I hated having to force quit windows when an error appeared
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)


if __name__ == '__main__':
    main()