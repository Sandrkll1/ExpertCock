import pygame
import constants
import sys
from helper import helper
from helper.TextPrinter import TextPrinter
from characters.hen import Hens


class Menu:

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, field):
        self.screen = screen
        self.clock = clock
        self.field = field
        self.hens = Hens()

    def preview(self):
        alpha = 0
        image = pygame.transform.scale(pygame.image.load(".\\sources\preview\Preview.jpg"), (constants.WIDTH, constants.HEIGHT))
        while alpha != 50:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            image.set_alpha(alpha)
            alpha += 1
            self.screen.blit(image, (0, 0))
            pygame.display.update()
            self.clock.tick(20)

    def menu(self):
        image = helper.get_images("background path", constants.WIDTH, constants.HEIGHT)[0]
        start = TextPrinter()

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.field.reset()
                    self.field.cock.events = events
                    self.field.cock.jump()
                    return

            self.screen.blit(image, (0, 0))
            self.field.cock.peck(self.screen)
            self.hens.update()
            self.hens.draw(self.screen)
            start.draw_live_text(self.screen, "Нажми пробел чтобы играть", (constants.WIDTH // 4, constants.HEIGHT//2), max_alpha=200, min_alpha=50)

            pygame.display.update()
            self.clock.tick(20)
