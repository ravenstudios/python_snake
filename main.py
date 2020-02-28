from constants import *
import pygame
import snake
import apple

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

snake = snake.Snake()
apple = apple.Apple()

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
    apple.draw(surface)
    pygame.display.flip()



def update():
    snake.update()
    apple.update(snake)


if __name__ == "__main__":
    main()
