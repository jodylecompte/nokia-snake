import pygame
import random

APPLE_COLOR = pygame.Color(255, 0, 0)

class Apple:
    def __init__(self, game_area, snake):
        self.game_area = game_area
        self.snake = snake
        self.size = 10 
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(self.game_area.left, self.game_area.right - self.size)
        y = random.randint(self.game_area.top, self.game_area.bottom - self.size)
        return pygame.Rect(x, y, self.size, self.size)

    def draw(self):
        pygame.draw.rect(self.snake.screen, APPLE_COLOR, self.position)

    def check_collision(self):
        return self.snake.rect.colliderect(self.position)

    def regenerate(self):
        self.position = self.generate_position()