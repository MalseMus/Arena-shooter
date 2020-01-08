import pygame


class Entity:



    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.alive = True

    def update(self, entities):
        raise Exception("not implemented")

    def draw(self, screen):
        raise Exception("not implemented")

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


    def on_collision(self, target):
        pass

    def check_collisions(self, entities):
        potential_collisions = [e for e in entities if e != self]
        for candidate in potential_collisions:
            if candidate.rect().colliderect(self.rect()):
                self.on_collision(candidate)

    def center(self):
        return (self.x + self.w / 2, self.y + self.h / 2)