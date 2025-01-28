import pygame
import random
import os

pygame.init()


WIDTH, HEIGHT = 400, 400
TILE_SIZE = WIDTH // 4
FPS = 30
FONT_SIZE = 24

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)


font = pygame.font.Font(None, FONT_SIZE)


class PuzzleGame:
    def __init__(self):
        self.grid_size = 4
        self.tiles = self.create_tiles()
        self.empty_tile_index = self.tiles.index(0)
        self.solved_tiles = list(range(self.grid_size ** 2))
        self.moves = 0
        self.start_time = pygame.time.get_ticks()

    def create_tiles(self):
        tiles = list(range(self.grid_size ** 2))
        random.shuffle(tiles)
        while not self.is_solvable(tiles):
            random.shuffle(tiles)
        return tiles

    def is_solvable(self, tiles):
        inversions = sum(
            1 for i in range(len(tiles)) for j in range(i + 1, len(tiles))
            if tiles[i] != 0 and tiles[j] != 0 and tiles[i] > tiles[j]
        )
        return inversions % 2 == 0

    def draw(self, screen):
        screen.fill(WHITE)
        for index, tile in enumerate(self.tiles):
            if tile != 0:
                x = (index % self.grid_size) * TILE_SIZE
                y = (index // self.grid_size) * TILE_SIZE
                pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE))
                text = font.render(str(tile), True, BLACK)
                text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(text, text_rect)

    def is_adjacent(self, index1, index2):
        row1, col1 = divmod(index1, self.grid_size)
        row2, col2 = divmod(index2, self.grid_size)
        return (row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1)

    def move_tile(self, index):
        if self.is_adjacent(index, self.empty_tile_index):
            self.tiles[self.empty_tile_index], self.tiles[index] = self.tiles[index], self.tiles[self.empty_tile_index]
            self.empty_tile_index = index
            self.moves += 1

    def is_solved(self):
        return self.tiles == self.solved_tiles

    def get_time_elapsed(self):
        return (pygame.time.get_ticks() - self.start_time) // 1000


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("15 Puzzle")
    clock = pygame.time.Clock()

    game = PuzzleGame()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                clicked_index = (mouse_y // TILE_SIZE) * game.grid_size + (mouse_x // TILE_SIZE)
                game.move_tile(clicked_index)

        game.draw(screen)

        moves_text = font.render(f"Moves: {game.moves}", True, BLACK)
        time_text = font.render(f"Time: {game.get_time_elapsed()}s", True, BLACK)
        screen.blit(moves_text, (10, HEIGHT - FONT_SIZE - 10))
        screen.blit(time_text, (WIDTH - time_text.get_width() - 10, HEIGHT - FONT_SIZE - 10))

        if game.is_solved():
            win_text = font.render("Поздравляем! Вы выиграли!", True, GREEN)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
