import pygame
import sys

from product.games.puzzle import main_game
from product.games.rebus import rebus_game
from product.games.matching import main_m

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Выбор игры")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

font = pygame.font.Font(None, 36)

buttons = [
    {"text": "Ребусы", "rect": pygame.Rect(300, 150, 200, 50), "action": "rebus"},
    {"text": "Пазлы", "rect": pygame.Rect(300, 250, 200, 50), "action": "puzzle"},
    {"text": "Пятнашки", "rect": pygame.Rect(250, 100, 300, 50), "action": "match"}
]


def draw_button(button):
    pygame.draw.rect(screen, GRAY, button["rect"])
    text_surface = font.render(button["text"], True, BLACK)
    text_rect = text_surface.get_rect(center=button["rect"].center)
    screen.blit(text_surface, text_rect)


def main_menu(screen, music, volume):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        if button["rect"].collidepoint(event.pos):
                            print(f"Выбрана игра: {button['action']}")
                            if button["action"] == "rebus":
                                rebus_game()
                            elif button["action"] == "puzzle":
                                pass
                            elif button["action"] == "match":
                                main_m(screen, music, volume)

        for button in buttons:
            draw_button(button)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_menu()
