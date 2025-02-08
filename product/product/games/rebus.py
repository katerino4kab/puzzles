import pygame

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ребусы")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_PURPLE = (200, 180, 255)
DARK_PURPLE = (100, 80, 155)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.Font(None, 36)

# Загадки и ответы
riddles = [
    {"question": "Что можно увидеть с закрытыми глазами?", "answer": "сон"},
    {"question": "Что растет вниз головой?", "answer": "сосулька"},
    {"question": "Что можно разбить, даже если не трогать?", "answer": "молчание"}
]
current_riddle = 0

# Переменные для ввода текста
input_text = ""
active = False

# Функция для отрисовки текста
def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Функция для отрисовки кнопки с закругленными краями
def draw_button(rect, text, color, border_color, hover=False):
    if hover:
        pygame.draw.rect(screen, border_color, rect, border_radius=10)  # Контур кнопки
    pygame.draw.rect(screen, color, rect.inflate(-4, -4), border_radius=10)  # Основная кнопка
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Функция для проверки ответа
def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.lower()

# Основная функция игры "Ребусы"
def rebus_game(screen, music, volume):
    global input_text, active, current_riddle
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)

    running = True
    while running:
        screen.fill(WHITE)

        # Получаем текущие размеры окна
        window_width, window_height = screen.get_size()

        # Отображение текущей загадки
        riddle = riddles[current_riddle]
        draw_text("Загадка:", window_width * 0.1, window_height * 0.1)
        draw_text(riddle["question"], window_width * 0.1, window_height * 0.2)

        # Поле для ввода текста
        input_rect = pygame.Rect(window_width * 0.1, window_height * 0.4, window_width * 0.8, 50)
        pygame.draw.rect(screen, GRAY if not active else LIGHT_PURPLE, input_rect, border_radius=10)
        draw_text(input_text, input_rect.x + 10, input_rect.y + 10)

        # Кнопка "Проверить"
        check_button_rect = pygame.Rect(window_width * 0.35, window_height * 0.6, window_width * 0.3, 50)
        mouse_pos = pygame.mouse.get_pos()
        hover = check_button_rect.collidepoint(mouse_pos)
        draw_button(check_button_rect, "Проверить", LIGHT_PURPLE, DARK_PURPLE, hover)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Game'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if check_button_rect.collidepoint(event.pos):
                    if check_answer(input_text, riddle["answer"]):
                        draw_text("Правильно!", window_width * 0.1, window_height * 0.8, GREEN)
                        current_riddle = (current_riddle + 1) % len(riddles)  # Переход к следующей загадке
                        input_text = ""  # Очистка поля ввода
                    else:
                        draw_text("Неправильно! Попробуйте еще раз.", window_width * 0.1, window_height * 0.8, RED)
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.display.flip()
