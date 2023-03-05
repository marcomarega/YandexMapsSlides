import pygame
import requests
from pygame import Rect

from UserInterfafce import init, functions, night_theme, run
from UserInterfafce.screen import Screen
from UserInterfafce.screen_elements import TextPlain, ImagePlain


def load_slide(request, filename):
    response = requests.get(request)
    if not response:
        return
    with open(filename, "wb") as file:
        file.write(response.content)


class SlideScreen(Screen):
    def __init__(self, display, intent, extra_theme=None):
        super(SlideScreen, self).__init__(display, intent, extra_theme)

        load_slide("https://static-maps.yandex.ru/1.x/?ll=9.212486,45.593130&z=17&l=sat", "ViaRisorgimento24.png")
        load_slide("https://static-maps.yandex.ru/1.x/?ll=9.648749,45.958463&z=8&l=sat", "TreLaghi.png")
        load_slide("https://static-maps.yandex.ru/1.x/?ll=-74.010176,40.707990&z=15&l=sat", "LowerManhattan.png")
        self.images = [pygame.image.load("ViaRisorgimento24.png"),
                       pygame.image.load("TreLaghi.png"),
                       pygame.image.load("LowerManhattan.png")]
        self.cur = 0

        self.add_element(
            image_plain := ImagePlain(self, Rect(0, 0, self.get_width(), self.get_height()), self.images[self.cur])
        )
        self.image_plain = image_plain

    def push_event(self, event):
        if super(SlideScreen, self).push_event(event):
            return True
        if event.type == pygame.KEYDOWN:
            self.cur = (self.cur + 1) % len(self.images)
            self.image_plain.set_image(self.images[self.cur])


if __name__ == "__main__":
    init((600, 450))
    functions.set_caption("UIPL program")
    run(SlideScreen, night_theme)
