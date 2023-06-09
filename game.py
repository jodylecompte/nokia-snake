import pygame, sys
from pygame.locals import QUIT

from src.snake import Snake

pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Snake')

background_color = pygame.Color(184, 194, 2)
fill_color = pygame.Color(112, 96, 1)
screen.fill(background_color)

snake_x = 100
snake_y = 100

snake = Snake(snake_x, snake_y, screen, fill_color)

while True:
    snake.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Motion Events
        if event.type == pygame.KEYDOWN:
          snake.handle_event(event)

    pygame.display.update()


    