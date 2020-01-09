import pygame
from src.entities.enemies.enemy import Enemy


class Zombie(Enemy):

    def __init__(self, x, y, player):
        super().__init__(x, y, 20, 30, pygame.Color("Green"), 100, None, player, 2)
