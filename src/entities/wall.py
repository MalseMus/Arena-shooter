import pygame
from src.entities.entity import Entity



class Wall(Entity):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, pygame.Color("red"))


    def update(self, entities):
        if not self.alive:
            return

    def draw(self, screen):
        if not self.alive:
            return
        pygame.draw.rect(screen, self.c, self.rect())


