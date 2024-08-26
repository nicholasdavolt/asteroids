import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(split_angle)
        vector2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        asteroid1 = Asteroid(x, y, new_radius)
        asteroid2 = Asteroid(x, y, new_radius)

        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2


    