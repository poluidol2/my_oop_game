import pygame

import utils
from game_object import GameObject


class Enemy(GameObject):
    def __init__(self, x, y, width, height, speed, enemy_type):
        GameObject.__init__(self, x, y, width, height, speed)
        self.enemy_type = enemy_type
        self.speed = speed

    def draw(self, surface):
        surface.blit(pygame.image.load(utils.get_enemy_image_by_type(self.enemy_type)), (self.x, self.y))


class Brain(Enemy):
    def __init__(self, x, y, width, height, speed):
        Enemy.__init__(self, x, y, width, height, speed, "brain")

    def update(self):
        self.x += self.speed


