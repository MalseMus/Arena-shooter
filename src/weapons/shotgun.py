import random
import pygame
from src.weapons.weapon import Weapon
from src.entities.bullet import Bullet


class Shotgun(Weapon):

    def __init__(self):
        super().__init__("Shotgun", 2000, 5)
        self.spread = 45 * 3.1415 / 180
        self.bullet_count = 5

    def fire(self, origin):
        if not self.ready():
            return[]
        theta = self.calc_theta(origin)
        t_min = theta - self.spread / 2
        t_max = theta + self.spread / 2
        bullets = []
        for i in range(0, self.bullet_count):
            r_theta = random.uniform(t_min, t_max)
            bullet = Bullet(origin.x + origin.w / 2, origin.y + origin.h / 2, 2, pygame.Color("white"), self.bullet_v, r_theta)
            bullets.append(bullet)
        self.reload_timer = self.now()
        return bullets
