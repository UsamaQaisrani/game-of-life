import pygame
from pygame import Color
from pattern import *

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
        self.grid = Pattern().setup()
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

    def draw_grid(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                x = j * BLOCKSIZE
                y = i * BLOCKSIZE
                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, BLACK, rect)  
                else:
                    pygame.draw.rect(screen, WHITE, rect)  
                pygame.draw.rect(screen, BLACK, rect, 1)  
                    
