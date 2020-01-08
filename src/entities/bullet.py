import math
import pygame
from src.entities.entity import Entity
from src.entities.wall import Wall

class Bullet(Entity):

    def __init__(self, x, y, r, c, v, t):
        super().__init__(x, y, r, r, c)
        self.v = v
        self.t = t
        self.r = r

    def update(self, entities):
        if not self.alive:
            return
        self.check_collisions(entities)
        self.x += math.cos(self.t) * self.v
        self.y += math.sin(self.t) * self.v

    def draw(self, screen):
        if not self.alive:
            return
        pygame.draw.circle(screen, self.c, (int(self.x), int(self.y)), self.r)


    def on_collision(self, target):
        if not self.alive or not target.alive:
            return
        if type(target) == Wall:
            self.alive = False
