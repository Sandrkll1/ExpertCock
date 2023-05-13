import pygame
import sys
import constants
from helper import helper
from field.field import Field
from main_menu.menu import Menu


pygame.init()


class Main:

    def __init__(self):
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("ExpertCock")
        pygame.display.set_icon(pygame.image.load(helper.get_elements("icon")))
        self.clock = pygame.time.Clock()
        self.field = Field(self.screen)
        self.menu = Menu(self.screen, self.clock, self.field)

    def play_music(self):
        pygame.mixer.music.load(helper.get_elements("music"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def run(self):
        self.menu.preview()
        self.menu.menu()
        self.play_music()
        self.field.reset()

        while True:

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    sys.exit(0)

            if self.field.isStop:
                self.menu.menu()

            self.update()
            self.clock.tick(constants.FPS)

    def update(self):
        self.screen.fill((0, 0, 0))
        self.field.update(self.events)
        pygame.display.update()


if __name__ == "__main__":
    Main().run()
