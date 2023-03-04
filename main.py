from pygame import Rect

from UserInterfafce import init, functions, run, night_theme
from UserInterfafce.screen import Screen
from UserInterfafce.screen_elements import TextPlain


class HelloWorldScreen(Screen):
    def __init__(self, display, rect, extra_style=None):
        super(HelloWorldScreen, self).__init__(display, rect, extra_style)

        self.add_element(
            TextPlain(self, Rect(5, 5, 150, 50), "Hello UIPL!")
        )


if __name__ == "__main__":
    init()
    functions.set_caption("UIPL program")
    run(HelloWorldScreen, night_theme)
