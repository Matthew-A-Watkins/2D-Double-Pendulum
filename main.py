import pygame
import numpy as np
import sys

import time

class pend():
    def __init__(self, th1, th2, color):

        self.L1 = 100  # length of the first pendulum arm
        self.L2 = 100  # length of the second pendulum arm
        self.M1 = 10   # mass of the first pendulum
        self.M2 = 10   # mass of the second pendulum
        self.G = 9.81  # gravitational constant
        self.dt = .1   # time step

        self.th1 = th1  # initial angle of the first pendulum
        self.th2 = th2  # initial angle of the second pendulum
        self.w1 = 0         # initial angular velocity of the first pendulum
        self.w2 = 0         # initial angular velocity of the second pendulum

        self.color = color # color of pendulum
    def calculate_new_positions(self):

        # calculate the angular accelerations
        num1 = -self.G*(2*self.M1 + self.M2)*np.sin(self.th1) - self.M2*self.G*np.sin(self.th1 - 2*self.th2) - 2*np.sin(self.th1 - self.th2)*self.M2*(self.w2**2*self.L2 + self.w1**2*self.L1*np.cos(self.th1 - self.th2))
        den1 = self.L1*(2*self.M1 + self.M2 - self.M2*np.cos(2*self.th1 - 2*self.th2))
        alpha1 = num1 / den1

        num2 = 2*np.sin(self.th1 - self.th2)*(self.w1**2*self.L1*(self.M1 + self.M2) + self.G*(self.M1 + self.M2)*np.cos(self.th1) + self.w2**2*self.L2*self.M2*np.cos(self.th1 - self.th2))
        den2 = self.L2*(2*self.M1 + self.M2 - self.M2*np.cos(2*self.th1 - 2*self.th2))
        alpha2 = num2 / den2

        # update the angular velocities and angles
        self.w1 = self.w1 + alpha1*self.dt
        self.w2 = self.w2 + alpha2*self.dt
        self.th1 = self.th1 + self.w1*self.dt
        self.th2 = self.th2 + self.w2*self.dt

        return self.th1, self.th2, self.w1, self.w2

    def draw_pendulums(self, screen, th1, th2, L1, L2, color):
        x1 = L1*np.sin(th1)
        y1 = L1*np.cos(th1)
        x2 = x1 + L2*np.sin(th2)
        y2 = y1 + L2*np.cos(th2)

        pygame.draw.line(screen, color, (400, 200), (400 + int(x1), 200 + int(y1)), 2)
        pygame.draw.line(screen, color, (400 + int(x1), 200 + int(y1)), (400 + int(x2), 200 + int(y2)), 2)
        pygame.draw.circle(screen, color, (400, 200), 5)
        pygame.draw.circle(screen, color, (400 + int(x1), 200 + int(y1)), 5)
        pygame.draw.circle(screen, color, (400 + int(x2), 200 + int(y2)), 5)


    def draw(self):
        # calculate the new positions of the pendulums
        th1, th2, w1, w2 = self.calculate_new_positions()
        # draw the pendulums on the screen
        self.draw_pendulums(screen, th1, th2, self.L1, self.L2, self.color)

screen = pygame.display.set_mode((800, 450))

pends = []
a = 0
b = 0
for i in range(100):
    pends.append(pend(np.pi/2+a, np.pi/2+a, (b, int(b*0.5), b*2)))
    if b>=100:
        b = 0
    b+=5
    print(b)
    a+=0.00001

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    # clear screen
    screen.fill((0, 0, 0))


    for p in pends:
        p.calculate_new_positions()
        p.draw()

    # update the screen
    pygame.display.flip()

