import pygame
from helper import helper
import constants

fence_sound = pygame.mixer.Sound(helper.get_sound("fence heat"))


class Fence(pygame.sprite.Sprite):

    def __init__(self, groups, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.groups = groups
        self.image = helper.get_images("fence path", constants.FENCE_WIDTH, constants.FENCE_HEIGHT)[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.isAlive = True

    def kill(self):
        if self.isAlive:
            self.image = pygame.transform.rotate(self.image, 60)
            fence_sound.play()
        self.isAlive = False

    def update(self):
        self.rect.x += constants.SPEED * -1

        if self.rect.x + self.rect.width < 0:
            self.remove(self.groups)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
