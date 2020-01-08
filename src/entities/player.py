import pygame
from src.entities.entity import Entity
from src.weapons.submachine_gun import SubmachineGun
from src.weapons.rifle import Rifle
from src.weapons.shotgun import Shotgun
from src.entities.wall import Wall


WEAPON_KEYS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]


class Player(Entity):

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, pygame.Color("yellow"))
        self.v = 5
        self.weapons = [Rifle(), SubmachineGun(), Shotgun()] + [None] * 6
        self.weapon_idx = 0


    def update(self, entities):
        if not self.alive:
            return
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
        self.check_collisions(entities)

        if pygame.mouse.get_pressed()[0]:
            bullets = self.weapons[self.weapon_idx].fire(self)
            for b in bullets:
                entities.append(b)

    def draw(self, screen):
        if not self.alive:
            return
        pygame.draw.rect(screen, self.c, self.rect())

    def on_collision(self, target):
        if not self.alive or not target.alive:
            return
        if type(target) == Wall:
            my_center = self.center()
            target_center = target.center()
            keys = pygame.key.get_pressed()

            if my_center[0] < target_center[0] and keys[pygame.K_d]:
                if self.x + self.w > target.x:
                    self.x -= self.v
            if my_center[0] > target_center[0] and keys[pygame.K_a]:
                if self.x < target.x + target.w:
                    self.x += self.v
            if my_center[1] < target_center[1] and keys[pygame.K_s]:
                if self.y + self.h > target.y:
                    self.y -= self.v
            if my_center[1] > target_center[1] and keys[pygame.K_w]:
                if self.y < target.y + target.h:
                    self.y += self.v