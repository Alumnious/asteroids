from circleshape import CircleShape
from asteroid import Asteroid
import pygame
from constants import LINE_WIDTH, SHOT_RADIUS
class Shot(Asteroid):
    def __init__(self, x, y, adjusted_velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = adjusted_velocity

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt