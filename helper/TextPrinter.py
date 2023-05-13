import pygame
import constants


class TextPrinter:

    def __init__(self, alpha=100, max_alpha=100, min_alpha=10, da=5):
        self.alpha = alpha
        self.max_alpha = max_alpha
        self.min_alpha = min_alpha
        self.da = da
        self.font_type = None

    def draw_text(self, screen, text, pos, font_type=constants.FONT, font_size=25, font_color=(255, 255, 255)):
        if self.font_type is None:
            self.font_type = pygame.font.Font(font_type, font_size)

        text = self.font_type.render(text, True, font_color)
        screen.blit(text, pos)

    def draw_live_text(self, screen, text, pos, font_type=constants.FONT, font_size=25, font_color=(255, 255, 255), max_alpha=100, min_alpha=10, da=5):
        if self.font_type is None:
            self.font_type = pygame.font.Font(font_type, font_size)

        text = self.font_type.render(text, True, font_color)
        text.set_alpha(self.alpha)
        screen.blit(text, pos)

        if self.alpha > max_alpha:
            self.da = -da
        elif self.alpha <= min_alpha:
            self.da = da

        self.alpha += self.da
