import pygame


class Entity:



    def __init__(self, x, y, w, h, c, faction = 0, hp = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.faction = faction
        self.hp = hp
        self.alive = True

    def update(self, entities):
        raise Exception("not implemented")

    def draw(self, screen):
        raise Exception("not implemented")

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def rect_wanted_pos(self, pos):
        return pygame.Rect(pos[0], pos[1], self.w, self.h)

    def on_collision(self, target):
        pass

    def check_collisions(self, entities):
        potential_collisions = [e for e in entities if e != self]
        for candidate in potential_collisions:
            if candidate.rect().colliderect(self.rect()):
                self.on_collision(candidate)

    def center(self):
        return (self.x + self.w / 2, self.y + self.h / 2)

    def is_outside_screen(self):
        screen_w, screen_h = pygame.display.get_surface().get_size()
        return (self.x + self.w < 0
            or self.x > screen_w
            or self.y + self.h < 0
            or self.y > screen_h)

    def hurt(self, dmg):
        pass
