import pygame
from src.entities.entity import Entity


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_FPS = 60




class Game:


    def __init__(self):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        self.screen.fill(pygame.Color("black"))
        for entity in self.entities:
            entity.draw(self.screen)

    def run(self):
        self.running = True
        e = Entity(200, 300, 150, 100, pygame.Color("red"))
        self.entities.append(e)

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(TARGET_FPS)








