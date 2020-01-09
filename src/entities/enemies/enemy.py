import pygame
from src.entities.entity import Entity


class Enemy(Entity):

    def __init__(self, x, y, w, h, c, hp, weapon):
        super().__init__(x, y, w, h, c, 2, hp)
        self.weapon = weapon

    def update(self, entities):
        if not self.alive:
            return


    def draw(self, screen):
        if not self.alive or self.is_outside_screen():
            return
        pygame.draw.rect(screen, self.c, self.rect())

    def hurt(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
