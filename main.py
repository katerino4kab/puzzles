import pygame
from logic.main_menu_logic import main_menu_logic
from logic.settings_logic import settings_logic
from product.games.connect import main_menu


music = 'music/main_menu_theme.mp3'
volume = 0
game_state = 'Menu'


def main():
    global game_state
    pygame.init()
    pygame.display.set_caption('ПРОТОТИП')
    screen = pygame.display.set_mode((500, 420))
    while True:
        if game_state == 'Menu':
            game_state = main_menu_logic(screen, music, volume)
        if game_state == 'Game':
            game_state = main_menu(screen, music, volume)
        if game_state == 'Created':
            pass
        if game_state == 'Settings':
            game_state = settings_logic(screen, music, volume)
        if game_state == 'About_Us':
            pass
        if game_state == 'Exit':
            pygame.quit()
            return


if __name__ == '__main__':
    main()
