from Particle import Particle

import pygame
from pygame.locals import*

import time
from timeit import default_timer as timer

def drawCircle(self):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

# initialization for the GUI
pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Gravity Simulation")

ball = Particle(300, 100, 15)

# initializes physical variables
g = 0.980665
vel = 0.0
totalTime = 0.0
start = 0.0
end = 0.0

while True:
    # begins simulation loop
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # create bouncing effect
    if ball.y == 700 or ball.y > 700:
        ball.y = 700
        vel = vel * -0.5
        totalTime = totalTime * 0.75

    # tracks total time amount taken so far in loop
    totalTime = totalTime + (end - start)
    # kinematic equation to determine velocity after period of acceleration from gravity
    vel = (vel)*(totalTime) + (1/2)*(g)*((totalTime)*(totalTime))
    # time tracker
    start = timer()
    time.sleep(0.000001)
    end = timer()
    # approximates where the ball's y position should be based on previous position and velocity's effect over
    # period of time before acceleration changes the velocity and new timers are created
    ball.y = int(ball.y + vel*(end - start))
    ball.display(screen)
    # refreshes screen
    pygame.display.update()







