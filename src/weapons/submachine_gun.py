import pygame
from src.weapons.weapon import Weapon
from src.entities.bullet import Bullet


class SubmachineGun(Weapon):

    def __init__(self, parent_faction):
        super().__init__("Submachine Gun", 100, 4, 20, parent_faction)

    def fire(self, origin):
        if not self.ready():
            return[]
        theta = self.calc_theta(origin)
        bullet = Bullet(origin.x + origin.w / 2, origin.y + origin.h / 2, 2, pygame.Color("white"), self.bullet_v, theta, self.bullet_dmg, self.parent_faction)
        self.reload_timer = self.now()
        return [bullet]