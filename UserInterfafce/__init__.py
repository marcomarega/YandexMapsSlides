import pygame

from .functions import load_image
from .intention import Intent


def init():
    pygame.init()


def run(start_screen):
    intent = Intent()
    from .themes import day_theme
    cur_screen = start_screen(display, intent, Theme(day_theme.data))

    running = True
    while running:
        if intent.has_intention:
            cur_screen = intent.get_screen(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                cur_screen.push_event(event)
        display.fill((0, 0, 0))
        cur_screen.draw(clock.tick(FPS))
        pygame.display.flip()


FPS = 60
clock = pygame.time.Clock()
SIZE = WIDTH, HEIGHT = 1200, 700
display = pygame.display.set_mode(SIZE)
from .themes import *

SCROLL_SHIFT = 25

pygame.display.set_caption("UIPL program")
BACKTOGAMESCREEN = pygame.USEREVENT + 1
