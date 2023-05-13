import pygame
import random
import constants
from helper import helper
import math


class Cock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = 0
        self.images = helper.get_images("cock path", constants.HERO_WIDTH, constants.HERO_HEIGHT)
        self.ready_image = helper.get_images("cock ready path", constants.HERO_WIDTH, constants.HERO_HEIGHT)[0]
        self.pecks_img = helper.get_images("cock peck path", constants.HERO_WIDTH, constants.HERO_HEIGHT)
        self.image = self.images[self.pos]
        self.rect = self.image.get_rect(center=(x, y))
        self.isJump = False
        self.max_jump = 10
        self.jumpCount = self.max_jump
        self.health = 5
        self.bullets = pygame.sprite.Group()
        self.events = None
        self.shoot_sound = helper.get_sound("cock shoot")
        self.jump_sound = helper.get_sound("jump")

    def reset(self):
        self.pos = 0
        self.health = 5
        self.bullets = pygame.sprite.Group()
        self.events = None

    def peck(self, screen):
        self.pos = random.randint(0, len(self.pecks_img) - 1)
        self.image = self.pecks_img[self.pos]
        screen.blit(self.image, self.rect)

    def update(self, events=None):
        self.events = events
        self.bullets.update()
        self.jump()
        self.shoot()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    self.health += 1000

        if self.pos >= len(self.images):
            self.pos = 0

        self.image = self.images[self.pos]

        if self.isJump:
            return

        self.pos += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        [bullet.draw(screen) for bullet in self.bullets.sprites()]

    def jump(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.isJump = True
                    self.jump_sound.play()

        if self.isJump:
            if self.jumpCount >= self.max_jump * -1:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2

                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.max_jump

    def shoot(self):

        if self.events is None:
            return

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                mouse_x, mouse_y = pygame.mouse.get_pos()

                distance_x = mouse_x - self.rect.x
                distance_y = mouse_y - self.rect.y

                angle = math.atan2(distance_y, distance_x)
                speed_x = math.cos(angle)
                speed_y = math.sin(angle)

                if speed_x < 0 or speed_y > 0:
                    return

                self.bullets.add(Bullet(self.bullets, self.rect.x + self.rect.w // 2, self.rect.y, speed_x, speed_y, angle))
                self.shoot_sound.play()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, group: pygame.sprite.Group, x, y, dx, dy, angle):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        self.dx = dx
        self.dy = dy
        self.speed = 10
        self.width = 50
        self.height = 50
        self.image = pygame.transform.rotate(helper.get_images("grain", self.width, self.height)[0], angle*100)
        self.rect = pygame.rect.Rect(x, y, self.width, self.height)

    def update(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

        if self.rect.x > constants.WIDTH or self.rect.y < 0:
            self.group.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def intersect(self, obj):
        if self.rect.colliderect(obj.rect):
            self.group.remove(self)
            obj.kill()
            return True
        return False
