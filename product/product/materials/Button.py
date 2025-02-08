import pygame


class Button:
    def __init__(self, mul_x, mul_y, mul_size, text, color_1=(165, 90, 195),
                 color_2=(95, 60, 125),
                 color_3=(100, 255, 100)):
        self.mul_x = mul_x
        self.mul_y = mul_y
        self.mul_size = mul_size
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.text = text
        self.mouse_at_button = False

    def draw(self, screen):
        color = self.color_2
        if not self.mouse_at_button:
            color = self.color_1
        pygame.draw.rect(screen, color, (int(screen.get_width() * self.mul_x),
                                         int(screen.get_height() * self.mul_y),
                                         int(screen.get_width() * self.mul_size[0]),
                                         int(screen.get_height() * self.mul_size[1])),
                         border_radius=int(screen.get_height() * self.mul_size[1]))
        font = pygame.font.Font(None, int(screen.get_height() * self.mul_size[1]))
        text = font.render(self.text, True, self.color_3)
        screen.blit(text, (int(screen.get_width() * self.mul_x) +
                           (int(screen.get_width() * self.mul_size[0]) - text.get_width()) // 2,
                           int(screen.get_height() * self.mul_y) +
                           (int(screen.get_height() * self.mul_size[1]) - text.get_height()) // 2))
        pygame.draw.rect(screen, self.color_2, (int(screen.get_width() * self.mul_x),
                                                int(screen.get_height() * self.mul_y),
                                                int(screen.get_width() * self.mul_size[0]),
                                                int(screen.get_height() * self.mul_size[1])),
                         int(screen.get_height() * self.mul_size[1] / 10),
                         int(screen.get_height() * self.mul_size[1]))

    def mouse_in(self, pos_x, pos_y, width, height):
        if (int(width * self.mul_x) <= pos_x <=
                int(width * self.mul_x) + int(width * self.mul_size[0]) and
                int(height * self.mul_y) <= pos_y <=
                int(height * self.mul_y) + int(height * self.mul_size[1])):
            self.mouse_at_button = True
            return True
        self.mouse_at_button = False
        return False
