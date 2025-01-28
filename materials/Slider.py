import pygame


class Slider:
    def __init__(self, mul_x, mul_y, mul_size, min, max, value,
                 color_1=(165, 90, 195),
                 color_2=(95, 60, 125),
                 color_3=(100, 255, 100),
                 orientation='horizontal'
                 ):
        self.mul_x = mul_x
        self.mul_y = mul_y
        self.mul_size = mul_size
        self.min = min
        self.max = max
        self.value = value
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.orientation = orientation
        self.LMB = False

    def draw(self, screen):
        if self.orientation == 'horizontal':
            self.draw_horizontal(screen)
        else:
            self.draw_vertical(screen)

    def mouse_in(self, pos_x, pos_y, width, height):
        if self.orientation == "horizontal":
            return ((((int(width * self.mul_x) +
                       int(height * self.mul_size[1]) // 2 +
                       (int(width * self.mul_size[0]) / (self.max - self.min)) * self.value) -
                      int(height * self.mul_size[1]) // 10 * 3) <= pos_x <= (
                             (int(width * self.mul_x) +
                              int(height * self.mul_size[1]) // 2 +
                              (int(width * self.mul_size[0]) / (self.max - self.min)) * self.value) +
                             int(height * self.mul_size[1]) // 10 * 3)) and
                    (((int(height * self.mul_y) + int(height * self.mul_size[1]) // 2) -
                      int(height * self.mul_size[1]) // 10 * 3) <= pos_y <= (
                             (int(height * self.mul_y) + int(height * self.mul_size[1]) // 2) +
                             int(height * self.mul_size[1]) // 10 * 3)))

        return ((int(width * self.mul_x) <= pos_x <= (int(width * self.mul_x) + (int(width * self.mul_size[0]))))
                and (int(height * self.mul_y) + (int(height * self.mul_size[1]) /
                                                 (self.max - self.min)) * self.value - (int(width * self.mul_size[0]))
                     <= pos_y <= int(height * self.mul_y) + (int(height * self.mul_size[1]) /
                                                             (self.max - self.min)) * self.value
                     - (int(width * self.mul_size[0]))))

    def motion(self, shift, width, height):
        if self.orientation == 'horizontal':
            if self.min <= self.value + shift / ((width * self.mul_size[0]) / (self.max - self.min)) <= self.max:
                self.value += shift / ((width * self.mul_size[0]) / (self.max - self.min))
        else:
            if self.min <= self.value + shift / ((height * self.mul_size[1]) / (self.max - self.min)) <= self.max:
                self.value += shift / ((height * self.mul_size[1]) / (self.max - self.min))

    def draw_horizontal(self, screen):
        pygame.draw.rect(screen, self.color_1, ((int(screen.get_width() * self.mul_x)),
                                                (int(screen.get_height() * self.mul_y)),
                                                (int(screen.get_width() * self.mul_size[0]) +
                                                 int(screen.get_height() * self.mul_size[1])),
                                                (int(screen.get_height() * self.mul_size[1]))),
                         border_radius=int(screen.get_height() * self.mul_size[1]))
        pygame.draw.rect(screen, self.color_2, ((int(screen.get_width() * self.mul_x)),
                                                (int(screen.get_height() * self.mul_y)),
                                                (int(screen.get_width() * self.mul_size[0]) +
                                                 int(screen.get_height() * self.mul_size[1])),
                                                (int(screen.get_height() * self.mul_size[1]))),
                         (int(screen.get_height() * self.mul_size[1])) // 10,
                         int(screen.get_height() * self.mul_size[1]))
        pygame.draw.line(screen, self.color_2,
                         (int(screen.get_width() * self.mul_x) + int(screen.get_height() * self.mul_size[1]) // 2,
                          int(screen.get_height() * self.mul_y) + int(screen.get_height() * self.mul_size[1]) // 2),
                         (int(screen.get_width() * self.mul_x) + (int(screen.get_width() * self.mul_size[0]) + int(
                             screen.get_height() * self.mul_size[1]) // 2),
                          int(screen.get_height() * self.mul_y) + int(screen.get_height() * self.mul_size[1]) // 2),
                         int(screen.get_height() * self.mul_size[1]) // 10)
        if self.LMB:
            pygame.draw.circle(screen, self.color_3,
                               (int(screen.get_width() * self.mul_x) +
                                int(screen.get_height() * self.mul_size[1]) // 2 +
                                (int(screen.get_width() * self.mul_size[0]) / (self.max - self.min)) * self.value,
                                int(screen.get_height() * self.mul_y) + int(
                                    screen.get_height() * self.mul_size[1]) // 2),
                               int(screen.get_height() * self.mul_size[1]) // 10 * 3)
        else:
            pygame.draw.circle(screen, self.color_2,
                               (int(screen.get_width() * self.mul_x) +
                                int(screen.get_height() * self.mul_size[1]) // 2 +
                                (int(screen.get_width() * self.mul_size[0]) / (self.max - self.min)) * self.value,
                                int(screen.get_height() * self.mul_y) + int(
                                    screen.get_height() * self.mul_size[1]) // 2),
                               int(screen.get_height() * self.mul_size[1]) // 10 * 3)

    def draw_vertical(self, screen):
        pygame.draw.rect(screen, self.color_1, ((int(screen.get_width() * self.mul_x)),
                                                (int(screen.get_height() * self.mul_y)),
                                                (int(screen.get_width() * self.mul_size[0])),
                                                (int(screen.get_height() * self.mul_size[1]))),
                         border_radius=int(screen.get_height() * self.mul_size[1]))
        pygame.draw.rect(screen, self.color_2, ((int(screen.get_width() * self.mul_x)),
                                                (int(screen.get_height() * self.mul_y)),
                                                (int(screen.get_width() * self.mul_size[0])),
                                                (int(screen.get_height() * self.mul_size[1]))),
                         (int(screen.get_width() * self.mul_size[0])) // 10,
                         int(screen.get_width() * self.mul_size[0]))
        pygame.draw.line(screen, self.color_2,
                         (int(screen.get_width() * self.mul_x) + int(screen.get_width() * self.mul_size[0]) // 2,
                          int(screen.get_height() * self.mul_y) + int(screen.get_width() * self.mul_size[0]) // 2),
                         (int(screen.get_width() * self.mul_x) + int(screen.get_width() * self.mul_size[0]) // 2,
                          int(screen.get_height() * self.mul_y) + int(screen.get_height() * self.mul_size[1])
                          - int(screen.get_width() * self.mul_size[0]) // 2),
                         int(screen.get_width() * self.mul_size[0]) // 10)

        if self.LMB:
            pygame.draw.circle(screen, self.color_3,
                               (int(screen.get_width() * self.mul_x) +
                                int(screen.get_width() * self.mul_size[0]) // 2,
                                int(screen.get_height() * self.mul_y) +
                                (int(screen.get_height() * self.mul_size[1]) / (self.max - self.min)) * self.value),
                               int(screen.get_width() * self.mul_size[0]) // 10 * 3)
        else:
            pygame.draw.circle(screen, self.color_2,
                               (int(screen.get_width() * self.mul_x) +
                                int(screen.get_width() * self.mul_size[0]) // 2,
                                int(screen.get_height() * self.mul_y) +
                                (int(screen.get_height() * self.mul_size[1]) / (self.max - self.min)) * self.value),
                               int(screen.get_width() * self.mul_size[0]) // 10 * 3)
