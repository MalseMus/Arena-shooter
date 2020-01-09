from datetime import datetime

import pygame

from src.entities.enemies.enemy import Enemy
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

    def get_enemy_count(self):
        return len([e for e in self.entities if e.alive and isinstance(e, Enemy)])

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
        x1 = MAP_GAP_W / 2
        x2 = SCREEN_WIDTH / 2
        x3 = SCREEN_WIDTH - MAP_GAP_W / 2
        y1 = MAP_GAP_H / 2
        y2 = SCREEN_HEIGHT / 2
        y3= SCREEN_HEIGHT - MAP_GAP_H / 2

        spawnpoints = [(x1, y1),
                       (x1, y2),
                       (x1, y3),
                       (x2, y1),
                       (x2, y3),
                       (x3, y1),
                       (x3, y2),
                       (x3, y3)]

        minimum_enemy_count = 4
        last_spawn_point_index = 1

        time_started = datetime.now()


        while self.running and player.alive:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw(player)
            pygame.display.flip()
            self.entities = [e for e in self.entities if e.alive]
            enemy_count = self.get_enemy_count()

            if enemy_count < minimum_enemy_count:
                spawn_point = spawnpoints[last_spawn_point_index % len(spawnpoints)]
                last_spawn_point_index += 1
                zombie = Zombie(spawn_point[0], spawn_point[1], player)
                zombie.alive = True
                self.entities.append(zombie)
                enemy_count += 1
                print(f"added enemy. count is now {enemy_count}")
            print(f"total entities: {len(self.entities)}, alive enemies: {enemy_count}")

            self.clock.tick(TARGET_FPS)

        time_survived = (datetime.now() - time_started)
        seconds_survived = int(time_survived.total_seconds())
        print(f"Time Survived: {seconds_survived} seconds")









