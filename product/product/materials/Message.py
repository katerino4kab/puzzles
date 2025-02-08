import pygame
from materials.Button import Button


class Message:
    def __init__(self, mul_x, mul_y, mul_size, fir_btn_txt, sec_btn_txt):
        self.mul_x = mul_x
        self.mul_y = mul_y
        self.mul_size = mul_size
        self.fir_btn_txt = fir_btn_txt
        self.sec_btn_txt = sec_btn_txt
        self.fir_btn = Button(mul_x + (mul_size[0] / 10), mul_y + (mul_size[1] / 5) * 3,
                         (mul_size[0] / 10 * 3, mul_size[1] / 5), fir_btn_txt)
        self.sec_btn = Button(mul_x + ((mul_size[0] / 10) * 6), mul_y + (mul_size[1] / 5) * 3,
                           (mul_size[0] / 10 * 3, mul_size[1] / 5), sec_btn_txt)

    def draw(self, screen, text):
        pygame.draw.rect(screen, (95, 60, 125), (int(screen.get_width() * self.mul_x),
                                                 int(screen.get_height() * self.mul_y),
                                                 int(screen.get_width() * self.mul_size[0]),
                                                 int(screen.get_height() * self.mul_size[1])),
                         border_radius=int(screen.get_height() * self.mul_size[1]) // 4)
        font = pygame.font.Font(None, int(screen.get_width() * self.mul_size[0]) // len(text) * 2)
        text = font.render(text, True, (100, 255, 100))
        screen.blit(text, (int(screen.get_width() * self.mul_x) +
                           (int(screen.get_width() * self.mul_size[0]) - text.get_width()) // 2,
                           int(screen.get_height() * self.mul_y) +
                           (int(screen.get_height() * self.mul_size[1]) - text.get_height()) // 10 * 4))
        self.fir_btn.draw(screen)
        self.sec_btn.draw(screen)

    def mouse_in(self, pos_x, pos_y, width, height):
        if self.fir_btn.mouse_in(pos_x, pos_y, width, height):
            return self.fir_btn_txt
        if self.sec_btn.mouse_in(pos_x, pos_y, width, height):
            return self.sec_btn_txt
        return False
