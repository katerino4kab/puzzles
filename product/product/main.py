import pygame
import sqlite3
from logic.main_menu_logic import main_menu_logic
from logic.settings_logic import settings_logic
from product.games.connect import connect_logic
from product.games.matching import main_m
from product.games.puzzle import main_game
from product.games.rebus import rebus_game


conn = sqlite3.connect('games.db')
cursor = conn.cursor()
music = 'music/main_menu_theme.mp3'
volume = 0
game_state = 'Menu'
image_path_to_insert = 'materials/puzzle.jpg'

cursor.execute('''
INSERT INTO images (path) VALUES (?)
''', (image_path_to_insert,))

conn.commit()
cursor.execute('SELECT path FROM images WHERE id = ?', (cursor.lastrowid,))
image_path = cursor.fetchone()[0]



def main():
    global game_state
    pygame.init()
    pygame.display.set_caption('Гамес')
    screen = pygame.display.set_mode((600, 600))
    while True:
        if game_state == 'Menu':
            game_state = main_menu_logic(screen, music, volume)
        if game_state == 'Game':
            game_state = connect_logic(screen, music, volume)
        if game_state == 'Created':
            pass
        if game_state == 'Settings':
            game_state = settings_logic(screen, music, volume)
        if game_state == 'About_Us':
            pass
        if game_state == 'Mutching':
            game_state = main_m(screen, music, volume)
        if game_state == 'Puzzle':
            game_state = main_game(screen, music, volume, image_path)
        if game_state == 'Rebus':
            game_state = rebus_game(screen, music, volume)
        if game_state == 'Exit':
            pygame.quit()
            return

conn.close()

if __name__ == '__main__':
    main()
