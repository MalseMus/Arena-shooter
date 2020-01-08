import pygame


class Entity:



    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def update(self):
        raise Exception("not implemented")

    def draw(self, screen):
        raise Exception("not implemented")

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
