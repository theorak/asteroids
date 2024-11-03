import pygame
import circleshape
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50) # new angle of direction
            vector1 = self.velocity.rotate(random_angle) # in opposite direction
            vector2 = self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS # step down size

            Asteroid(self.position.x, self.position.y, radius).velocity = vector1 * 1.2
            Asteroid(self.position.x, self.position.y, radius).velocity = vector2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt