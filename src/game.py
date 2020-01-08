import pygame
from src.entities.player import Player
from src.entities.wall import Wall
from src.entities.enemies.zombie import Zombie

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_FPS = 60
PLAYER_DEF_WIDTH = 20
PLAYER_DEF_HEIGHT = 30
MAP_GAP_W = 100
MAP_GAP_H = 60
BOX_W = (SCREEN_WIDTH - 4 * MAP_GAP_W) / 2
BOX_H = (SCREEN_HEIGHT - 4 * MAP_GAP_H) / 2



class Game:


    def __init__(self):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.entities = []
        self.hud_font = pygame.font.Font(None, 18)

    def update(self):
        for entity in self.entities:
            entity.update(self.entities)

    def draw(self, player):
        self.screen.fill(pygame.Color("black"))
        for entity in self.entities:
            entity.draw(self.screen)
        self.draw_hud(player)


    def draw_hud(self, player):
        weapon_surface = self.hud_font.render(player.weapons[player.weapon_idx].name, False, pygame.Color("white"))
        self.screen.blit(weapon_surface, (0, 0))


    def run(self):
        self.running = True
        player_start_x = SCREEN_WIDTH / 2 - PLAYER_DEF_WIDTH / 2
        player_start_y = SCREEN_HEIGHT / 2 - PLAYER_DEF_HEIGHT / 2
        player = Player(player_start_x, player_start_y, PLAYER_DEF_WIDTH, PLAYER_DEF_HEIGHT)
        self.entities.append(player)
        self.entities.append(Wall(MAP_GAP_W, MAP_GAP_H, BOX_W, BOX_H))
        self.entities.append(Wall(3 * MAP_GAP_W + BOX_W, MAP_GAP_H, BOX_W, BOX_H))
        self.entities.append(Wall(3 * MAP_GAP_W + BOX_W, 3 * MAP_GAP_H + BOX_H, BOX_W, BOX_H))
        self.entities.append(Wall(MAP_GAP_W, 3 * MAP_GAP_H + BOX_H, BOX_W, BOX_H))
        self.entities.append(Zombie(10, 10))

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw(player)
            pygame.display.flip()
            self.entities = [e for e in self.entities if e.alive]
            self.clock.tick(TARGET_FPS)








