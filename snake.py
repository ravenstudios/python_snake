from constants import *
import pygame

class Snake:
    def __init__(self):
        self.x = COLS // 2 * BLOCK_SIZE
        self.y = ROWS // 2 * BLOCK_SIZE
        self.width, self.height = BLOCK_SIZE, BLOCK_SIZE
        self.dir = "W"#moves east
        self.parts = [(self.x, self.y)]



    def update(self):
        self.key_input()
        self.move()
#check_collide_body() is called in move
#because we need to check if the new x
#and y are alread in the body_parts list
        # self.check_edge()


    def draw(self, surface):
        for part in self.parts:
            pygame.draw.rect(surface, BLACK, (part[0], part[1], self.width, self.height), 3)
            pygame.draw.rect(surface, WHITE, (part[0], part[1], self.width, self.height), 3)



    def check_edge(self):
        if self.x < 0 or self.x + BLOCK_SIZE > GAME_WIDTH or self.y < 0 or self.y + BLOCK_SIZE > GAME_HEIGHT:
            self.game_over()




    def check_collide_body(self):
        if (self.x, self.y) in self.parts:
            print("hit!!!")
            return True


    def game_over(self):
        print("game over")
        pygame.quit()



    def move(self):
        if self.dir == "N":
            self.y += -BLOCK_SIZE
        if self.dir == "E":
            self.x += BLOCK_SIZE
        if self.dir == "S":
            self.y += BLOCK_SIZE
        if self.dir == "W":
            self.x += -BLOCK_SIZE

        if self.check_collide_body():
            self.game_over()
#inserts the current x and y into the first
#position in the parts list and then removes the
#last item
        self.parts.insert(0, (self.x, self.y))
        self.parts.pop()



    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if self.dir != "S":
                self.dir = "N"
        if keys[pygame.K_DOWN]:
            if self.dir != "N":
                self.dir = "S"
        if keys[pygame.K_LEFT]:
            if self.dir != "E":
                self.dir = "W"
        if keys[pygame.K_RIGHT]:
            if self.dir != "W":
                self.dir = "E"
        if keys[pygame.K_SPACE]:
            self.add_part()



    def add_part(self):
        self.parts.insert(0, (self.x, self.y))



    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



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
