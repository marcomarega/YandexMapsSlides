import pygame

from UserInterfafce.intention import Intent
from UserInterfafce import display


class Screen(pygame.Surface):
    def __init__(self, display, intent, theme):
        super(Screen, self).__init__(display.get_size(), pygame.SRCALPHA, 32)
        self.display = display
        self.intent = intent
        self.theme = theme
        self.theme_src = theme
        self.elements = list()

    def draw(self, tick):
        self.fill((0, 0, 0, 0))
        self.blit(self.theme.data["background"], (0, 0))
        for element in self.elements:
            element.draw(tick)
        self.display.blit(self, (0, 0))

    def push_event(self, event):
        for element in self.elements[::-1]:
            if element.push_event(event):
                return True

    def add_element(self, element):
        self.elements.append(element)

    def set_theme(self, theme):
        self.theme.data = theme.data

    def set_intent(self, intent: Intent):
        self.intent = intent

    def get_mouse_pos(self):
        if self.display == display:
            return pygame.mouse.get_pos()
        return self.display.get_mouse_pos()
