from constants import *
import pygame
import snake

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

snake = snake.Snake()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    snake.draw(surface)
    pygame.display.flip()



def update():
    snake.update()



if __name__ == "__main__":
    main()
