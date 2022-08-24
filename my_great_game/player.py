import pygame
import sprites
from collections import defaultdict

from game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, offset):
        GameObject.__init__(self, x, y, width, height, )
        self.offset = offset
        self.moving_left = False
        self.moving_right = False
        self.is_jump = False
        self.animation_count = 0
        self.jump_count = 10
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)

    def draw(self, surface):
        if self.animation_count + 1 >= 30:
            self.animation_count = 0
        if self.moving_left:
            surface.blit(sprites.walkLeft[self.animation_count // 15], (self.x, self.y))
            self.animation_count += 1
        elif self.moving_right:
            surface.blit(sprites.walkRight[self.animation_count // 15], (self.x, self.y))
            print(self.bounds)
            self.animation_count += 1
            print("draw_right")
        elif self.is_jump:
            surface.blit(sprites.playerJump, (self.x, self.y))
        else:
            surface.blit(sprites.playerStand, (self.x, self.y))

    def handle(self, key):

        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        elif key == pygame.K_RIGHT:
            self.moving_right = not self.moving_right

        if key == pygame.K_SPACE and not self.is_jump:
            self.is_jump = True
            print("jump")

    def update(self):

        if self.is_jump:
            if self.jump_count >= -10:
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2) / 2
                else:
                    self.y -= (self.jump_count ** 2) / 2
                self.jump_count -= 1
                print(self.x, self.y)
            else:
                self.is_jump = False
                self.jump_count = 10

        if self.moving_left:
            if self.x > 5:
                self.x -= self.offset
            print("moving_left")

        elif self.moving_right:
            if self.x < 1000 - 5 - self.width:
                self.x += self.offset
            print("moving_right")
            print(self.x, self.y)
        else:
            return

