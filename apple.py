import pygame
from constants import *
import random
class Apple:
    def __init__(self):

        self.rect = pygame.Rect(
        random.randint(0, COLS - 1) * BLOCK_SIZE,
        random.randint(0, ROWS - 1) * BLOCK_SIZE, BLOCK_SIZE,
        BLOCK_SIZE
        )
        self.relocate()


    def update(self, snake):
        if self.rect.colliderect(snake.get_rect()):
            snake.add_part()
            self.relocate()


    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

    def relocate(self):
        self.rect.x = random.randint(0, COLS) * BLOCK_SIZE
        self.rect.y = random.randint(0, ROWS) * BLOCK_SIZE
