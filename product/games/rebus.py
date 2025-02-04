import pygame

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Ребусы")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
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

input_text = ""
active = False

check_button = pygame.Rect(300, 400, 200, 50)

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_button(rect, text, color):
    pygame.draw.rect(screen, color, rect)
    draw_text(text, rect.x + 20, rect.y + 15)

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.lower()

def rebus_game(screen, music, volume):
    global input_text, active, current_riddle

    running = True
    while running:
        screen.fill(WHITE)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)

        riddle = riddles[current_riddle]
        draw_text("Загадка:", 50, 50)
        draw_text(riddle["question"], 50, 100)

        input_rect = pygame.Rect(50, 200, 500, 50)
        pygame.draw.rect(screen, GRAY if not active else BLUE, input_rect, 2)
        draw_text(input_text, input_rect.x + 10, input_rect.y + 10)

        draw_button(check_button, "Проверить", GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Game'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if check_button.collidepoint(event.pos):
                    if check_answer(input_text, riddle["answer"]):
                        draw_text("Правильно!", 50, 500, GREEN)
                        current_riddle = (current_riddle + 1) % len(riddles)
                        input_text = ""
                    else:
                        draw_text("Неправильно! Попробуйте еще раз.", 50, 500, RED)
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        pygame.display.flip()
