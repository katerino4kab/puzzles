import pygame
import random
import os


pygame.init()


WIDTH, HEIGHT = 600, 600
TILE_SIZE = 200
GRID_SIZE = 3
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def load_image(image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    tiles = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            tile = image.subsurface(rect)
            tiles.append(tile)
    return tiles



def shuffle_tiles(tiles):
    random.shuffle(tiles)
    return tiles



def is_solved(tiles):
    for i in range(len(tiles)):
        if tiles[i] != original_tiles[i]:
            return False
    return True


def main_game(screen, music, volume, image_path):
    global original_tiles
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)
    original_tiles = load_image(image_path)
    tiles = shuffle_tiles(original_tiles.copy())

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Пазлы")
    clock = pygame.time.Clock()

    empty_tile_index = GRID_SIZE * GRID_SIZE - 1

    running = True
    while running:
        screen.fill(WHITE)

        for index, tile in enumerate(tiles):
            if index != empty_tile_index:
                x = (index % GRID_SIZE) * TILE_SIZE
                y = (index // GRID_SIZE) * TILE_SIZE
                screen.blit(tile, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'Game'

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                clicked_index = (mouse_y // TILE_SIZE) * GRID_SIZE + (mouse_x // TILE_SIZE)

                if clicked_index != empty_tile_index and is_adjacent(clicked_index, empty_tile_index):
                    tiles[empty_tile_index], tiles[clicked_index] = tiles[clicked_index], tiles[empty_tile_index]
                    empty_tile_index = clicked_index


        if is_solved(tiles):
            print("Поздравляем! Вы собрали пазл!")
            running = False

        pygame.display.flip()
        clock.tick(FPS)


def is_adjacent(index1, index2):
    row1, col1 = divmod(index1, GRID_SIZE)
    row2, col2 = divmod(index2, GRID_SIZE)
    return (row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1)


if __name__ == "__main__":
    image_path = "../materials/puzzle.jpg"
    if not os.path.exists(image_path):
        print(f"Изображение по пути '{image_path}' не найдено.")
    else:
        main_game(image_path)

    pygame.quit()
