from constants import *
import pygame

class Snake:
    def __init__(self):
        self.x = COLS // 2 * BLOCK_SIZE
        self.y = ROWS // 2 * BLOCK_SIZE
        self.width, self.height = BLOCK_SIZE, BLOCK_SIZE
        self.dir = "E"#moves east
        self.parts = [(self.x, self.y)]
    def update(self):
        self.key_input()
        self.move()

    def draw(self, surface):
        for part in self.parts:
            pygame.draw.rect(surface, WHITE, (part[0], part[1], self.width, self.height))



    def move(self):
        if self.dir == "N":
            if self.y > 0:
                self.y += -BLOCK_SIZE
        if self.dir == "E":
            if self.x + self.width < GAME_WIDTH:
                self.x += BLOCK_SIZE
        if self.dir == "S":
            if self.y + self.height < GAME_HEIGHT:
                self.y += BLOCK_SIZE
        if self.dir == "W":
            if self.x > 0:
                self.x += -BLOCK_SIZE
        self.parts.insert(0, (self.x, self.y))
        self.parts.pop()



    def key_input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.dir = "N"
        if keys[pygame.K_DOWN]:
            self.dir = "S"
        if keys[pygame.K_LEFT]:
            self.dir = "W"
        if keys[pygame.K_RIGHT]:
            self.dir = "E"
        if keys[pygame.K_SPACE]:
            self.add_part()


    def add_part(self):
        self.parts.insert(0, (self.x, self.y))
        
class Body_Part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

    def update(self):
        pass



    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
