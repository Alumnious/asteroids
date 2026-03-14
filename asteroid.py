from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            first_rotation = self.velocity.rotate(new_angle)
            second_rotation = self.velocity.rotate(new_angle * -1)
            new_size = self.radius - ASTEROID_MIN_RADIUS
            first_ast= Asteroid(self.position[0],self.position[1],new_size)
            second_ast= Asteroid(self.position[0],self.position[1],new_size)
            first_ast.velocity += first_rotation * 1.2
            second_ast.velocity += second_rotation * 1.2
