import pygame

class Snake:
  def __init__(self, x, y, screen, fill_color):
    self.x = x
    self.y = y
    self.speed_x = 10
    self.speed_y = 10
    self.screen = screen
    self.fill_color = fill_color

  def update(self):
    self.x += self.speed_x
    self.y += self.speed_y

  def draw(self):
    snake = pygame.Rect(self.x, self.y, 10, 10)
    pygame.draw.rect(self.screen, self.fill_color, snake)

  def handle_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        self.speed_x = -10
        self.speed_y = 0
      if event.key == pygame.K_RIGHT:
        self.speed_x = 10
        self.speed_y = 0
      if event.key == pygame.K_UP:
        self.speed_x = 0
        self.speed_y = -10
      if event.key == pygame.K_DOWN:
        self.speed_x = 0
        self.speed_y = 10