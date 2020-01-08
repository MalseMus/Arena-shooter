import time
import math
import pygame




class Weapon:

    def __init__(self, name, fire_rate, bullet_v, bullet_dmg, parent_faction):
        self.name = name
        self.fire_rate = fire_rate
        self.bullet_v = bullet_v
        self.bullet_dmg = bullet_dmg
        self.reload_timer = 0
        self.parent_faction = parent_faction


    def fire(self, origin):
        raise Exception("not implemented")

    def calc_theta(self, origin):
        m_pos = pygame.mouse.get_pos()
        delta_x = m_pos[0] - origin.x + origin.w / 2
        delta_y = m_pos[1] - origin.y + origin.w / 2
        return math.atan2(delta_y, delta_x)

    def ready(self):
        time_now = self.now()
        return time_now >= self.reload_timer + self.fire_rate


    def now(self):
        return int(round(time.time() * 1000))