import sys
import os
import pygame


def load_image(fullname, colorkey=None):
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' is not found")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def set_caption(caption):
    pygame.display.set_caption(caption)


def hor_center(screen_width, element_width):
    return (screen_width - element_width) // 2


def ver_center(screen_height, element_height):
    return (screen_height - element_height) // 2


def terminate():
    pygame.quit()
    sys.exit()
