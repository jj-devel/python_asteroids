import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Variables
        rand_angle = random.uniform(20, 50)
        neg_rand_angle = rand_angle - (rand_angle * 2)
        velocity0 = self.velocity.rotate(rand_angle)
        velocity1 = self.velocity.rotate(neg_rand_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Delete the previous Asteroid. 
        self.kill()
        # If the asteroid is small, just kill it and return. 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Create new smaller, faster asteroids. 
        split_asteroid_0 = Asteroid(self.position.x, self.position.y, radius)
        split_asteroid_0.velocity = velocity0 * 1.2
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        split_asteroid_1.velocity = velocity1 * 1.2
