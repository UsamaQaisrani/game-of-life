import pygame
from pygame import Color

BLACK = Color(0, 0, 0)
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
        self.states = []

    def setup(self):
        self.populate_grid()
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.fill(WHITE)
        running = True

        while running:
            self.draw_grid(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        print(f"Width: {len(self.grid)}, Height: {len(self.grid[0])}")
        pygame.quit()

    def populate_grid(self):
        for x in range(self.cols):
            grid_col = []
            state_col = []
            for y in range(self.rows):
                rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                grid_col.append(rect)
                state_col.append(0)
            self.grid.append(grid_col)
            self.states.append(state_col)

    def draw_grid(self, screen):
        for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
            for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)
                
