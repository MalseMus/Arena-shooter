import math
import pygame
from src.entities.entity import Entity
from src.entities.player import Player


class Enemy(Entity):

    def __init__(self, x, y, w, h, c, hp, weapon, player, v=1):
        super().__init__(x, y, w, h, c, 2, hp)
        self.weapon = weapon
        self.player = player
        self.v = v

    def update(self, entities):
        if not self.alive:
            return
        pos = self.wanted_position()
        collided = self.does_collide(entities=entities, wanted_pos=pos)
        if collided:
            return
        self.move(pos[0], pos[1])


    def draw(self, screen):
        if not self.alive or self.is_outside_screen():
            return
        pygame.draw.rect(screen, self.c, self.rect())

    def hurt(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False

    def wanted_position(self):
        t = self.calc_theta()
        x = self.x + math.cos(t) * self.v
        y = self.y + math.sin(t) * self.v
        return x, y

    def calc_theta(self):
        delta_x = self.player.x - self.x + self.w / 2
        delta_y = self.player.y - self.y + self.w / 2
        return math.atan2(delta_y, delta_x)

    def move(self, x, y):
        self.x = x
        self.y = y

    def does_collide(self, entities, wanted_pos):
        potential_collisions = [e for e in entities if e != self]
        for candidate in potential_collisions:
            if candidate.rect().colliderect(self.rect_wanted_pos(pos=wanted_pos)):
                if type(candidate) == Player:
                    self.player.hurt(5)
                return True
        return False
