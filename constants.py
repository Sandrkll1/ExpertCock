import json


IS_LOAD = False
WIDTH = 0
HEIGHT = 0
FPS = 0
SPRITE_WIDTH = 0
SPRITE_HEIGHT = 0
HERO_WIDTH = 0
HERO_HEIGHT = 0
FENCE_WIDTH = 0
FENCE_HEIGHT = 0
SPEED = 0
FONT = None


def load():
    global IS_LOAD, WIDTH, HEIGHT, FPS, SPRITE_WIDTH, SPRITE_HEIGHT, HERO_WIDTH, HERO_HEIGHT, FENCE_WIDTH, FENCE_HEIGHT, SPEED, FONT

    if IS_LOAD:
        return

    with open(".\\constants.json", "r", encoding="utf8") as file:
        data = json.load(file)

    WIDTH = data["WIDTH"]
    HEIGHT = data["HEIGHT"]
    FPS = data["FPS"]
    SPRITE_WIDTH = data["SPRITE_WIDTH"]
    SPRITE_HEIGHT = data["SPRITE_HEIGHT"]
    HERO_WIDTH = data["HERO_WIDTH"]
    HERO_HEIGHT = data["HERO_HEIGHT"]
    FENCE_WIDTH = data["FENCE_WIDTH"]
    FENCE_HEIGHT = data["FENCE_HEIGHT"]
    SPEED = data["SPEED"]
    FONT = data["FONT"]
    IS_LOAD = True


load()
