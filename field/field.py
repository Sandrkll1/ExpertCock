import pygame
import constants
from .background import Background
from characters.cock import Cock
from characters.hen import Hens
from characters.fence import Fence
from helper.TextPrinter import TextPrinter
from helper import helper
import random


class Field:

    MAX_FENCE = 5

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.background = Background(screen)
        self.cock = Cock(200, constants.HEIGHT - 100)
        self.hens = Hens()
        self.fences = pygame.sprite.Group()
        self.isStop = False
        self.score = 0
        self.font_type = None
        self.info = TextPrinter()
        self.egg_sound = helper.get_sound("cock heat sound")
        self.egg_shoot = helper.get_sound("egg heat")

    def reset(self):
        self.cock.reset()
        self.hens = Hens()
        self.fences = pygame.sprite.Group()
        self.isStop = False
        self.score = 0
        self.font_type = None

    def intersects_cock_hen(self):
        [hen.add_egg() for hen in self.hens.sprites()]

    def intersects_cock_egg(self):
        for hen in self.hens.sprites():
            for egg in hen.eggs:
                if self.cock.rect.colliderect(egg.rect):
                    self.cock.health -= 1
                    hen.eggs.remove(egg)
                    self.egg_sound.play()

    def intersects_cock_fence(self):
        for fence in self.fences.sprites():
            if self.cock.rect.colliderect(fence.rect) and fence.isAlive:
                fence.kill()
                self.cock.health -= 1

    def intersects_bullet_egg(self):
        for bullet in self.cock.bullets.sprites():
            for egg in self.hens.get_all_eggs():
                if bullet.intersect(egg):
                    self.score += 1
                    self.egg_shoot.play()

    def add_fences(self):
        while len(self.fences.sprites()) < self.MAX_FENCE:
            if len(self.fences.sprites()) == 0:
                x = constants.WIDTH + random.randint(300, 500)
            else:
                x = self.fences.sprites()[-1].rect.x + random.randint(300, 500)
                if x - self.fences.sprites()[-1].rect.x < 200:
                    x += 100

            self.fences.add(Fence(self.fences, x, constants.HEIGHT - 100))

    def draw_text(self, text, pos, font_color=(255, 255, 255), font_size=20):
        if self.font_type is None:
            self.font_type = pygame.font.Font(constants.FONT, font_size)

        text = self.font_type.render(text, True, font_color)
        self.screen.blit(text, pos)

    def check_health(self):
        if self.cock.health <= 0:
            self.isStop = True

    def update(self, events):
        self.background.update()

        self.hens.update()
        self.add_fences()
        self.fences.update()
        self.intersects_cock_hen()
        self.intersects_cock_egg()
        self.intersects_cock_fence()
        self.intersects_bullet_egg()
        self.cock.update(events)
        self.check_health()
        self.draw()

    def draw(self):
        self.info.draw_text(self.screen, f"Score: {self.score}     HP: {self.cock.health}", (0, 0))
        self.hens.draw(self.screen)
        [hen.eggs.draw(self.screen) for hen in self.hens]
        self.fences.draw(self.screen)
        self.cock.draw(self.screen)
