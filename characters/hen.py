import pygame
from helper import helper
import constants
import random
from .egg import Egg


class Hen(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = helper.get_images("hen path")
        self.pos = 0
        self.image = self.images[self.pos]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(5, 10) * -1
        self.eggs = pygame.sprite.Group()
        self.limit = 0

    def add_egg(self):
        if self.limit >= 80:
            self.eggs.add(Egg(self.eggs, self.rect.x, self.rect.y + self.rect.height, self.speed))
            self.limit = 0

        self.limit += 1

    def update(self):
        if self.pos >= len(self.images):
            self.pos = 0

        self.image = self.images[self.pos]

        self.rect.x += constants.SPEED // 2 * -1
        self.pos += 1

        for egg in self.eggs:
            egg.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Hens(pygame.sprite.Group):
    MAX_HENS = 4

    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, *sprites)

    def update(self, *args, **kwargs):
        if len(self.sprites()) < self.MAX_HENS:
            y = random.randrange(30, 200, 50)
            x = constants.WIDTH + 30 if len(self.sprites()) == 0 else self.sprites()[-1].rect.x + random.randint(300, 500)
            if x < constants.WIDTH:
                x += constants.WIDTH + random.randint(200, 300)

            self.add(Hen(x, y))

        for sprite in self.sprites():
            sprite.update()

            if sprite.rect.x + sprite.rect.width < -constants.WIDTH / 2:
                self.remove(sprite)

    def get_all_eggs(self):
        eggs = []

        for hen in self.sprites():
            eggs.extend(hen.eggs)

        return eggs
