import pygame
from pygame import Color
from pattern import *
import time

ALIVE = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GRAY = Color(128, 128, 128)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BLOCKSIZE = 10 

class Board:
    def __init__(self) -> None:
        self.rows = WINDOW_HEIGHT // BLOCKSIZE
        self.cols = WINDOW_WIDTH // BLOCKSIZE
        self.grid = []

    def setup(self):
        self.grid = Pattern().setup()
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.fill(GRAY)
        running = True

        while running:
            self.draw_grid(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            self.grid = self.evolve()
            time.sleep(0.25)
        pygame.quit()

    def update(self, grid):
        self.grid = grid
        pygame.display.flip()

    def draw_grid(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                x = j * BLOCKSIZE
                y = i * BLOCKSIZE
                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, ALIVE, rect)  
                else:
                    pygame.draw.rect(screen, WHITE, rect)  
                pygame.draw.rect(screen, ALIVE, rect, 1)  
                    
    def evolve(self):
        evolved = [[0 for _ in row] for row in self.grid]
        ROWS, COLS = len(self.grid), len(self.grid[0])
        directions = [
            [-1,0], [1,0], [0,1], [0,-1],
            [1,1], [-1,-1], [-1,1], [1,-1]
        ]

        def valid_index(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        for r in range(ROWS):
            for c in range(COLS):
                n_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if valid_index(nr, nc) and self.grid[nr][nc] == 1:
                        n_count += 1

                cell_val = self.grid[r][c]
                if cell_val == 1:
                    if n_count < 2 or n_count > 3:
                        evolved[r][c] = 0
                    else:
                        evolved[r][c] = 1
                else:
                    if n_count == 3:
                        evolved[r][c] = 1

        return evolved

