import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Snake')

background_color = pygame.Color(184, 194, 2)
fill_color = pygame.Color(112, 96, 1)
screen.fill(background_color)

snake_x = 100
snake_y = 100
snake_speed_x = 0
snake_speed_y = 0

while True:
    snake_x += snake_speed_x
    snake_y += snake_speed_y

    snake = pygame.Rect(snake_x, snake_y, 10, 10)
    pygame.draw.rect(screen, fill_color, snake)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Motion Events
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            snake_speed_x = -10
            snake_speed_y = 0
          if event.key == pygame.K_RIGHT:
            snake_speed_x = 10
            snake_speed_y = 0
          if event.key == pygame.K_UP:
            snake_speed_x = 0
            snake_speed_y = -10
          if event.key == pygame.K_DOWN:
            snake_speed_x = 0
            snake_speed_y = 10

    pygame.display.update()


    