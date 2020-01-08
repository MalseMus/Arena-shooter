import pygame
from src.entities.entity import Entity
from src.weapons.submachine_gun import SubmachineGun
from src.weapons.rifle import Rifle


WEAPON_KEYS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]


class Player(Entity):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, pygame.Color("yellow"))
        self.v = 1
        self.weapons = [Rifle(), SubmachineGun()] + [None] * 7
        self.weapon_idx = 0


    def update(self, entities):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.v
        if keys[pygame.K_a]:
            self.x -= self.v
        if keys[pygame.K_s]:
            self.y += self.v
        if keys[pygame.K_d]:
            self.x += self.v
        for k in WEAPON_KEYS:
            if keys[k]:
                self.weapon_idx = k - pygame.K_1 if self.weapons[k - pygame.K_1] is not None else self.weapon_idx



        if pygame.mouse.get_pressed()[0]:
            bullets = self.weapons[self.weapon_idx].fire(self)
            for b in bullets:
                entities.append(b)

    def draw(self, screen):
        pygame.draw.rect(screen, self.c, self.rect())
