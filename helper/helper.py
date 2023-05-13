import pygame
import json
import constants
import os
import os.path

pygame.mixer.init()


def get_elements(el):
    with open("./config.json", "r", encoding="utf8") as file:
        data = json.load(file)

    return os.getcwd() + data.get(el)


def get_images(el, width=constants.SPRITE_WIDTH, height=constants.SPRITE_HEIGHT):
    images = []

    path = get_elements(el)
    paths = os.listdir(path)

    for file in paths:
        file = f"{path}\\{file}"
        if os.path.isfile(file):
            image = pygame.image.load(file)
            image = pygame.transform.scale(image, (width, height))
            images.append(image)

    return images


def get_sound(sound):
    return pygame.mixer.Sound(get_elements(sound))
