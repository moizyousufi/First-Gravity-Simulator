import pygame

class Particle:
    # simple constructor for ball size and position
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 255)
        self.thickness = 5

    # displaying based on object properties into pygame
    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)


