import math
import pygame
from src.weapons.weapon import Weapon
from src.entities.bullet import Bullet


class Rifle(Weapon):

    def __init__(self, parent_faction):
        super().__init__("Rifle", 1000, 5, 50, parent_faction)

    def fire(self, origin):
        if not self.ready():
            return[]
        theta = self.calc_theta(origin)
        bullet = Bullet(origin.x + origin.w / 2, origin.y + origin.h / 2, 2, pygame.Color("white"), self.bullet_v, theta, self.bullet_dmg, self.parent_faction)
        self.reload_timer = self.now()
        return [bullet]
