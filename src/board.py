import pygame
from pygame import Color

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GRAY = Color(128, 128, 128)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 720

class Board:
    def __init__(self) -> None:
        pass

    def setup(self):
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.fill(WHITE)
        running = True

        while running:
            self.drawGrid(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()

    def drawGrid(self, screen):
        blockSize = 15 
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, GRAY, rect, 1)
