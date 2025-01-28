import pygame

from materials.Button import Button
from materials.Slider import Slider


class Choice_color_menu:
    def __init__(self):
        self.RGB = [Slider(0.15, 0.05, (0.4, 0.1), 0, 255, 0, (255, 0, 0)),
                    Slider(0.15, 0.15, (0.4, 0.1), 0, 255, 0, (0, 255, 0)),
                    Slider(0.15, 0.25, (0.4, 0.1), 0, 255, 0, (0, 0, 255))]
        self.move = [0, 0, 0]
        self.drawing = [False, False, False]
        self.OK = Button(0.3, 0.35, (0.2, 0.05), 'Выбрать')

    def draw(self, screen):
        pygame.draw.rect(screen, (95, 60, 125),
                         ((int(screen.get_width() * 0.1)),
                          (int(screen.get_height() * 0.025)),
                          (int(screen.get_width() * 0.575) + int(screen.get_height() * 0.2)),
                          (int(screen.get_height() * 0.4))))
        for slider in self.RGB:
            slider.draw(screen)
        pygame.draw.rect(screen, tuple(map(int, [slider.value for slider in self.RGB])),
                         ((int(screen.get_width() * 0.65)),
                          (int(screen.get_height() * 0.05)),
                          (int(screen.get_height() * 0.2)),
                          (int(screen.get_height() * 0.2))))
        self.OK.draw(screen)

    def mouse_in(self, pos_x, pos_y, width, height):
        for i, slider in enumerate(self.RGB):
            if slider.mouse_in(pos_x, pos_y, width, height):
                self.drawing[i] = True
                return
        if self.OK.mouse_in(pos_x, pos_y, width, height):
            return 'button_press'

    def motion(self, sdvig, width):
        for i, value in enumerate(self.drawing):
            if value:
                self.RGB[i].motion(sdvig, width)
                return list(map(int, [slider.value for slider in self.RGB]))
