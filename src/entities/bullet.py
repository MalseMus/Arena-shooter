import math
import pygame
from src.entities.entity import Entity

class Bullet(Entity):

    def __init__(self, x, y, r, c, v, t, dmg, faction):
        super().__init__(x, y, r, r, c)
        self.v = v
        self.t = t
        self.r = r
        self.dmg = dmg
        self.faction = faction

    def update(self, entities):
        self.alive = not self.is_outside_screen()
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
        if target.faction == 0:
            self.alive = False
            return

        if target.faction != self.faction:
            target.hurt(self.dmg)
            self.alive = False

