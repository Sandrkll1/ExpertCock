import pygame

import constants
from helper import helper
import random


class Egg(pygame.sprite.Sprite):

    def __init__(self, group, x, y, dx):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        self.image = helper.get_images("egg path")[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(4, 7)
        self.dx = dx

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.dx

        if self.rect.y > constants.HEIGHT or self.rect.x + self.rect.width < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def kill(self):
        self.group.remove(self)
