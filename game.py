import pygame, sys
from pygame.locals import QUIT

from src.snake import Snake

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('Snake')

background_color = pygame.Color(184, 194, 2)
fill_color = pygame.Color(112, 96, 1)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

snake_x = 100
snake_y = 100

score = 0

snake = Snake(snake_x, snake_y, screen, fill_color)

font = pygame.font.SysFont(None, 36)
text_rendered = font.render("Snake", True, fill_color)
text_width = text_rendered.get_width()
text_x = (400 - text_width) // 2

game_area_margin = 30
rect_width = screen.get_width() - 2 * game_area_margin
rect_height = screen.get_height() - 2 * game_area_margin

game_area = pygame.Rect(game_area_margin, game_area_margin, rect_width, rect_height)

while True:
    clock.tick(30)

    screen.fill(background_color)
    pygame.draw.rect(screen, fill_color, game_area, 2)

    # surf = pygame.Surface((162, 100), fill_color)
    # pygame.draw.rect(surf, (0, 100, 255, 155), (0, 0, 162, 100), 21)

    screen.blit(text_rendered, (text_x, 5))  # Adjust the vertical position as needed


    snake.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Motion Events
        if event.type == pygame.KEYDOWN:
          snake.handle_event(event)

    pygame.display.update()


    