import pygame
from helper import helper
import os
import constants
from copy import copy


class Background:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.backgrounds = []
        self.get_backgrounds()
        self.bg_pos = 0
        self.current_bg = self.backgrounds[self.bg_pos]
        self.next_bg = self.backgrounds[self.bg_pos + 1]

    def get_backgrounds(self):
        path = helper.get_elements("background path")
        paths = os.listdir(path)

        x = 0
        for img in paths:
            pth = f"{path}\\{img}"
            if os.path.isfile(pth):
                image = pygame.transform.scale(pygame.image.load(pth), (constants.WIDTH+10, constants.HEIGHT))
                temp = {"image": image, "x": x, "y": 0}
                self.backgrounds.append(temp)
                x += constants.WIDTH

        if len(self.backgrounds) <= 1:
            back = copy(self.backgrounds[0])
            back["x"] += constants.WIDTH
            self.backgrounds.append(back)

    def update(self):

        for bg in enumerate(self.backgrounds):
            back = bg[1]

            self.screen.blit(back["image"], (back["x"], back["y"]))

            back["x"] += constants.SPEED * -1

            if back["x"] + constants.WIDTH <= 0:
                if bg[0] + 1 >= len(self.backgrounds):
                    pos = 0
                else:
                    pos = bg[0] + 1

                back["x"] = self.backgrounds[pos]["x"] + constants.WIDTH
