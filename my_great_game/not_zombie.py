import pygame

from game import Game
import config
import sprites
from player import Player
from brain import Brain
import random


class NotZombie(Game):
    def __init__(self):
        Game.__init__(self, 'Not assets', config.screen_width, config.screen_height, sprites.background_image, config.frame_rate)
        self.create_objects()
        self.timer = 0

    def create_objects(self):
        self.create_player()

    def event_generator(self):
        self.timer += 1

        if self.timer == 30:
            rnd = random.randint(0, 100)
            if rnd > 50:
                self.create_brain_low()
                self.timer = 0
            if rnd < 30:
                self.create_brain_high()
            self.timer = 0


    def create_player(self):
        player = Player(50, 350, 80, 110, 5)
        self.keydown_handlers[pygame.K_LEFT].append(player.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(player.handle)
        self.keydown_handlers[pygame.K_SPACE].append(player.handle)
        self.keyup_handlers[pygame.K_LEFT].append(player.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(player.handle)
        self.keyup_handlers[pygame.K_SPACE].append(player.handle)
        self.objects.append(player)
        self.player = player

    def watcher(self):
        for elem in self.objects:
            if isinstance(elem, Brain):
                if elem.x > 1000:
                    self.objects.pop(self.objects.index(elem))
                if self.player.x + 80 > elem.x > self.player.x and self.player.y + 110 > elem.y > self.player.y:
                    self.objects.pop(self.objects.index(elem))
                    self.game_over = True

    def create_brain_low(self):
        brain = Brain(0, 300, 50, 50, 10)
        self.objects.append(brain)

    def create_brain_high(self):
        brain = Brain(0, 390, 50, 50, 5)
        self.objects.append(brain)


def main():
    NotZombie().run()


if __name__ == '__main__':
    main()
