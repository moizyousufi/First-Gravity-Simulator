from Particle import Particle

import pygame
from pygame.locals import*

import time
from timeit import default_timer as timer

# initializes physical variables
gravity = 0.980665 # gravity is scaled down for simulation

vel = 0.0
permVel = False # permVel ensures no more movement once ball stops bouncing
permVelThreshold = 3 # threshold for how much velocity at bottom portion before stopping

totalTime = 0.0
start = 0.0
end = 0.0
timeSlept = 0.00001
timeMultiplier = 0.75

shouldChangeDir = True
bounciness = -0.7 # this should be a value between 0 and -1 (exclusive)
                  # higher magnitude vals for more bounce, lower for less
                  # technically works for values outside of this range, but does not follow reality

floor = 700

# starting coordinates
startX = 300
startY = 100
size = 15

isRunning = True

# initialization for the GUI
pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Gravity Simulation")
ball = Particle(startX, startY, size)


# begins simulation loop
while isRunning:
    # begin a default screen fill
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # create bouncing effect
    if ball.y >= floor:
        # we only want to change the direction of the ball if it's already going downward
        if shouldChangeDir:
            vel *= bounciness

            # once we reach threshold in magnitude of velocity, we will activate permVel
            if abs(vel) < permVelThreshold:
                permVel = True

            shouldChangeDir = False
            totalTime *= timeMultiplier # this multiplier only exists to ensure further realism in bouncing
    else:
        # if the ball is no longer touching the floor, it can now change direction again
            # once the ball touches the floor again
        shouldChangeDir = True

    # tracks total time amount taken so far in loop
    # we do this because we want to track the previous frame's data whenever performing
        # our final caclulation for the ball's y positioning
    totalTime += end - start
    # kinematic equation to determine velocity after period of acceleration from gravity
    vel += gravity * totalTime

    # time tracker, which will update this frame's data
    start = timer()
    time.sleep(timeSlept)
    end = timer()

    # if our permVel boolean has activated, then we'll always keep the ball on the floor
    if permVel:
        vel = 0

    # approximates where the ball's y position should be based on previous position and velocity's effect over
        # the period of time before acceleration influences the velocity and new timers are created
    ball.y += vel * (end - start)
    ball.display(screen)

    # refreshes screen for each frame
    pygame.display.update()







